import random
import json
import os
from datetime import date

DATA_FILE = "jee_progress.json"

math_chapters = [
    ("Basic Math", 15), ("Quadratic Equations", 9), ("Sequences & Series", 9),
    ("Trigonometric Functions", 8), ("Trigonometric Equations", 4), ("PNC", 9),
    ("Binomial Theorem", 8), ("Straight Lines", 9), ("Circle", 9),
    ("Parabola", 7), ("Ellipse", 5), ("Solution of Triangles", 4),
    ("Hyperbola", 4), ("Determinants", 3), ("Matrices", 7), ("Sets", 2),
    ("Functions", 14), ("ITF", 5), ("Limits", 10), ("MOD", 4),
    ("AOD", 10), ("Indefinite Integration", 6), ("STAT", 3),
    ("Definite Integration", 6), ("AOI", 4), ("Differential Equations", 3),
    ("Vector Algebra", 8), ("3D Geometry", 4), ("Probability", 5),
    ("Complex Numbers", 7),
]
chem_chapters = [
    ("SBCOC", 16), ("Redox Reactions", 8), ("Solutions", 11),
    ("Chemical Kinetics", 10), ("Thermodynamics", 13), ("Chemical Equilibrium", 5),
    ("Ionic Equilibrium", 6), ("Structure of Atom", 9), ("Electrochemistry", 8),
    ("Solid State", 5), ("States of Matter", 4), ("Surface Chemistry", 1),
    ("Periodic Table", 14), ("Chemical Bonding", 21), ("Coordination Compounds", 18),
    ("Salt Analysis", 12), ("P Block", 6), ("D and F Block", 1),
    ("S Block", 1), ("Hydrogen", 1), ("Metallurgy", 2), ("IUPAC", 10),
    ("GOC", 14), ("Isomerism", 17), ("Hydrocarbons", 15), ("Haloalkanes", 8),
    ("Alcohols", 6), ("Aldehydes & Ketones", 6), ("Amines", 2),
    ("Biomolecules", 3), ("Polymers", 1), ("Chemistry in Everyday Life", 2),
    ("Environmental Chemistry", 1),
]
phy_chapters = [
    ("Math Tools", 8), ("Straight Line Motion", 7), ("Plane Motion", 4),
    ("Relative Motion", 4), ("Laws of Motion", 13), ("WEP", 9),
    ("Circular Motion", 10), ("COM & System of Particles", 15), ("Rotational Motion", 20),
    ("Oscillations", 8), ("Ray Optics", 19), ("Dual Nature", 4),
    ("Atoms", 3), ("Nuclei", 3), ("Thermal Properties", 6), ("Kinetic Theory", 3),
    ("Thermodynamics", 4), ("Solids", 1), ("Fluids", 9),
    ("Electric Charge, Field & Potential", 17), ("Current Electricity", 9),
    ("Gravitation", 2), ("Units & Measurement", 2),
    ("Electric Potential & Capacitance", 6), ("Moving Charges & Magnetism", 12),
    ("Electromagnetic Induction", 7), ("Alternating Current", 3),
    ("Waves", 9), ("EM Waves", 1), ("Wave Optics", 6), ("Semiconductors", 2),
]

# ── persistence ────────────────────────────────────────────────────────────────

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {
        "done": {"phy": {}, "che": {}, "mat": {}},
        "prev_idx": {"phy": -1, "che": -1, "mat": -1},
        "history": [],
        "rolls": 0,
    }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ── weighted pickers ───────────────────────────────────────────────────────────

def pick_chapter(chapters, prev_idx, done_map):
    weights = []
    for i, (_, total) in enumerate(chapters):
        if i == prev_idx:
            weights.append(0)
            continue
        done_count = len(done_map.get(str(i), []))
        pct = done_count / total
        weights.append(max(0.5, 4 * (1 - pct)))
    return random.choices(range(len(chapters)), weights=weights, k=1)[0]

def pick_lecture(total, done_list):
    population = list(range(1, total + 1))
    weights = []
    for lec in population:
        if lec in done_list:
            weights.append(0.3)
        elif lec == 1 or lec == total:
            weights.append(1)
        else:
            weights.append(4)
    return random.choices(population, weights=weights, k=1)[0]

# ── display helpers ────────────────────────────────────────────────────────────

def progress_bar(done, total, width=16):
    filled = int(done / total * width) if total else 0
    return f"[{'█' * filled}{'░' * (width - filled)}] {done}/{total}"

def print_stats(data):
    subjects = [
        ("Physics",   phy_chapters,  "phy"),
        ("Chemistry", chem_chapters, "che"),
        ("Math",      math_chapters, "mat"),
    ]
    total_done = total_lecs = 0
    print("\n── Overall Progress ──────────────────────────────────")
    for label, chapters, key in subjects:
        done = sum(len(v) for v in data["done"][key].values())
        total = sum(t for _, t in chapters)
        total_done += done
        total_lecs += total
        print(f"  {label:<12} {progress_bar(done, total)}  {done}/{total}")
    print(f"  {'TOTAL':<12} {progress_bar(total_done, total_lecs)}  "
          f"{round(total_done/total_lecs*100)}%")
    print(f"  Total rolls: {data['rolls']}")

def print_result(pi, ci, mi, pl, cl, ml):
    col = 38
    p_str = f"Lec {pl}/{phy_chapters[pi][1]}  {phy_chapters[pi][0]}"
    c_str = f"Lec {cl}/{chem_chapters[ci][1]}  {chem_chapters[ci][0]}"
    m_str = f"Lec {ml}/{math_chapters[mi][1]}  {math_chapters[mi][0]}"
    print("\n" + "─" * (10 + col * 3))
    print(f"  {'PHYSICS':<{col}} {'CHEMISTRY':<{col}} {'MATH':<{col}}")
    print(f"  {p_str:<{col}} {c_str:<{col}} {m_str:<{col}}")
    print("─" * (10 + col * 3))

def print_history(history):
    if not history:
        print("  No history yet.")
        return
    col = 38
    print(f"\n  {'#':<4} {'Physics':<{col}} {'Chemistry':<{col}} {'Math':<{col}}")
    print("  " + "─" * (4 + col * 3))
    for i, h in enumerate(history, 1):
        p = f"Lec {h['phy']['lec']}/{h['phy']['tot']}  {h['phy']['ch']}"
        c = f"Lec {h['che']['lec']}/{h['che']['tot']}  {h['che']['ch']}"
        m = f"Lec {h['mat']['lec']}/{h['mat']['tot']}  {h['mat']['ch']}"
        print(f"  {i:<4} {p:<{col}} {c:<{col}} {m:<{col}}")

# ── mark done helper ───────────────────────────────────────────────────────────

def toggle_done(data, subj, idx, lec):
    key = str(idx)
    arr = data["done"][subj].setdefault(key, [])
    if lec in arr:
        arr.remove(lec)
        return False
    else:
        arr.append(lec)
        return True

# ── main loop ──────────────────────────────────────────────────────────────────

def main():
    data = load_data()
    last_roll = None  # (pi, ci, mi, pl, cl, ml)

    print("\n╔══════════════════════════════════════╗")
    print("║     JEE Lecture Randomizer  v2.0     ║")
    print("╚══════════════════════════════════════╝")

    while True:
        print("\nOptions:  [r] Roll   [d] Mark done   [s] Stats   [h] History   [reset] Reset   [q] Quit")
        cmd = input(">>> ").strip().lower()

        if cmd == "q":
            print("Bye! Keep grinding.")
            break

        elif cmd == "r":
            pi = pick_chapter(phy_chapters,  data["prev_idx"]["phy"], data["done"]["phy"])
            ci = pick_chapter(chem_chapters, data["prev_idx"]["che"], data["done"]["che"])
            mi = pick_chapter(math_chapters, data["prev_idx"]["mat"], data["done"]["mat"])
            data["prev_idx"] = {"phy": pi, "che": ci, "mat": mi}

            pl = pick_lecture(phy_chapters[pi][1],  data["done"]["phy"].get(str(pi), []))
            cl = pick_lecture(chem_chapters[ci][1], data["done"]["che"].get(str(ci), []))
            ml = pick_lecture(math_chapters[mi][1], data["done"]["mat"].get(str(mi), []))

            last_roll = (pi, ci, mi, pl, cl, ml)
            data["rolls"] += 1
            data["history"].insert(0, {
                "phy": {"ch": phy_chapters[pi][0],  "lec": pl, "tot": phy_chapters[pi][1]},
                "che": {"ch": chem_chapters[ci][0], "lec": cl, "tot": chem_chapters[ci][1]},
                "mat": {"ch": math_chapters[mi][0], "lec": ml, "tot": math_chapters[mi][1]},
            })
            if len(data["history"]) > 20:
                data["history"] = data["history"][:20]

            save_data(data)
            print_result(pi, ci, mi, pl, cl, ml)

        elif cmd == "d":
            if not last_roll:
                print("  Roll first, then mark lectures as done.")
                continue
            pi, ci, mi, pl, cl, ml = last_roll
            print(f"\n  Which subject? (p=Physics, c=Chemistry, m=Math, a=All, x=Cancel)")
            sub = input("  >>> ").strip().lower()
            map_ = {"p": ("phy", pi, pl), "c": ("che", ci, cl), "m": ("mat", mi, ml)}
            targets = list(map_.values()) if sub == "a" else ([map_[sub]] if sub in map_ else [])
            for subj, idx, lec in targets:
                added = toggle_done(data, subj, idx, lec)
                ch_name = {"phy": phy_chapters, "che": chem_chapters, "mat": math_chapters}[subj][idx][0]
                status = "✓ marked done" if added else "✗ unmarked"
                print(f"  {status}: {ch_name} Lec {lec}")
            save_data(data)

        elif cmd == "s":
            print_stats(data)

        elif cmd == "h":
            print("\n── Roll History ──────────────────────────────────────")
            print_history(data["history"])

        elif cmd == "reset":
            confirm = input("  Type YES to reset all progress: ").strip()
            if confirm == "YES":
                data["done"] = {"phy": {}, "che": {}, "mat": {}}
                save_data(data)
                print("  Progress reset.")
            else:
                print("  Cancelled.")

        else:
            print("  Unknown command.")

if __name__ == "__main__":
    main()
