# -*- coding: utf-8 -*-
"""mycoffee functions."""
import math
import argparse
from mycoffee.params import MESSAGE_TEMPLATE, METHODS_LIST_TEMPLATE, EMPTY_MESSAGE
from mycoffee.params import MY_COFFEE_VERSION, DEFAULT_PARAMS
from mycoffee.params import METHODS_MAP, COFFEE_UNITS_MAP, WATER_UNITS_MAP, TEMPERATURE_UNITS_MAP
from mycoffee.params import RATIO_WARNING_MESSAGE, GRIND_WARNING_MESSAGE, TEMPERATURE_WARNING_MESSAGE
from mycoffee.params import POSITIVE_INTEGER_ERROR_MESSAGE, POSITIVE_FLOAT_ERROR_MESSAGE
from mycoffee.params import MY_COFFEE_OVERVIEW, MY_COFFEE_REPO
from art import tprint


def mycoffee_info():  # pragma: no cover
    """
    Print mycoffee details.

    :return: None
    """
    tprint("MyCoffee")
    tprint("V:" + MY_COFFEE_VERSION)
    print(MY_COFFEE_OVERVIEW)
    print(MY_COFFEE_REPO)


def validate_positive_int(string):
    """
    Validate that the input string is a positive integer.

    :param string: input string
    :type string: str
    :return: the validated positive integer or raise argparse.ArgumentTypeError
    """
    try:
        number = int(string)
        if number <= 0:
            raise Exception
        return number
    except Exception:
        raise argparse.ArgumentTypeError(POSITIVE_INTEGER_ERROR_MESSAGE.format(string=string))


def validate_positive_float(string):
    """
    Validate that the input string is a positive float.

    :param string: input string
    :type string: str
    :return: the validated positive float or raise argparse.ArgumentTypeError
    """
    try:
        number = float(string)
        if number <= 0:
            raise Exception
        return number
    except Exception:
        raise argparse.ArgumentTypeError(POSITIVE_FLOAT_ERROR_MESSAGE.format(string=string))


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
    grind_type = get_grind_type(params["grind"])
    print(
        MESSAGE_TEMPLATE.format(
            method=method,
            cups=params["cups"],
            coffee=params["coffee"],
            water=params["water"],
            coffee_ratio=params["coffee_ratio"],
            water_ratio=params["water_ratio"],
            message=params["message"],
            coffee_unit=params["coffee_unit"],
            water_unit=params["water_unit"],
            grind_size=params["grind"],
            temperature=params["temperature"],
            temperature_unit=params["temperature_unit"],
            grind_type=grind_type))


def print_warnings(params):
    """
    Print warnings.

    :param params: parameters
    :type params: dict
    :return: None
    """
    method = params["method"]
    if not check_ratio_limits(params):
        ratio_lower_limit = METHODS_MAP[method]["ratio_lower_limit"]
        ratio_upper_limit = METHODS_MAP[method]["ratio_upper_limit"]
        print(
            RATIO_WARNING_MESSAGE.format(
                method=method,
                lower_limit=str(ratio_lower_limit),
                upper_limit=str(ratio_upper_limit)))
    if not check_grind_limits(params):
        grind_lower_limit = METHODS_MAP[method]["grind_lower_limit"]
        grind_upper_limit = METHODS_MAP[method]["grind_upper_limit"]
        print(
            GRIND_WARNING_MESSAGE.format(
                method=method,
                lower_limit=str(grind_lower_limit),
                upper_limit=str(grind_upper_limit)))
    if not check_temperature_limits(params):
        temperature_lower_limit = convert_temperature(
            METHODS_MAP[method]["temperature_lower_limit"],
            from_unit="C",
            to_unit=params["temperature_unit"],
            digits=params["digits"])
        temperature_upper_limit = convert_temperature(
            METHODS_MAP[method]["temperature_upper_limit"],
            from_unit="C",
            to_unit=params["temperature_unit"],
            digits=params["digits"])
        print(
            TEMPERATURE_WARNING_MESSAGE.format(
                method=method,
                lower_limit=str(temperature_lower_limit),
                upper_limit=str(temperature_upper_limit),
                unit=params["temperature_unit"]))


def get_grind_type(grind):
    """
    Return grind type.

    :param grind: grind size
    :type grind: int
    :return: grind type as str
    """
    if grind <= 200:
        return "Extra-Fine"
    elif grind <= 400:
        return "Fine"
    elif grind <= 600:
        return "Medium-Fine"
    elif grind <= 800:
        return "Medium"
    elif grind <= 1000:
        return "Medium-Coarse"
    elif grind <= 1200:
        return "Coarse"
    return "Extra-Coarse"


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
                index=i,
                item=method,
                data=METHODS_MAP[method]['message']))


def show_coffee_units_list():
    """
    Show coffee units list.

    :return: None
    """
    print("Coffee units list:\n")
    for i, unit in enumerate(sorted(COFFEE_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=unit,
                data=COFFEE_UNITS_MAP[unit]['name']))


def show_water_units_list():
    """
    Show water units list.

    :return: None
    """
    print("Water units list:\n")
    for i, unit in enumerate(sorted(WATER_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=unit,
                data=WATER_UNITS_MAP[unit]['name']))


def show_temperature_units_list():
    """
    Show temperature units list.

    :return: None
    """
    print("Temperature units list:\n")
    for i, unit in enumerate(sorted(TEMPERATURE_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=unit,
                data=TEMPERATURE_UNITS_MAP[unit]['name']))


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
    if is_int(params["temperature"]):
        params["temperature"] = int(params["temperature"])
    if len(params["message"]) == 0:
        params["message"] = EMPTY_MESSAGE
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
        ratio_lower_limit = float(METHODS_MAP[method]["ratio_lower_limit"])
        ratio_upper_limit = float(METHODS_MAP[method]["ratio_upper_limit"])
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


def convert_temperature(value, from_unit, to_unit, digits=3):
    """
    Convert temperature.

    :param value: temperature value to convert
    :type value: float
    :param from_unit: unit of the input value
    :type from_unit: str
    :param to_unit: unit to convert to
    :type to_unit: str
    :param digits: number of digits up to which the result is rounded
    :type digits: int
    :return: converted temperature value
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    result = value
    if from_unit != to_unit:
        if from_unit == 'F':
            celsius = (value - 32) * 5 / 9
        elif from_unit == 'K':
            celsius = value - 273.15
        else:
            celsius = value

        if to_unit == 'F':
            result = (celsius * 9 / 5) + 32
        elif to_unit == 'K':
            result = celsius + 273.15
        else:
            result = celsius
    result = round(result, digits)
    if is_int(result):
        result = int(result)
    return result


def check_temperature_limits(params):
    """
    Check temperature limits.

    :param params: parameters
    :type params: dict
    :return: result as bool (False --> the temperature is out of range)
    """
    method = params["method"]
    if "temperature_lower_limit" in METHODS_MAP[method] and "temperature_upper_limit" in METHODS_MAP[method]:
        temperature = convert_temperature(params["temperature"], from_unit=params["temperature_unit"], to_unit="C")
        temperature_lower_limit = METHODS_MAP[method]["temperature_lower_limit"]
        temperature_upper_limit = METHODS_MAP[method]["temperature_upper_limit"]
        if temperature < temperature_lower_limit or temperature > temperature_upper_limit:
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
    elif args.info:  # pragma: no cover
        mycoffee_info()
    elif args.methods_list:
        show_methods_list()
    elif args.coffee_units_list:
        show_coffee_units_list()
    elif args.water_units_list:
        show_water_units_list()
    elif args.temperature_units_list:
        show_temperature_units_list()
    else:
        params = load_params(args)
        params["coffee"] = calc_coffee(params)
        params["water"] = convert_water(params["water"], params["water_unit"])
        params = filter_params(params)
        print_result(params)
        if not args.ignore_warnings:
            print_warnings(params)
