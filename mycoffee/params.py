# -*- coding: utf-8 -*-
"""mycoffee params."""

MY_COFFEE_VERSION = "0.1"
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
INPUT_EXAMPLE = "Example: mycoffee --method=v60 "
MESSAGE_TEMPLATE = """
Method: {0}

Cups: {1}

Coffee: {2} gr

Water: {3} ml

Ratio: {4}/{5}
"""

METHODS_LIST_TEMPLATE = "{0}. `{1}` - {2}"


DEFAULT_PARAMS = {
    "cups": 1,
    "water": 0,
    "coffee_ratio": 1,
    "water_ratio": 1,
    "message": ""

}

METHODS_MAP = {
    "v60": {
        "coffee_ratio": 3,
        "water_ratio": 50,
        "water": 242,
        "message": "V60 method"
    }
}
