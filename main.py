import random

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
    ("Math Tools", 8), ("Stra Line", 7),
    ("Plane", 4), ("Rela Moti", 4), ("Laws of Moti", 13),
    ("WEP", 9), ("Circ Moti", 10),
    ("COM and Sys of Part", 15), ("Rota Moti", 20),
    ("Oscil", 8), ("Ray", 19),
    ("Dual Nature", 4), ("Atom", 3), ("Nuclei", 3),
    ("Thermal Propert", 6), ("Kinetic ", 3),
    ("Thermo", 4), ("Solids", 1),
    ("Fluids", 9),
    ("Elec Char, Fiel and Pote", 17),
    ("Curr Elec", 9), ("Grav", 2),
    ("Unit and Meas", 2),
    ("Elec Pote and Capa", 6),
    ("Movi Char and Magn", 12), ("Elec Indu", 7),
    ("Alte Curr", 3), ("Waves", 9),
    ("Elec Wave", 1), ("Wave Opti", 6), ("Semi", 2),
]


def pick_different(chapters, prev_index):
    choices = [i for i in range(len(chapters)) if i != prev_index]
    return random.choice(choices)


def pick_lecture(total):
    """Pick a lecture number with low weight on first and last."""
    if total == 1:
        return 1
    population = list(range(1, total + 1))
    # First and last get weight 1, middle lectures get weight 4
    weights = [1] + [4] * (total - 2) + [1] if total > 2 else [1, 1]
    return random.choices(population, weights=weights, k=1)[0]


NUM_ATTEMPTS = 8

col_w = 36
print(f"{'Attempt':<10} {'Physics':<{col_w}} {'Chemistry':<{col_w}} {'Math':<{col_w}}")
print("-" * (10 + col_w * 3))

prev_p = prev_c = prev_m = -1

for i in range(1, NUM_ATTEMPTS + 1):
    pi = pick_different(phy_chapters,  prev_p)
    ci = pick_different(chem_chapters, prev_c)
    mi = pick_different(math_chapters, prev_m)

    prev_p, prev_c, prev_m = pi, ci, mi

    p_name, p_total = phy_chapters[pi]
    c_name, c_total = chem_chapters[ci]
    m_name, m_total = math_chapters[mi]

    # Pick a specific lecture number with weightage applied
    p_lec = pick_lecture(p_total)
    c_lec = pick_lecture(c_total)
    m_lec = pick_lecture(m_total)

    p_str = f"Lec {p_lec}/{p_total} | {p_name}"
    c_str = f"Lec {c_lec}/{c_total} | {c_name}"
    m_str = f"Lec {m_lec}/{m_total} | {m_name}"

    print(f"{i:<10} {p_str:<{col_w}} {c_str:<{col_w}} {m_str:<{col_w}}")
