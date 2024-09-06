# -*- coding: utf-8 -*-
"""mycoffee main."""
from mycoffee.params import METHODS_MAP, EXIT_MESSAGE
from mycoffee.functions import run
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', help='brewing method', type=str, choices=sorted(METHODS_MAP), default="custom")
    parser.add_argument('--info', help='information about the brewing method', type=str)
    parser.add_argument('--coffee-ratio', help='coefficient for the coffee component in the ratio', type=float)
    parser.add_argument('--water-ratio', help='coefficient for the water component in the ratio', type=float)
    parser.add_argument('--water', help='amount of water in each cup (gr)', type=float)
    parser.add_argument('--cups', help='number of cups', type=int)
    parser.add_argument('--methods-list', help='brewing methods list', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    try:
        run(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


if __name__ == "__main__":
    main()
