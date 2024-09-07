# -*- coding: utf-8 -*-
"""mycoffee functions."""
from mycoffee.params import MESSAGE_TEMPLATE, METHODS_LIST_TEMPLATE
from mycoffee.params import MY_COFFEE_VERSION, DEFAULT_PARAMS, METHODS_MAP
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


def print_message(params):
    """
    Print message.

    :param params: parameters
    :type params: dict
    :return: None
    """
    tprint("MyCoffee", font="bulbhead")
    info = params["info"]
    if len(info) == 0:
        info = "Nothing :)"
    print(
        MESSAGE_TEMPLATE.format(
            params["method"],
            params["cups"],
            params["coffee"],
            params["water"],
            params["coffee_ratio"],
            params["water_ratio"],
            info))


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
    params["method"] = args.method
    return params


def filter_params(params, digits=3):
    """
    Filter params.

    :param params: parameters
    :type params: dict
    :param digits: number of digits up to which the given number is to be rounded
    :type digits: int
    :return: filtered parameters as dict
    """
    params["coffee"] = round(params["coffee"], digits)
    if is_int(params["coffee"]):
        params["coffee"] = int(params["coffee"])
    if is_int(params["water_ratio"]):
        params["water_ratio"] = int(params["water_ratio"])
    if is_int(params["coffee_ratio"]):
        params["coffee_ratio"] = int(params["coffee_ratio"])
    if len(params["info"]) == 0:
        params["info"] = "Nothing :)"
    return params




def coffee_calc(params, digits=3):
    """
    Calculate coffee.

    :param params: parameters
    :type params: dict
    :param digits: number of digits up to which the given number is to be rounded
    :type digits: int
    :return: coffee amount as float
    """
    coffee = params["water"] * params["coffee_ratio"] / params["water_ratio"]
    coffee = round(coffee, digits)
    if is_int(coffee):
        coffee = int(coffee)
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
    else:
        params = load_params(args)
        coffee = coffee_calc(params)
        params["coffee"] = coffee
        print_message(params)
