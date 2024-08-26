# -*- coding: utf-8 -*-
"""mycoffee functions."""
import os
import sys
import time
from mycoffee.params import MESSAGE_TEMPLATE
from mycoffee.params import DEFAULT_PARAMS, METHODS_MAP

from art import tprint


def print_message(params):
    """
    Print message.

    :param message: message text
    :type message: str
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :param confirm: confirm flag
    :type confirm: bool
    :return: None
    """
    print(MESSAGE_TEMPLATE.format(params["method"], params["cups"], params["coffee"], params["water"], params["coffee_ratio"], params["water_ratio"]))



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


def show_programs_list():
    """
    Show programs list.

    :return: None
    """
    print("Programs list:\n")
    for i, program in enumerate(sorted(PROGRAMS_MAP), 1):
        print(
            PROGRAMS_LIST_TEMPLATE.format(
                i,
                program,
                PROGRAMS_MAP[program]['message']))


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


def clear_screen():
    """
    Clear screen function.

    :return: None
    """
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def coffee_calc(params):
    """
    Calculate coffee.

    :param params: parameters
    :type params: dict
    :return: coffee amount as float
    """
    coffee = params["water"] * params["coffee_ratio"] / params["water_ratio"]
    return coffee


def run(args):
    """
    Run program.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: None
    """
    params = load_params(args)
    coffee = coffee_calc(params)
    params["coffee"] = coffee
    print_message(params)