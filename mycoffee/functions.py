# -*- coding: utf-8 -*-
"""mycoffee functions."""
from typing import Union, Dict, List
import json
import math
import argparse
from mycoffee.params import MESSAGE_TEMPLATE, METHODS_LIST_TEMPLATE, EMPTY_MESSAGE
from mycoffee.params import MY_COFFEE_VERSION, DEFAULT_PARAMS
from mycoffee.params import METHODS_MAP, COFFEE_UNITS_MAP, WATER_UNITS_MAP, TEMPERATURE_UNITS_MAP
from mycoffee.params import RATIO_WARNING_MESSAGE, GRIND_WARNING_MESSAGE, TEMPERATURE_WARNING_MESSAGE
from mycoffee.params import POSITIVE_INTEGER_ERROR_MESSAGE, POSITIVE_FLOAT_ERROR_MESSAGE
from mycoffee.params import MY_COFFEE_OVERVIEW, MY_COFFEE_REPO
from mycoffee.params import SAVE_FILE_ERROR_MESSAGE, SAVE_FILE_SUCCESS_MESSAGE
from art import tprint


def mycoffee_info() -> None:  # pragma: no cover
    """Print mycoffee details."""
    tprint("MyCoffee")
    tprint("V:" + MY_COFFEE_VERSION)
    print(MY_COFFEE_OVERVIEW)
    print(MY_COFFEE_REPO)


def validate_positive_int(string: str) -> int:
    """
    Validate and return a positive integer or raise argparse.ArgumentTypeError.

    :param string: input string
    """
    try:
        number = int(string)
        if number <= 0:
            raise Exception
        return number
    except Exception:
        raise argparse.ArgumentTypeError(POSITIVE_INTEGER_ERROR_MESSAGE.format(string=string))


def validate_positive_float(string: str) -> float:
    """
    Validate and return a positive float or raise argparse.ArgumentTypeError.

    :param string: input string
    """
    try:
        number = float(string)
        if number <= 0:
            raise Exception
        return number
    except Exception:
        raise argparse.ArgumentTypeError(POSITIVE_FLOAT_ERROR_MESSAGE.format(string=string))


def is_int(number: Union[int, float]) -> bool:
    """
    Check that input number is int or not.

    :param number: input number
    """
    if int(number) == number:
        return True
    return False


def format_result(params: Dict[str, Union[str, int, float]]) -> str:
    """
    Format result.

    :param params: parameters
    """
    result = MESSAGE_TEMPLATE.format(
        method=params["method"],
        cups=params["cups"],
        coffee=params["coffee"],
        water=params["water"],
        coffee_ratio=params["coffee_ratio"],
        water_ratio=params["water_ratio"],
        ratio=params["ratio"],
        message=params["message"],
        coffee_unit=params["coffee_unit"],
        water_unit=params["water_unit"],
        grind_size=params["grind"],
        temperature=params["temperature"],
        temperature_unit=params["temperature_unit"],
        grind_unit=params["grind_unit"],
        grind_type=params["grind_type"],
        strength=params["strength"])
    return result


def print_result(params: Dict[str, Union[str, int, float]], ignore_warnings: bool = False) -> None:
    """
    Print result.

    :param params: parameters
    :param ignore_warnings: ignore warnings flag
    """
    tprint("MyCoffee", font="bulbhead")
    print(format_result(params))
    if not ignore_warnings:
        warnings_list = params["warnings"]
        if len(warnings_list) > 0:
            print("\n".join(warnings_list))


def save_result(
        params: Dict[str, Union[str, int, float]],
        file_path: str,
        file_format: str = "text",
        ignore_warnings: bool = False) -> Dict[str, Union[bool, str]]:
    """
    Save result.

    :param params: parameters
    :param file_path: file path
    :param file_format: file format
    :param ignore_warnings: ignore warnings flag
    """
    details = {"status": True, "message": SAVE_FILE_SUCCESS_MESSAGE}
    try:
        if file_format == "json":
            save_result_json(params, file_path, ignore_warnings)
        else:
            save_result_text(params, file_path, ignore_warnings)
    except Exception as e:
        details["status"] = False
        details["message"] = str(e)
    return details


def save_result_text(params: Dict[str, Union[str, int, float]], file_path: str, ignore_warnings: bool = False) -> None:
    """
    Save result as a text file.

    :param params: parameters
    :param file_path: file path
    :param ignore_warnings: ignore warnings flag
    """
    result = format_result(params).strip()
    if not ignore_warnings:
        warnings_list = params["warnings"]
        if len(warnings_list) > 0:
            result = result + "\n\n" + "\n".join(warnings_list)
    with open(file_path, "w") as file:
        file.write(result)


def save_result_json(params: Dict[str, Union[str, int, float]], file_path: str, ignore_warnings: bool = False) -> None:
    """
    Save result as a JSON file.

    :param params: parameters
    :param file_path: file path
    :param ignore_warnings: ignore warnings flag
    """
    result = params.copy()
    result["mycoffee_version"] = MY_COFFEE_VERSION
    if ignore_warnings:
        result["warnings"] = []
    with open(file_path, "w") as file:
        json.dump(result, file)


def get_warnings(params: Dict[str, Union[str, int, float]]) -> List[str]:
    """
    Get warnings as a list.

    :param params: parameters
    """
    warnings_list = []
    method = params["method"]
    if not check_ratio_limits(params):
        ratio_lower_limit = METHODS_MAP[method]["ratio_lower_limit"]
        ratio_upper_limit = METHODS_MAP[method]["ratio_upper_limit"]
        warnings_list.append(
            RATIO_WARNING_MESSAGE.format(
                method=method,
                lower_limit=str(ratio_lower_limit),
                upper_limit=str(ratio_upper_limit)))
    if not check_grind_limits(params):
        grind_lower_limit = METHODS_MAP[method]["grind_lower_limit"]
        grind_upper_limit = METHODS_MAP[method]["grind_upper_limit"]
        warnings_list.append(
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
        warnings_list.append(
            TEMPERATURE_WARNING_MESSAGE.format(
                method=method,
                lower_limit=str(temperature_lower_limit),
                upper_limit=str(temperature_upper_limit),
                unit=params["temperature_unit"]))
    return warnings_list


def get_grind_type(grind: int) -> str:
    """
    Return grind type.

    :param grind: grind size
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


def get_brew_strength(ratio: float) -> str:
    """
    Return brew strength.

    :param ratio: coffee to water ratio
    """
    strength_labels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    thresholds = [1 / 40, 1 / 22, 1 / 15, 1 / 12, 1 / 8]

    if ratio < thresholds[0]:
        return strength_labels[0]
    elif ratio < thresholds[1]:
        return strength_labels[1]
    elif ratio < thresholds[2]:
        return strength_labels[2]
    elif ratio < thresholds[3]:
        return strength_labels[3]
    else:
        return strength_labels[4]


def load_method_params(method_name: str) -> Dict[str, Union[str, int, float]]:
    """
    Load method params.

    :param method_name: method name
    """
    method_params = dict()
    for item in DEFAULT_PARAMS:
        if item in METHODS_MAP[method_name]:
            method_params[item] = METHODS_MAP[method_name][item]
        else:
            method_params[item] = DEFAULT_PARAMS[item]
    return method_params


def show_methods_list() -> None:
    """Show methods list."""
    print("Methods list:\n")
    for i, method in enumerate(sorted(METHODS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=method,
                data=METHODS_MAP[method]['message']))


def show_coffee_units_list() -> None:
    """Show coffee units list."""
    print("Coffee units list:\n")
    for i, unit in enumerate(sorted(COFFEE_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=unit,
                data=COFFEE_UNITS_MAP[unit]['name']))


def show_water_units_list() -> None:
    """Show water units list."""
    print("Water units list:\n")
    for i, unit in enumerate(sorted(WATER_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=unit,
                data=WATER_UNITS_MAP[unit]['name']))


def show_temperature_units_list() -> None:
    """Show temperature units list."""
    print("Temperature units list:\n")
    for i, unit in enumerate(sorted(TEMPERATURE_UNITS_MAP), 1):
        print(
            METHODS_LIST_TEMPLATE.format(
                index=i,
                item=unit,
                data=TEMPERATURE_UNITS_MAP[unit]['name']))


def load_params(args: argparse.Namespace) -> Dict[str, Union[str, int, float]]:
    """
    Load params as a dictionary.

    :param args: input arguments
    """
    params = load_method_params(args.method)
    for item in params:
        if getattr(args, item) is not None:
            params[item] = getattr(args, item)
    if getattr(args, "water") is None:
        params["water"] = convert_water(params["water"], params["water_unit"])
    if getattr(args, "temperature") is None:
        params["temperature"] = convert_temperature(
            params["temperature"],
            from_unit="C",
            to_unit=params["temperature_unit"],
            digits=params["digits"])
    params["method"] = args.method
    return params


def filter_params(params: Dict[str, Union[str, int, float]]) -> Dict[str, Union[str, int, float]]:
    """
    Filter params.

    :param params: parameters
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


def check_ratio_limits(params: Dict[str, Union[str, int, float]]) -> bool:
    """
    Return True if the ratio is within limits, otherwise False.

    :param params: parameters
    """
    method = params["method"]
    if "ratio_lower_limit" in METHODS_MAP[method] and "ratio_upper_limit" in METHODS_MAP[method]:
        ratio = params["coffee_ratio"] / params["water_ratio"]
        ratio_lower_limit = float(METHODS_MAP[method]["ratio_lower_limit"])
        ratio_upper_limit = float(METHODS_MAP[method]["ratio_upper_limit"])
        if ratio < ratio_lower_limit or ratio > ratio_upper_limit:
            return False
    return True


def check_grind_limits(params: Dict[str, Union[str, int, float]]) -> bool:
    """
    Return True if the grind is within limits, otherwise False.

    :param params: parameters
    """
    method = params["method"]
    if "grind_lower_limit" in METHODS_MAP[method] and "grind_upper_limit" in METHODS_MAP[method]:
        grind = params["grind"]
        grind_lower_limit = METHODS_MAP[method]["grind_lower_limit"]
        grind_upper_limit = METHODS_MAP[method]["grind_upper_limit"]
        if grind < grind_lower_limit or grind > grind_upper_limit:
            return False
    return True


def convert_temperature(value: float, from_unit: str, to_unit: str, digits: int = 3) -> float:
    """
    Convert temperature.

    :param value: temperature value to convert
    :param from_unit: unit of the input value
    :param to_unit: unit to convert to
    :param digits: number of digits up to which the result is rounded
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


def check_temperature_limits(params: Dict[str, Union[str, int, float]]) -> bool:
    """
    Return True if the temperature is within limits, otherwise False.

    :param params: parameters
    """
    method = params["method"]
    if "temperature_lower_limit" in METHODS_MAP[method] and "temperature_upper_limit" in METHODS_MAP[method]:
        temperature = convert_temperature(params["temperature"], from_unit=params["temperature_unit"], to_unit="C")
        temperature_lower_limit = METHODS_MAP[method]["temperature_lower_limit"]
        temperature_upper_limit = METHODS_MAP[method]["temperature_upper_limit"]
        if temperature < temperature_lower_limit or temperature > temperature_upper_limit:
            return False
    return True


def convert_coffee(coffee: float, unit: str) -> Union[float, int]:
    """
    Convert and return the coffee amount as a float or int.

    :param coffee: coffee amount
    :param unit: coffee unit
    """
    coffee = coffee * COFFEE_UNITS_MAP[unit]["rate"]
    if unit == "cb":
        coffee = math.ceil(coffee)
    return coffee


def convert_water(water: float, unit: str, reverse: bool = False) -> Union[float, int]:
    """
    Convert and return the water amount as a float or int.

    :param water: water amount
    :param unit: water unit
    :param reverse: reverse convert flag
    """
    rate = WATER_UNITS_MAP[unit]["rate"]
    if reverse:
        rate = 1 / rate
    water = water * rate
    return water


def calc_coffee(params: Dict[str, Union[str, int, float]]) -> float:
    """
    Calculate coffee.

    :param params: parameters
    """
    water_gram = convert_water(params["water"], params["water_unit"], True)
    coffee_gram = params["cups"] * water_gram * params["coffee_ratio"] / params["water_ratio"]
    coffee = convert_coffee(coffee_gram, params["coffee_unit"])
    return coffee


def get_result(params: Dict[str, Union[str, int, float]]) -> Dict[str, Union[str, int, float]]:
    """
    Get result.

    :param params: parameters
    """
    params_copy = params.copy()
    params_copy["coffee"] = calc_coffee(params_copy)
    params_copy["grind_type"] = get_grind_type(params_copy["grind"])
    params_copy["ratio"] = round(params_copy["coffee_ratio"] / params_copy["water_ratio"], params["digits"])
    params_copy["strength"] = get_brew_strength(ratio=params_copy["ratio"])
    params_copy["grind_unit"] = "um"
    result = filter_params(params_copy)
    result["warnings"] = get_warnings(result)
    return result


def run(args: argparse.Namespace) -> None:
    """
    Run program.

    :param args: input arguments
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
        input_params = load_params(args)
        result_params = get_result(input_params)
        print_result(params=result_params, ignore_warnings=args.ignore_warnings)
        if args.save_path:
            save_details = save_result(
                params=result_params,
                file_path=args.save_path,
                file_format=args.save_format,
                ignore_warnings=args.ignore_warnings)
            if not save_details["status"]:
                print(SAVE_FILE_ERROR_MESSAGE)
            else:
                print(save_details["message"])
