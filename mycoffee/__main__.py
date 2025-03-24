# -*- coding: utf-8 -*-
"""mycoffee main."""
from mycoffee.params import METHODS_MAP, EXIT_MESSAGE, FILE_FORMATS_LIST
from mycoffee.params import COFFEE_UNITS_MAP, WATER_UNITS_MAP, TEMPERATURE_UNITS_MAP
from mycoffee.functions import run, validate_positive_int, validate_positive_float
import argparse


def main() -> None:
    """CLI main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--method',
        help='brewing method',
        type=str.lower,
        choices=sorted(METHODS_MAP),
        default="custom")
    parser.add_argument('--message', help='extra information about the brewing method', type=str)
    parser.add_argument(
        '--coffee-ratio',
        help='coefficient for the coffee component in the ratio',
        type=validate_positive_float)
    parser.add_argument(
        '--water-ratio',
        help='coefficient for the water component in the ratio',
        type=validate_positive_float)
    parser.add_argument('--water', help='amount of water in each cup', type=validate_positive_float)
    parser.add_argument('--cups', help='number of cups', type=validate_positive_int)
    parser.add_argument('--grind', help='grind size (um)', type=validate_positive_int)
    parser.add_argument('--temperature', help='brewing temperature', type=float)
    parser.add_argument(
        '--digits',
        help='number of digits up to which the result is rounded',
        type=int,
        default=3)
    parser.add_argument(
        '--coffee-unit',
        help='coffee unit',
        type=str.lower,
        choices=sorted(COFFEE_UNITS_MAP),
        default="g")
    parser.add_argument('--water-unit', help='water unit', type=str.lower, choices=sorted(WATER_UNITS_MAP), default="g")
    parser.add_argument(
        '--temperature-unit',
        help='temperature unit',
        type=str.upper,
        choices=sorted(TEMPERATURE_UNITS_MAP),
        default="C")
    parser.add_argument('--coffee-units-list', help='coffee units list', nargs="?", const=1)
    parser.add_argument('--water-units-list', help='water units list', nargs="?", const=1)
    parser.add_argument('--temperature-units-list', help='temperature units list', nargs="?", const=1)
    parser.add_argument('--methods-list', help='brewing methods list', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--info', help='info', nargs="?", const=1)
    parser.add_argument('--ignore-warnings', help='ignore warnings', nargs="?", const=1)
    parser.add_argument('--save-path', help='file path to save', type=str)
    parser.add_argument('--save-format', help='file format', type=str.lower, choices=FILE_FORMATS_LIST, default="text")
    args = parser.parse_args()
    try:
        run(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


if __name__ == "__main__":
    main()
