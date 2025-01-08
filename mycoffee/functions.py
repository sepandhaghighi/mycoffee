# -*- coding: utf-8 -*-
"""mycoffee functions."""
import math
from mycoffee.params import MESSAGE_TEMPLATE, METHODS_LIST_TEMPLATE, EMPTY_INFO
from mycoffee.params import MY_COFFEE_VERSION, DEFAULT_PARAMS
from mycoffee.params import METHODS_MAP, COFFEE_UNITS_MAP, WATER_UNITS_MAP
from mycoffee.params import RATIO_WARNING_MESSAGE, GRIND_WARNING_MESSAGE
from art import tprint


def is_int(number):
    """
    Check that input number is int or not.

    :param number: input number
    :type number: float or int
    :return: result as bool
    """
    if int(number) == number:
        return True
    return False


def print_result(params):
    """
    Print result.

    :param params: parameters
    :type params: dict
    :return: None
    """
    method = params["method"]
    tprint("MyCoffee", font="bulbhead")
    print(
        MESSAGE_TEMPLATE.format(
            method,
            params["cups"],
            params["coffee"],
            params["water"],
            params["coffee_ratio"],
            params["water_ratio"],
            params["info"],
            params["coffee_unit"],
            params["water_unit"],
            params["grind"]))
    if not check_ratio_limits(params):
        ratio_lower_limit = METHODS_MAP[method]["ratio_lower_limit"]
        ratio_upper_limit = METHODS_MAP[method]["ratio_upper_limit"]
        print(RATIO_WARNING_MESSAGE.format(method, str(ratio_lower_limit), str(ratio_upper_limit)))
    if not check_grind_limits(params):
        grind_lower_limit = METHODS_MAP[method]["grind_lower_limit"]
        grind_upper_limit = METHODS_MAP[method]["grind_upper_limit"]
        print(GRIND_WARNING_MESSAGE.format(method, str(grind_lower_limit), str(grind_upper_limit)))


def load_method_params(method_name):
    """
    Load method params.

    :param method_name: method name
    :type method_name: str
    :return: method params as dict
    """
    method_params = dict()
    for item in DEFAULT_PARAMS:
        if item in METHODS_MAP[method_name]:
            method_params[item] = METHODS_MAP[method_name][item]
        else:
            method_params[item] = DEFAULT_PARAMS[item]
    return method_params


def show_methods_list():
    """
    Show methods list.

    :return: None
    """
    print("Methods list:\n")
    for i, method in enumerate(sorted(METHODS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                i,
                method,
                METHODS_MAP[method]['info']))


def show_coffee_units_list():
    """
    Show coffee units list.

    :return: None
    """
    print("Coffee units list:\n")
    for i, unit in enumerate(sorted(COFFEE_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                i,
                unit,
                COFFEE_UNITS_MAP[unit]['name']))


def show_water_units_list():
    """
    Show water units list.

    :return: None
    """
    print("Water units list:\n")
    for i, unit in enumerate(sorted(WATER_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                i,
                unit,
                WATER_UNITS_MAP[unit]['name']))


def load_params(args):
    """
    Load params.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: params as dict
    """
    params = load_method_params(args.method)
    for item in params:
        if getattr(args, item) is not None:
            params[item] = getattr(args, item)
    if getattr(args, "water") is not None:
        params["water"] = convert_water(params["water"], params["water_unit"], True)
    params["method"] = args.method
    return params


def filter_params(params):
    """
    Filter params.

    :param params: parameters
    :type params: dict
    :return: filtered parameters as dict
    """
    digits = params["digits"]
    params["coffee"] = round(params["coffee"], digits)
    params["water"] = round(params["water"], digits)
    if is_int(params["coffee"]):
        params["coffee"] = int(params["coffee"])
    if is_int(params["water_ratio"]):
        params["water_ratio"] = int(params["water_ratio"])
    if is_int(params["coffee_ratio"]):
        params["coffee_ratio"] = int(params["coffee_ratio"])
    if is_int(params["water"]):
        params["water"] = int(params["water"])
    if len(params["info"]) == 0:
        params["info"] = EMPTY_INFO
    return params


def check_ratio_limits(params):
    """
    Check ratio limits.

    :param params: parameters
    :type params: dict
    :return: result as bool (False --> the ratio is out of range)
    """
    method = params["method"]
    if "ratio_lower_limit" in METHODS_MAP[method] and "ratio_upper_limit" in METHODS_MAP[method]:
        ratio = params["coffee_ratio"] / params["water_ratio"]
        ratio_lower_limit = METHODS_MAP[method]["ratio_lower_limit"]
        ratio_upper_limit = METHODS_MAP[method]["ratio_upper_limit"]
        if ratio < ratio_lower_limit or ratio > ratio_upper_limit:
            return False
    return True


def check_grind_limits(params):
    """
    Check grind limits.

    :param params: parameters
    :type params: dict
    :return: result as bool (False --> the grind is out of range)
    """
    method = params["method"]
    if "grind_lower_limit" in METHODS_MAP[method] and "grind_upper_limit" in METHODS_MAP[method]:
        grind = params["grind"]
        grind_lower_limit = METHODS_MAP[method]["grind_lower_limit"]
        grind_upper_limit = METHODS_MAP[method]["grind_upper_limit"]
        if grind < grind_lower_limit or grind > grind_upper_limit:
            return False
    return True


def convert_coffee(coffee, unit):
    """
    Convert coffee unit.

    :param coffee: coffee amount
    :type coffee: float
    :param unit: coffee unit
    :type unit: str
    :return: converted coffee amount as float/int
    """
    coffee = coffee * COFFEE_UNITS_MAP[unit]["rate"]
    if unit == "cb":
        coffee = math.ceil(coffee)
    return coffee


def convert_water(water, unit, reverse=False):
    """
    Convert water unit.

    :param water: water amount
    :type water: float
    :param unit: water unit
    :type unit: str
    :param reverse: reverse convert flag
    :type reverse: bool
    :return: converted water amount as float/int
    """
    rate = WATER_UNITS_MAP[unit]["rate"]
    if reverse:
        rate = 1 / rate
    water = water * rate
    return water


def calc_coffee(params):
    """
    Calculate coffee.

    :param params: parameters
    :type params: dict
    :return: coffee amount as float
    """
    coffee = params["cups"] * params["water"] * params["coffee_ratio"] / params["water_ratio"]
    coffee = convert_coffee(coffee, params["coffee_unit"])
    return coffee


def run(args):
    """
    Run program.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: None
    """
    if args.version:
        print(MY_COFFEE_VERSION)
    elif args.methods_list:
        show_methods_list()
    elif args.coffee_units_list:
        show_coffee_units_list()
    elif args.water_units_list:
        show_water_units_list()
    else:
        params = load_params(args)
        params["coffee"] = calc_coffee(params)
        params["water"] = convert_water(params["water"], params["water_unit"])
        params = filter_params(params)
        print_result(params)
