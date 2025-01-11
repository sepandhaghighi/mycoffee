# -*- coding: utf-8 -*-
"""mycoffee params."""
from fractions import Fraction

MY_COFFEE_VERSION = "1.2"
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
RATIO_WARNING_MESSAGE = "[Warning] The ratio is not within the standard range. For `{0}`, the ratio can be anywhere between `{1}` and `{2}`"
GRIND_WARNING_MESSAGE = "[Warning] The grind size is not within the standard range. For `{0}`, the grind size can be anywhere between `{1} um` and `{2} um`"
INPUT_EXAMPLE = "Example: mycoffee --method=v60"
EXIT_MESSAGE = "See you. Bye!"
EMPTY_INFO = "Nothing :)"
MESSAGE_TEMPLATE = """

Method: `{0}`

Cups: {1}

Coffee: {2} {7}

Water: {3} {8}

Ratio: {4}/{5}

Grind: {9} um

Info: {6}
"""

METHODS_LIST_TEMPLATE = "{0}. `{1}` - {2}"


DEFAULT_PARAMS = {
    "cups": 1,
    "water": 0,
    "coffee_ratio": 1,
    "water_ratio": 1,
    "grind": 700,
    "coffee_unit": "g",
    "water_unit": "g",
    "digits": 3,
    "info": ""

}

METHODS_MAP = {
    "custom": {
        "coffee_ratio": 1,
        "water_ratio": 17,
        "grind": 700,
        "water": 240,
        "info": "Custom brewing method"
    },
    "v60": {
        "coffee_ratio": 3,
        "water_ratio": 50,
        "grind": 550,
        "grind_lower_limit": 400,
        "grind_upper_limit": 700,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 250,
        "info": "V60 method"
    },
    "espresso": {
        "coffee_ratio": 1,
        "water_ratio": 2,
        "grind": 280,
        "grind_lower_limit": 180,
        "grind_upper_limit": 380,
        "ratio_lower_limit": Fraction(2, 5),
        "ratio_upper_limit": Fraction(2, 3),
        "water": 36,
        "info": "Espresso method"
    },
    "ristretto": {
        "coffee_ratio": 1,
        "water_ratio": 1,
        "grind": 280,
        "grind_lower_limit": 180,
        "grind_upper_limit": 380,
        "ratio_lower_limit": Fraction(2, 3),
        "ratio_upper_limit": Fraction(1, 1),
        "water": 18,
        "info": "Ristretto method"
    },
    "lungo": {
        "coffee_ratio": 1,
        "water_ratio": 4,
        "grind": 280,
        "grind_lower_limit": 180,
        "grind_upper_limit": 380,
        "ratio_lower_limit": Fraction(1, 4),
        "ratio_upper_limit": Fraction(2, 5),
        "water": 72,
        "info": "Lungo method"
    },
    "chemex": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 670,
        "grind_lower_limit": 410,
        "grind_upper_limit": 930,
        "ratio_lower_limit": Fraction(1, 21),
        "ratio_upper_limit": Fraction(1, 10),
        "water": 240,
        "info": "Chemex method"
    },
    "french-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 995,
        "grind_lower_limit": 690,
        "grind_upper_limit": 1300,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 120,
        "info": "French press method"
    },
    "siphon": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 588,
        "grind_lower_limit": 375,
        "grind_upper_limit": 800,
        "ratio_lower_limit": Fraction(1, 16),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 240,
        "info": "Siphon method"
    },
    "pour-over": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 670,
        "grind_lower_limit": 410,
        "grind_upper_limit": 930,
        "ratio_lower_limit": Fraction(1, 16),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 240,
        "info": "Pour-over method"
    },
    "auto-drip": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "grind": 600,
        "grind_lower_limit": 300,
        "grind_upper_limit": 900,
        "ratio_lower_limit": Fraction(1, 17),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 128,
        "info": "Auto drip method"
    },
    "cold-brew": {
        "coffee_ratio": 1,
        "water_ratio": 11,
        "grind": 1100,
        "grind_lower_limit": 800,
        "grind_upper_limit": 1400,
        "ratio_lower_limit": Fraction(1, 15),
        "ratio_upper_limit": Fraction(1, 8),
        "water": 242,
        "info": "Cold brew method"
    },
    "cold-brew-conc": {
        "coffee_ratio": 1,
        "water_ratio": 5,
        "grind": 1100,
        "grind_lower_limit": 800,
        "grind_upper_limit": 1400,
        "ratio_lower_limit": Fraction(1, 6),
        "ratio_upper_limit": Fraction(1, 4),
        "water": 120,
        "info": "Cold brew concentrate method"
    },
    "moka-pot": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "grind": 510,
        "grind_lower_limit": 360,
        "grind_upper_limit": 660,
        "ratio_lower_limit": Fraction(1, 12),
        "ratio_upper_limit": Fraction(1, 7),
        "water": 60,
        "info": "Moka pot method"
    },
    "turkish": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "grind": 130,
        "grind_lower_limit": 40,
        "grind_upper_limit": 220,
        "ratio_lower_limit": Fraction(1, 12),
        "ratio_upper_limit": Fraction(1, 8),
        "water": 50,
        "info": "Turkish method"
    },
    "cupping": {
        "coffee_ratio": 11,
        "water_ratio": 200,
        "grind": 655,
        "grind_lower_limit": 460,
        "grind_upper_limit": 850,
        "ratio_lower_limit": Fraction(1, 19),
        "ratio_upper_limit": Fraction(1, 17),
        "water": 150,
        "info": "Cupping method"
    },
    "aero-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 640,
        "grind_lower_limit": 320,
        "grind_upper_limit": 960,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 135,
        "info": "AeroPress standard method"
    },
    "aero-press-conc": {
        "coffee_ratio": 1,
        "water_ratio": 6,
        "grind": 640,
        "grind_lower_limit": 320,
        "grind_upper_limit": 960,
        "ratio_lower_limit": Fraction(1, 7),
        "ratio_upper_limit": Fraction(1, 5),
        "water": 90,
        "info": "AeroPress concentrate method"
    },
    "aero-press-inv": {
        "coffee_ratio": 1,
        "water_ratio": 12,
        "grind": 640,
        "grind_lower_limit": 320,
        "grind_upper_limit": 960,
        "ratio_lower_limit": Fraction(1, 14),
        "ratio_upper_limit": Fraction(1, 10),
        "water": 132,
        "info": "AeroPress inverted method"
    },
    "steep-and-release": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "grind": 638,
        "grind_lower_limit": 450,
        "grind_upper_limit": 825,
        "ratio_lower_limit": Fraction(1, 17),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 255,
        "info": "Steep-and-release method"
    }
}

COFFEE_UNITS_MAP = {
    "g": {"name": "gram", "rate": 1},
    "oz": {"name": "ounce", "rate": 0.03527396195},
    "lb": {"name": "pound", "rate": 0.00220462262185},
    "mg": {"name": "milligram", "rate": 1000},
    "kg": {"name": "kilogram", "rate": 0.001},
    "cb": {"name": "coffee bean", "rate": 7.5471698},
    "tbsp": {"name": "tablespoon", "rate": 0.18528},
    "tsp": {"name": "teaspoon", "rate": 0.55585},
    "dsp": {"name": "dessertspoon", "rate": 0.27792},
    "cup": {"name": "cup", "rate": 0.01158},
    "t oz": {"name": "troy ounce", "rate": 0.032151},
    "gr": {"name": "grain", "rate": 15.4324},
    "ct": {"name": "carat", "rate": 5},
    "t lb": {"name": "troy pound", "rate": 0.0026792289},
    "dwt": {"name": "pennyweight", "rate": 0.643015},
}

WATER_UNITS_MAP = {
    "g": {"name": "gram", "rate": 1},
    "ml": {"name": "milliliter", "rate": 1},
    "cc": {"name": "cubic centimeter", "rate": 1},
    "cl": {"name": "centiliter", "rate": 0.1},
    "l": {"name": "liter", "rate": 0.001},
    "oz": {"name": "ounce", "rate": 0.03527396195},
    "lb": {"name": "pound", "rate": 0.00220462262185},
    "mg": {"name": "milligram", "rate": 1000},
    "kg": {"name": "kilogram", "rate": 0.001},
    "tbsp": {"name": "tablespoon", "rate": 0.067628},
    "tsp": {"name": "teaspoon", "rate": 0.20288},
    "dsp": {"name": "dessertspoon", "rate": 0.10144},
    "cup": {"name": "cup", "rate": 0.0042268},
    "pt": {"name": "pint", "rate": 0.00211338},
    "qt": {"name": "quart", "rate": 0.00105669},
    "fl oz": {"name": "fluid ounce", "rate": 0.033814},
    "t oz": {"name": "troy ounce", "rate": 0.032151},
    "gr": {"name": "grain", "rate": 15.4324},
    "ct": {"name": "carat", "rate": 5},
    "t lb": {"name": "troy pound", "rate": 0.0026792289},
    "dwt": {"name": "pennyweight", "rate": 0.643015},
}
