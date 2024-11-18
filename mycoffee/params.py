# -*- coding: utf-8 -*-
"""mycoffee params."""
from fractions import Fraction

MY_COFFEE_VERSION = "0.7"
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
RATIO_WARNING_MESSAGE = "[Warning] The ratio is not within the standard range. For `{0}`, the ratio can be anywhere between `{1}` and `{2}`"
INPUT_EXAMPLE = "Example: mycoffee --method=v60"
EXIT_MESSAGE = "See you. Bye!"
EMPTY_INFO = "Nothing :)"
MESSAGE_TEMPLATE = """

Method: `{0}`

Cups: {1}

Coffee: {2} {7}

Water: {3} g

Ratio: {4}/{5}

Info: {6}
"""

METHODS_LIST_TEMPLATE = "{0}. `{1}` - {2}"


DEFAULT_PARAMS = {
    "cups": 1,
    "water": 0,
    "coffee_ratio": 1,
    "water_ratio": 1,
    "coffee_unit": "g",
    "digits": 3,
    "info": ""

}

METHODS_MAP = {
    "custom": {
        "coffee_ratio": 1,
        "water_ratio": 17,
        "water": 240,
        "info": "Custom brewing method"
    },
    "v60": {
        "coffee_ratio": 3,
        "water_ratio": 50,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 250,
        "info": "V60 method"
    },
    "espresso": {
        "coffee_ratio": 1,
        "water_ratio": 2,
        "ratio_lower_limit": Fraction(2, 5),
        "ratio_upper_limit": Fraction(2, 3),
        "water": 36,
        "info": "Espresso method"
    },
    "ristretto": {
        "coffee_ratio": 1,
        "water_ratio": 1,
        "ratio_lower_limit": Fraction(2, 3),
        "ratio_upper_limit": Fraction(1, 1),
        "water": 18,
        "info": "Ristretto method"
    },
    "lungo": {
        "coffee_ratio": 1,
        "water_ratio": 4,
        "ratio_lower_limit": Fraction(1, 4),
        "ratio_upper_limit": Fraction(2, 5),
        "water": 72,
        "info": "Lungo method"
    },
    "chemex": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "ratio_lower_limit": Fraction(1, 21),
        "ratio_upper_limit": Fraction(1, 10),
        "water": 240,
        "info": "Chemex method"
    },
    "french-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 120,
        "info": "French press method"
    },
    "siphon": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "ratio_lower_limit": Fraction(1, 16),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 240,
        "info": "Siphon method"
    },
    "pour-over": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "ratio_lower_limit": Fraction(1, 16),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 240,
        "info": "Pour-over method"
    },
    "auto-drip": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "ratio_lower_limit": Fraction(1, 17),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 128,
        "info": "Auto drip method"
    },
    "cold-brew": {
        "coffee_ratio": 1,
        "water_ratio": 11,
        "ratio_lower_limit": Fraction(1, 15),
        "ratio_upper_limit": Fraction(1, 8),
        "water": 242,
        "info": "Cold brew method"
    },
    "cold-brew-conc": {
        "coffee_ratio": 1,
        "water_ratio": 5,
        "ratio_lower_limit": Fraction(1, 6),
        "ratio_upper_limit": Fraction(1, 4),
        "water": 120,
        "info": "Cold brew concentrate method"
    },
    "moka-pot": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "ratio_lower_limit": Fraction(1, 12),
        "ratio_upper_limit": Fraction(1, 7),
        "water": 60,
        "info": "Moka pot method"
    },
    "turkish": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "ratio_lower_limit": Fraction(1, 12),
        "ratio_upper_limit": Fraction(1, 8),
        "water": 50,
        "info": "Turkish method"
    },
    "cupping": {
        "coffee_ratio": 11,
        "water_ratio": 200,
        "ratio_lower_limit": Fraction(1, 19),
        "ratio_upper_limit": Fraction(1, 17),
        "water": 150,
        "info": "Cupping method"
    },
    "aero-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 135,
        "info": "AeroPress standard method"
    },
    "aero-press-conc": {
        "coffee_ratio": 1,
        "water_ratio": 6,
        "ratio_lower_limit": Fraction(1, 7),
        "ratio_upper_limit": Fraction(1, 5),
        "water": 90,
        "info": "AeroPress concentrate method"
    },
    "aero-press-inv": {
        "coffee_ratio": 1,
        "water_ratio": 12,
        "ratio_lower_limit": Fraction(1, 14),
        "ratio_upper_limit": Fraction(1, 10),
        "water": 132,
        "info": "AeroPress inverted method"
    },
    "steep-and-release": {
        "coffee_ratio": 1,
        "water_ratio": 16,
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
    "cb": {"name": "coffee beans", "rate": 7.5471698},
    "tbsp": {"name": "tablespoon", "rate": 0.18528},
    "tsp": {"name": "teaspoon", "rate": 0.55585},
    "dsp": {"name": "dessertspoon", "rate": 0.27792},
}
