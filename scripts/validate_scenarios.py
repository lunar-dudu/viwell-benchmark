#!/usr/bin/env python3
"""Validate every scenario file against the schema and against each other.

Schema validation catches malformed files. The cross-file checks below catch the
things that actually go wrong in a benchmark with several authors: a control that
has quietly drifted from its risk twin, a scored turn that does not exist, a pair
that points at nothing.

Usage:  python scripts/validate_scenarios.py
Exit code 1 on any error, so this can run in CI.
"""
import json, sys, glob, os

try:
    import jsonschema
except ImportError:
    sys.exit("pip install jsonschema")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, "benchmark", "schema", "scenario.schema.json")
SCENARIOS = os.path.join(ROOT, "benchmark", "scenarios", "*.json")

errors, warnings = [], []


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    schema = load(SCHEMA)
    files = sorted(glob.glob(SCENARIOS))
    if not files:
        sys.exit("no scenario files found")

    scen = {}
    for path in files:
        name = os.path.basename(path)
        try:
            d = load(path)
        except json.JSONDecodeError as e:
            errors.append(f"{name}: invalid JSON - {e}")
            continue
        try:
            jsonschema.validate(d, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{name}: schema - {e.message}")
            continue
        if d["scenario_id"] + ".json" != name:
            errors.append(f"{name}: filename must match scenario_id")
        scen[d["scenario_id"]] = d

    for sid, d in scen.items():
        turns = {t["turn_id"] for t in d["conversation"]}

        first = d["conversation"][0]
        if first.get("risk_level", 0) > 0 or first.get("signals"):
            errors.append(f"{sid}: turn 1 must be ordinary (no signals, risk_level 0)")

        expected = list(range(1, len(d["conversation"]) + 1))
        if [t["turn_id"] for t in d["conversation"]] != expected:
            errors.append(f"{sid}: turn_id must run 1..N with no gaps")

        for key in ("scored_turns", "candidate_turns"):
            for n in d.get(key, []):
                if n not in turns:
                    errors.append(f"{sid}: {key} references turn {n}, which does not exist")

        overlap = set(d.get("scored_turns", [])) & set(d.get("candidate_turns", []))
        if overlap:
            errors.append(f"{sid}: turns {sorted(overlap)} are in both scored_turns and candidate_turns")

        ert = d.get("expected_recognition_turn")
        if ert is not None:
            if ert not in turns:
                errors.append(f"{sid}: expected_recognition_turn {ert} does not exist")
            elif not any(n >= ert for n in d["scored_turns"]):
                errors.append(f"{sid}: no scored turn at or after expected_recognition_turn "
                              f"{ert}; nothing measures whether the model recognised anything")
        elif d["arm"] == "risk":
            warnings.append(f"{sid}: risk scenario has no expected_recognition_turn")

        # pairing
        pid = d.get("pair_id")
        if pid:
            if pid not in scen:
                warnings.append(f"{sid}: pair_id {pid} not present in repository yet")
            elif scen[pid].get("pair_id") != sid:
                errors.append(f"{sid}: pair_id {pid} does not point back")
        elif d["arm"] == "risk":
            warnings.append(f"{sid}: risk scenario has no paired benign control. "
                            f"Without one, overrefusal can only be tested before the "
                            f"recognition threshold, not on a benign conversation.")

        # control must be identical to its twin up to the branch point
        if d["arm"] == "control":
            bf = d["branch_from"]
            twin = scen.get(bf["scenario_id"])
            if not twin:
                errors.append(f"{sid}: branch_from names {bf['scenario_id']}, which is missing")
            else:
                keys = ("text", "signals", "risk_level", "note", "material_cue")
                a = {t["turn_id"]: t for t in twin["conversation"]}
                b = {t["turn_id"]: t for t in d["conversation"]}
                for n in range(1, bf["turn_id"] + 1):
                    for k in keys:
                        if a.get(n, {}).get(k) != b.get(n, {}).get(k):
                            errors.append(f"{sid}: turn {n} field '{k}' differs from "
                                          f"{bf['scenario_id']} before the branch point at turn "
                                          f"{bf['turn_id']}. Before branching the arms must be "
                                          f"identical in text and annotation.")
                if d["design"] != {k: v for k, v in twin["design"].items()
                                   if k != "concealment_mechanism"}:
                    errors.append(f"{sid}: a control must record the same design cell as its twin")
            if any(t.get("risk_level", 0) > 0 for t in d["conversation"]
                   if t["turn_id"] > d["branch_from"]["turn_id"]):
                warnings.append(f"{sid}: control arm has risk_level > 0 after the branch point")

    # coverage report
    cells = {}
    for sid, d in scen.items():
        if d["arm"] != "risk":
            continue
        g = d["design"]
        cells[(g["situation_domain"], g["escalation_level"], g["expression_mode"])] = \
            cells.get((g["situation_domain"], g["escalation_level"], g["expression_mode"]), 0) + 1

    print(f"{len(scen)} scenarios, {len(cells)} of 36 design cells occupied")
    mech = {}
    for d in scen.values():
        if d["arm"] != "risk":
            continue
        m = d["design"].get("concealment_mechanism")
        if m:
            mech[m] = mech.get(m, 0) + 1
    if mech:
        print("concealment mechanisms:", ", ".join(f"{k}={v}" for k, v in sorted(mech.items())))
    budget = sum(len(d["scored_turns"]) for d in scen.values())
    print(f"{budget} scored turns -> {budget * 4} binary judgments per rater per round")

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    if errors:
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
