# -*- coding: utf-8 -*-
"""mycoffee main."""
from mycoffee.params import METHODS_MAP
from mycoffee.functions import run
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    #parser.epilog = ADDITIONAL_INFO
    parser.add_argument('--method', help='method', type=str, choices=sorted(METHODS_MAP), required=True)
    parser.add_argument('--coffee_ratio', help='coffee ratio', type=float)
    parser.add_argument('--water_ratio', help='water ratio', type=float)
    parser.add_argument('--water', help='water', type=float)
    parser.add_argument('--cups', help='cups', type=int)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    try:
        run(args)
    except (KeyboardInterrupt, EOFError):
        #print(EXIT_MESSAGE)
        pass


if __name__ == "__main__":
    main()
