# -*- coding: utf-8 -*-
"""mycoffee params."""

MY_COFFEE_VERSION = "0.3"
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
INPUT_EXAMPLE = "Example: mycoffee --method=v60"
EXIT_MESSAGE = "See you. Bye!"
EMPTY_INFO = "Nothing :)"
MESSAGE_TEMPLATE = """

Method: `{0}`

Cups: {1}

Coffee: {2} gr

Water: {3} gr

Ratio: {4}/{5}

Info: {6}
"""

METHODS_LIST_TEMPLATE = "{0}. `{1}` - {2}"


DEFAULT_PARAMS = {
    "cups": 1,
    "water": 0,
    "coffee_ratio": 1,
    "water_ratio": 1,
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
        "water": 250,
        "info": "V60 method"
    },
    "espresso": {
        "coffee_ratio": 1,
        "water_ratio": 2,
        "water": 36,
        "info": "Espresso method"
    },
    "ristretto": {
        "coffee_ratio": 1,
        "water_ratio": 1,
        "water": 18,
        "info": "Ristretto method"
    },
    "lungo": {
        "coffee_ratio": 1,
        "water_ratio": 4,
        "water": 72,
        "info": "Lungo method"
    },
    "chemex": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "water": 240,
        "info": "Chemex method"
    },
    "french-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "water": 120,
        "info": "French press method"
    },
    "siphon": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "water": 240,
        "info": "Siphon method"
    },
    "pour-over": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "water": 240,
        "info": "Pour-over method"
    },
    "auto-drip": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "water": 128,
        "info": "Auto drip method"
    },
    "cold-brew": {
        "coffee_ratio": 1,
        "water_ratio": 11,
        "water": 242,
        "info": "Cold brew method"
    },
    "cold-brew-conc": {
        "coffee_ratio": 1,
        "water_ratio": 5,
        "water": 120,
        "info": "Cold brew concentrate method"
    },
    "moka-pot": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "water": 60,
        "info": "Moka pot method"
    },
    "turkish": {
        "coffee_ratio": 1,
        "water_ratio": 10,
        "water": 50,
        "info": "Turkish method"
    },
    "cupping": {
        "coffee_ratio": 11,
        "water_ratio": 200,
        "water": 150,
        "info": "Cupping method"
    },
    "aero-press": {
        "coffee_ratio": 1,
        "water_ratio": 15,
        "water": 135,
        "info": "AeroPress standard method"
    },
    "aero-press-conc": {
        "coffee_ratio": 1,
        "water_ratio": 6,
        "water": 90,
        "info": "AeroPress concentrate method"
    },
    "aero-press-inv": {
        "coffee_ratio": 1,
        "water_ratio": 12,
        "water": 132,
        "info": "AeroPress inverted method"
    },
    "steep-and-release": {
        "coffee_ratio": 1,
        "water_ratio": 16,
        "water": 255,
        "info": "Steep-and-release method"
    }
}
