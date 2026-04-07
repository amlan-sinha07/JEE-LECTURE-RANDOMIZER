import random


math_chapters = [
    ("Basic Math", 15), ("Quadratic Equations", 9), ("Sequences & Series", 9),
    ("Trigonometric Functions", 8), ("Trigonometric Equations", 4), ("PNC", 9),
    ("Binomial Theorem", 0), ("Straight Lines", 9), ("Circle", 9),
    ("Parabola", 7), ("Ellipse", 5), ("Solution of Triangles", 4),
    ("Hyperbola", 4), ("Determinants", 3), ("Matrices", 7), ("Sets", 2),
    ("Functions", 14), ("ITF", 5), ("Limits", 10), ("MOD", 4),
    ("AOD", 10), ("Indefinite Integration", 6), ("STST", 3),
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
    ("Mathematical Tools", 8), ("Motion in a Straight Line", 7),
    ("Motion in a Plane", 4), ("Relative Motion", 4), ("Laws of Motion", 13),
    ("Work, Energy and Power", 9), ("Circular Motion", 10),
    ("COM and System of Particles", 15), ("Rotational Motion", 20),
    ("Oscillations", 8), ("Ray Optics and Optical Instruments", 19),
    ("Dual Nature", 4), ("Atom", 3), ("Nuclei", 3),
    ("Thermal Properties of Matter", 6), ("Kinetic Theory of Gases", 3),
    ("Thermodynamics", 4), ("Mechanical Properties of Solids", 1),
    ("Mechanical Properties of Fluids", 9),
    ("Electric Charges, Fields and Potential", 17),
    ("Current Electricity", 9), ("Gravitation", 2),
    ("Units and Measurements", 2),
    ("Electrostatic Potential and Capacitance", 6),
    ("Moving Charges and Magnetism", 12), ("Electromagnetic Induction", 7),
    ("Alternating Current", 3), ("Waves", 9),
    ("Electromagnetic Waves", 1), ("Wave Optics", 6), ("Semiconductor", 2),
]


def pick_different(chapters, prev_index):
    """Pick a random chapter index different from the previous one."""
    choices = [i for i in range(len(chapters)) if i != prev_index]
    return random.choice(choices)


NUM_ATTEMPTS = 4

col_w = 36  
print(f"{'Attempt':<10} {'Physics':<{col_w}} {'Chemistry':<{col_w}} {'Math':<{col_w}}")
print("-" * (10 + col_w * 3))

prev_p = prev_c = prev_m = -1

for i in range(1, NUM_ATTEMPTS + 1):
    pi = pick_different(phy_chapters,  prev_p)
    ci = pick_different(chem_chapters, prev_c)
    mi = pick_different(math_chapters, prev_m)

    prev_p, prev_c, prev_m = pi, ci, mi

    p_name, p_lec = phy_chapters[pi]
    c_name, c_lec = chem_chapters[ci]
    m_name, m_lec = math_chapters[mi]

    p_str = f"Lec {p_lec} | {p_name}"
    c_str = f"Lec {c_lec} | {c_name}"
    m_str = f"Lec {m_lec} | {m_name}"

    print(f"{i:<10} {p_str:<{col_w}} {c_str:<{col_w}} {m_str:<{col_w}}")
