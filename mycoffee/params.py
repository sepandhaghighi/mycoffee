# -*- coding: utf-8 -*-
"""mycoffee params."""
from fractions import Fraction

MY_COFFEE_VERSION = "1.8"
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
POSITIVE_INTEGER_ERROR_MESSAGE = "invalid positive int value: '{string}'"
POSITIVE_FLOAT_ERROR_MESSAGE = "invalid positive float value: '{string}'"
RATIO_WARNING_MESSAGE = "The ratio is not within the recommended range. For `{method}`, the ratio can be anywhere between `{lower_limit}` and `{upper_limit}`"
GRIND_WARNING_MESSAGE = "The grind size is not within the recommended range. For `{method}`, the grind size can be anywhere between `{lower_limit} um` and `{upper_limit} um`"
TEMPERATURE_WARNING_MESSAGE = "The temperature is not within the recommended range. For `{method}`, the temperature can be anywhere between `{lower_limit} {unit}` and `{upper_limit} {unit}`"
SAVE_FILE_ERROR_MESSAGE = "[Error] Failed to save file!"
SAVE_FILE_SUCCESS_MESSAGE = "[Info] File saved successfully!"
INPUT_EXAMPLE = "Example: mycoffee --method=v60"
EXIT_MESSAGE = "See you. Bye!"
EMPTY_MESSAGE = "Nothing :)"
MY_COFFEE_REPO = "https://github.com/sepandhaghighi/mycoffee"
MY_COFFEE_OVERVIEW = '''
MyCoffee is a command-line tool for coffee enthusiasts who love brewing with precision.
It helps you calculate the perfect coffee-to-water ratio for various brewing methods,
ensuring you brew your ideal cup every time-right from your terminal.
'''
MESSAGE_TEMPLATE = """

Method: `{method}`

Cups: {cups}

Coffee:

    - Cup:   {coffee[cup]} {coffee[unit]}
    - Total: {coffee[total]} {coffee[unit]}

Water:

    - Cup: {water[cup]} {water[unit]}
    - Total: {water[total]} {water[unit]}

Ratio: {coffee[ratio]}/{water[ratio]} ({ratio})

Strength: {strength}

Grind: {grind[value]} {grind[unit]} ({grind[type]})

Temperature: {temperature[value]} {temperature[unit]}

Message: {message}
"""

METHODS_LIST_TEMPLATE = "{index}. `{item}` - {data}"


DEFAULT_PARAMS = {
    "cups": 1,
    "water": 0,
    "coffee_ratio": 1,
    "water_ratio": 1,
    "grind": 700,
    "temperature": 90,
    "coffee_unit": "g",
    "water_unit": "g",
    "temperature_unit": "C",
    "digits": 3,
    "message": ""

}

METHODS_MAP = {
    "custom": {
        "coffee_ratio": 1,
        "water_ratio": 17,
        "grind": 700,
        "temperature": 90,
        "water": 240,
        "message": "Custom brewing method"
    },
    "v60": {
        "coffee_ratio": 3,
        "water_ratio": 50,
        "grind": 550,
        "temperature": 91,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 400,
        "grind_upper_limit": 700,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 250,
        "message": "V60 method"
    },
    "espresso": {
        "coffee_ratio": 1,
        "water_ratio": 2,
        "grind": 280,
        "temperature": 92,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 180,
        "grind_upper_limit": 380,
        "ratio_lower_limit": Fraction(2, 5),
        "ratio_upper_limit": Fraction(2, 3),
        "water": 36,
        "message": "Espresso method"
    },
    "ristretto": {
        "coffee_ratio": 1,
        "water_ratio": 1,
        "grind": 280,
        "temperature": 92,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 180,
        "grind_upper_limit": 380,
        "ratio_lower_limit": Fraction(2, 3),
        "ratio_upper_limit": Fraction(1, 1),
        "water": 18,
        "message": "Ristretto method"
    },
    "lungo": {
        "coffee_ratio": 1,
        "water_ratio": 4,
        "grind": 280,
        "temperature": 92,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 180,
        "grind_upper_limit": 380,
        "ratio_lower_limit": Fraction(1, 4),
        "ratio_upper_limit": Fraction(2, 5),
        "water": 72,
        "message": "Lungo method"
    },
    "chemex": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 670,
        "temperature": 94,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 410,
        "grind_upper_limit": 930,
        "ratio_lower_limit": Fraction(1, 21),
        "ratio_upper_limit": Fraction(1, 10),
        "water": 240,
        "message": "Chemex method"
    },
    "french-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 995,
        "temperature": 90,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 690,
        "grind_upper_limit": 1300,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 120,
        "message": "French press method"
    },
    "siphon": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 588,
        "temperature": 93,
        "temperature_lower_limit": 91,
        "temperature_upper_limit": 94,
        "grind_lower_limit": 375,
        "grind_upper_limit": 800,
        "ratio_lower_limit": Fraction(1, 16),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 240,
        "message": "Siphon method"
    },
    "pour-over": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 670,
        "temperature": 92,
        "temperature_lower_limit": 90,
        "temperature_upper_limit": 93,
        "grind_lower_limit": 410,
        "grind_upper_limit": 930,
        "ratio_lower_limit": Fraction(1, 16),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 240,
        "message": "Pour-over method"
    },
    "auto-drip": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "grind": 600,
        "temperature": 93,
        "temperature_lower_limit": 90,
        "temperature_upper_limit": 96,
        "grind_lower_limit": 300,
        "grind_upper_limit": 900,
        "ratio_lower_limit": Fraction(1, 17),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 128,
        "message": "Auto drip method"
    },
    "cold-brew": {
        "coffee_ratio": 1,
        "water_ratio": 11,
        "grind": 1100,
        "temperature": 20,
        "temperature_lower_limit": 0,
        "temperature_upper_limit": 40,
        "grind_lower_limit": 800,
        "grind_upper_limit": 1400,
        "ratio_lower_limit": Fraction(1, 15),
        "ratio_upper_limit": Fraction(1, 8),
        "water": 242,
        "message": "Cold brew method"
    },
    "cold-brew-conc": {
        "coffee_ratio": 1,
        "water_ratio": 5,
        "grind": 1100,
        "temperature": 20,
        "temperature_lower_limit": 0,
        "temperature_upper_limit": 40,
        "grind_lower_limit": 800,
        "grind_upper_limit": 1400,
        "ratio_lower_limit": Fraction(1, 6),
        "ratio_upper_limit": Fraction(1, 4),
        "water": 120,
        "message": "Cold brew concentrate method"
    },
    "moka-pot": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "grind": 510,
        "temperature": 93,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 360,
        "grind_upper_limit": 660,
        "ratio_lower_limit": Fraction(1, 12),
        "ratio_upper_limit": Fraction(1, 7),
        "water": 60,
        "message": "Moka pot method"
    },
    "turkish": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "grind": 130,
        "temperature": 90,
        "temperature_lower_limit": 90,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 40,
        "grind_upper_limit": 220,
        "ratio_lower_limit": Fraction(1, 12),
        "ratio_upper_limit": Fraction(1, 8),
        "water": 50,
        "message": "Turkish method"
    },
    "cupping": {
        "coffee_ratio": 11,
        "water_ratio": 200,
        "grind": 655,
        "temperature": 93,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 460,
        "grind_upper_limit": 850,
        "ratio_lower_limit": Fraction(1, 19),
        "ratio_upper_limit": Fraction(1, 17),
        "water": 150,
        "message": "Cupping method"
    },
    "aero-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "grind": 640,
        "temperature": 93,
        "temperature_lower_limit": 90,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 320,
        "grind_upper_limit": 960,
        "ratio_lower_limit": Fraction(1, 18),
        "ratio_upper_limit": Fraction(1, 12),
        "water": 135,
        "message": "AeroPress standard method"
    },
    "aero-press-conc": {
        "coffee_ratio": 1,
        "water_ratio": 6,
        "grind": 640,
        "temperature": 93,
        "temperature_lower_limit": 90,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 320,
        "grind_upper_limit": 960,
        "ratio_lower_limit": Fraction(1, 7),
        "ratio_upper_limit": Fraction(1, 5),
        "water": 90,
        "message": "AeroPress concentrate method"
    },
    "aero-press-inv": {
        "coffee_ratio": 1,
        "water_ratio": 12,
        "grind": 640,
        "temperature": 93,
        "temperature_lower_limit": 90,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 320,
        "grind_upper_limit": 960,
        "ratio_lower_limit": Fraction(1, 14),
        "ratio_upper_limit": Fraction(1, 10),
        "water": 132,
        "message": "AeroPress inverted method"
    },
    "steep-and-release": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "grind": 638,
        "temperature": 93,
        "temperature_lower_limit": 85,
        "temperature_upper_limit": 95,
        "grind_lower_limit": 450,
        "grind_upper_limit": 825,
        "ratio_lower_limit": Fraction(1, 17),
        "ratio_upper_limit": Fraction(1, 14),
        "water": 255,
        "message": "Steep-and-release method"
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

TEMPERATURE_UNITS_MAP = {
    "C": {"name": "Celsius"},
    "F": {"name": "Fahrenheit"},
    "K": {"name": "Kelvin"}
}

FILE_FORMATS_LIST = ["text", "json"]
