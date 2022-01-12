import re



def get_mapping(df, valid_databases, pd):
    mapping = {}
    for id, row in df.iterrows():
        mapping[id] = {}
        #print(dir(row))
        for db in df.keys():
            #print(db)
            if db in valid_databases:
                value = row[db]
                if not pd.isna(value):
                    mapping[id][db] = value
    return mapping


def atom_count(formula):
    atoms = {}
    pairs = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    for p in pairs:
        if not p[0] in atoms:
            atoms[p[0]] = 0
        v = p[1]
        if len(v) == 0:
            v = 1
        atoms[p[0]] += int(v)
        #print(p[0], v)
    return atoms


def is_valid_formula(f, pt):
    atoms = atom_count(f)
    for e in atoms:
        name = pt.get_element_name(e)
        if name == None:
            return False
    return True


class PeriodicTable:
    
    def __init__(self):
        self.elements_v = {
            "Ac": 89,
            "Ag": 47,
            "Al": 13,
            "Am": 95,
            "Ar": 18,
            "As": 33,
            "At": 85,
            "Au": 79,
            "B": 5,
            "Ba": 56,
            "Be": 4,
            "Bh": 107,
            "Bi": 83,
            "Bk": 97,
            "Br": 35,
            "C": 6,
            "Ca": 20,
            "Cd": 48,
            "Ce": 58,
            "Cf": 98,
            "Cl": 17,
            "Cm": 96,
            "Cn": 112,
            "Co": 27,
            "Cr": 24,
            "Cs": 55,
            "Cu": 29,
            "Db": 105,
            "Ds": 110,
            "Dy": 66,
            "Er": 68,
            "Es": 99,
            "Eu": 63,
            "F": 9,
            "Fe": 26,
            "Fl": 114,
            "Fm": 100,
            "Fr": 87,
            "Ga": 31,
            "Gd": 64,
            "Ge": 32,
            "H": 1,
            "He": 2,
            "Hf": 72,
            "Hg": 80,
            "Ho": 67,
            "Hs": 108,
            "I": 53,
            "In": 49,
            "Ir": 77,
            "K": 19,
            "Kr": 36,
            "La": 57,
            "Li": 3,
            "Lr": 103,
            "Lu": 71,
            "Lv": 116,
            "Mc": 115,
            "Md": 101,
            "Mg": 12,
            "Mn": 25,
            "Mo": 42,
            "Mt": 109,
            "N": 7,
            "Na": 11,
            "Nb": 41,
            "Nd": 60,
            "Ne": 10,
            "Nh": 113,
            "Ni": 28,
            "No": 102,
            "Np": 93,
            "O": 8,
            "Og": 118,
            "Os": 76,
            "P": 15,
            "Pa": 91,
            "Pb": 82,
            "Pd": 46,
            "Pm": 61,
            "Po": 84,
            "Pr": 59,
            "Pt": 78,
            "Pu": 94,
            "Ra": 88,
            "Rb": 37,
            "Re": 75,
            "Rf": 104,
            "Rg": 111,
            "Rh": 45,
            "Rn": 86,
            "Ru": 44,
            "S": 16,
            "Sb": 51,
            "Sc": 21,
            "Se": 34,
            "Sg": 106,
            "Si": 14,
            "Sm": 62,
            "Sn": 50,
            "Sr": 38,
            "Ta": 73,
            "Tb": 65,
            "Tc": 43,
            "Te": 52,
            "Th": 90,
            "Ti": 22,
            "Tl": 81,
            "Tm": 69,
            "Ts": 117,
            "U": 92,
            "V": 23,
            "W": 74,
            "Xe": 54,
            "Y": 39,
            "Yb": 70,
            "Zn": 30,
            "Zr": 40
        }
        self.elements = {
            "Ac": "Actinium",
            "Ag": "Silver",
            "Al": "Aluminum",
            "Am": "Americium",
            "Ar": "Argon",
            "As": "Arsenic",
            "At": "Astatine",
            "Au": "Gold",
            "B": "Boron",
            "Ba": "Barium",
            "Be": "Beryllium",
            "Bh": "Bohrium",
            "Bi": "Bismuth",
            "Bk": "Berkelium",
            "Br": "Bromine",
            "C": "Carbon",
            "Ca": "Calcium",
            "Cd": "Cadmium",
            "Ce": "Cerium",
            "Cf": "Californium",
            "Cl": "Chlorine",
            "Cm": "Curium",
            "Cn": "Copernicium",
            "Co": "Cobalt",
            "Cr": "Chromium",
            "Cs": "Cesium",
            "Cu": "Copper",
            "Db": "Dubnium",
            "Ds": "Darmstadtium",
            "Dy": "Dysprosium",
            "Er": "Erbium",
            "Es": "Einsteinium",
            "Eu": "Europium",
            "F": "Fluorine",
            "Fe": "Iron",
            "Fl": "Flerovium",
            "Fm": "Fermium",
            "Fr": "Francium",
            "Ga": "Gallium",
            "Gd": "Gadolinium",
            "Ge": "Germanium",
            "H": "Hydrogen",
            "He": "Helium",
            "Hf": "Hafnium",
            "Hg": "Mercury",
            "Ho": "Holmium",
            "Hs": "Hassium",
            "I": "Iodine",
            "In": "Indium",
            "Ir": "Iridium",
            "K": "Potassium",
            "Kr": "Krypton",
            "La": "Lanthanum",
            "Li": "Lithium",
            "Lr": "Lawrencium",
            "Lu": "Lutetium",
            "Lv": "Livermorium",
            "Mc": "Moscovium",
            "Md": "Mendelevium",
            "Mg": "Magnesium",
            "Mn": "Manganese",
            "Mo": "Molybdenum",
            "Mt": "Meitnerium",
            "N": "Nitrogen",
            "Na": "Sodium",
            "Nb": "Niobium",
            "Nd": "Neodymium",
            "Ne": "Neon",
            "Nh": "Nihonium",
            "Ni": "Nickel",
            "No": "Nobelium",
            "Np": "Neptunium",
            "O": "Oxygen",
            "Og": "Oganesson",
            "Os": "Osmium",
            "P": "Phosphorus",
            "Pa": "Protactinium",
            "Pb": "Lead",
            "Pd": "Palladium",
            "Pm": "Promethium",
            "Po": "Polonium",
            "Pr": "Praseodymium",
            "Pt": "Platinum",
            "Pu": "Plutonium",
            "Ra": "Radium",
            "Rb": "Rubidium",
            "Re": "Rhenium",
            "Rf": "Rutherfordium",
            "Rg": "Roentgenium",
            "Rh": "Rhodium",
            "Rn": "Radon",
            "Ru": "Ruthenium",
            "S": "Sulfur",
            "Sb": "Antimony",
            "Sc": "Scandium",
            "Se": "Selenium",
            "Sg": "Seaborgium",
            "Si": "Silicon",
            "Sm": "Samarium",
            "Sn": "Tin",
            "Sr": "Strontium",
            "Ta": "Tantalum",
            "Tb": "Terbium",
            "Tc": "Technetium",
            "Te": "Tellurium",
            "Th": "Thorium",
            "Ti": "Titanium",
            "Tl": "Thallium",
            "Tm": "Thulium",
            "Ts": "Tennessine",
            "U": "Uranium",
            "V": "Vanadium",
            "W": "Tungsten",
            "Xe": "Xenon",
            "Y": "Yttrium",
            "Yb": "Ytterbium",
            "Zn": "Zinc",
            "Zr": "Zirconium"
        }
        
    def get_element_name(self, e):
        if e in self.elements:
            return self.elements[e]
        return None
