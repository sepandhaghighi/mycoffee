# -*- coding: utf-8 -*-
"""
>>> import os
>>> import json
>>> import yaml
>>> import argparse
>>> from mycoffee.functions import *
>>> from mycoffee.params import *
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('--method', help='brewing method', type=str.lower, choices=sorted(METHODS_MAP), default="custom")
>>> _ = parser.add_argument('--message', help='extra information about the brewing method', type=str)
>>> _ = parser.add_argument('--coffee-ratio', help='coffee ratio', type=validate_positive_float)
>>> _ = parser.add_argument('--water-ratio', help='water ratio', type=validate_positive_float)
>>> _ = parser.add_argument('--water', help='water', type=validate_positive_float)
>>> _ = parser.add_argument('--coffee', help='coffee', type=validate_positive_float)
>>> _ = parser.add_argument('--cups', help='number of cups', type=validate_positive_int)
>>> _ = parser.add_argument('--grind', help='grind size (um)', type=validate_positive_int)
>>> _ = parser.add_argument('--temperature', help='brewing temperature', type=float)
>>> _ = parser.add_argument('--digits', help='number of digits up to which the result is rounded', type=int, default=3)
>>> _ = parser.add_argument('--coffee-unit', help='coffee unit', type=str.lower, choices=sorted(COFFEE_UNITS_MAP), default="g")
>>> _ = parser.add_argument('--water-unit', help='water unit', type=str.lower, choices=sorted(WATER_UNITS_MAP), default="g")
>>> _ = parser.add_argument('--temperature-unit', help='temperature unit', type=str.upper, choices=sorted(TEMPERATURE_UNITS_MAP), default="C")
>>> _ = parser.add_argument('--coffee-units-list', help='coffee units list', nargs="?", const=1)
>>> _ = parser.add_argument('--water-units-list', help='water units list', nargs="?", const=1)
>>> _ = parser.add_argument('--temperature-units-list', help='temperature units list', nargs="?", const=1)
>>> _ = parser.add_argument('--methods-list', help='brewing methods list', nargs="?", const=1)
>>> _ = parser.add_argument('--version', help='version', nargs="?", const=1)
>>> _ = parser.add_argument('--info', help='info', nargs="?", const=1)
>>> _ = parser.add_argument('--ignore-warnings', help='ignore warnings', nargs="?", const=1)
>>> _ = parser.add_argument('--mode', help='conversion mode', type=str.lower, choices=MODES_LIST, default="water-to-coffee")
>>> _ = parser.add_argument('--save-path', help='file path to save', type=str)
>>> _ = parser.add_argument('--save-format', help='file format', type=str.lower, choices=FILE_FORMATS_LIST, default="text")
>>> args = parser.parse_args({"--version":True})
>>> run_program(args)
2.0
>>>
>>> args = parser.parse_args(["--method", 'v60'])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 550 um (Medium-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
>>> args = parser.parse_args(["--method", 'v60', "--mode", 'coffee-to-water'])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 550 um (Medium-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
>>> args = parser.parse_args(["--method", 'V60', '--grind', '50', '--save-path', "save_test2.txt"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
>>> file = open("save_test2.txt", "r")
>>> print(file.read())
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
>>> args = parser.parse_args(["--method", 'V60', '--grind', '50', '--save-path', "save_test5.txt", '--mode', 'coffee-to-water'])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
>>> file = open("save_test5.txt", "r")
>>> print(file.read())
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--save-path', "save_test2.json", '--save-format', "JsOn"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
>>> file = open("save_test2.json", "r")
>>> save_test2_object = json.load(file)
>>> _ = format_date(save_test2_object["date"])
>>> del save_test2_object["date"]
>>> save_test2_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"water-to-coffee", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total':15, 'cup':15, 'unit':'g', 'ratio':3}, 'cups': 1,'digits': 3,'water': {'cup':250, 'total':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)}, 'warnings': ['The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`'], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--save-path', "save_test2.yaml", '--save-format', "YaMl"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
>>> file = open("save_test2.yaml", "r")
>>> save_test2_object = yaml.safe_load(file)
>>> _ = format_date(save_test2_object["date"])
>>> del save_test2_object["date"]
>>> save_test2_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"water-to-coffee", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total':15, 'cup':15, 'unit':'g', 'ratio':3}, 'cups': 1,'digits': 3,'water': {'cup':250, 'total':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)}, 'warnings': ['The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`'], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--save-path', "save_test5.json", '--save-format', "JsOn", "--mode", "coffee-to-water"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
>>> file = open("save_test5.json", "r")
>>> save_test5_object = json.load(file)
>>> _ = format_date(save_test5_object["date"])
>>> del save_test5_object["date"]
>>> save_test5_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"coffee-to-water", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total':15, 'cup':15, 'unit':'g', 'ratio':3}, 'cups': 1,'digits': 3,'water': {'cup':250, 'total':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)}, 'warnings': ['The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`'], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--save-path', "save_test5.yaml", '--save-format', "YAML", "--mode", "coffee-to-water"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
>>> file = open("save_test5.yaml", "r")
>>> save_test5_object = yaml.safe_load(file)
>>> _ = format_date(save_test5_object["date"])
>>> del save_test5_object["date"]
>>> save_test5_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"coffee-to-water", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total':15, 'cup':15, 'unit':'g', 'ratio':3}, 'cups': 1,'digits': 3,'water': {'cup':250, 'total':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)}, 'warnings': ['The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`'], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test3.txt"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Info] File saved successfully!
>>> file = open("save_test3.txt", "r")
>>> print(file.read())
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test6.txt", "--mode", "coffee-to-water", "--coffee", "30"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   30 g
    - Total: 30 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 500 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Info] File saved successfully!
>>> file = open("save_test6.txt", "r")
>>> print(file.read())
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   30 g
    - Total: 30 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 500 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test3.json", '--save-format', "json"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Info] File saved successfully!
>>> file = open("save_test3.json", "r")
>>> save_test3_object = json.load(file)
>>> _ = format_date(save_test3_object["date"])
>>> del save_test3_object["date"]
>>> save_test3_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"water-to-coffee", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total': 15, 'cup': 15, 'unit': 'g', 'ratio': 3}, 'cups': 1,'digits': 3, 'water': {'total':250, 'cup':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)},"warnings":[], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test3.yaml", '--save-format', "yaml"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Info] File saved successfully!
>>> file = open("save_test3.yaml", "r")
>>> save_test3_object = yaml.safe_load(file)
>>> _ = format_date(save_test3_object["date"])
>>> del save_test3_object["date"]
>>> save_test3_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"water-to-coffee", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total': 15, 'cup': 15, 'unit': 'g', 'ratio': 3}, 'cups': 1,'digits': 3, 'water': {'total':250, 'cup':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)},"warnings":[], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test6.json", '--save-format', "json", "--mode", "coffee-to-water", "--coffee", "30", "--cups", "2"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 2
<BLANKLINE>
Coffee:
    - Cup:   30 g
    - Total: 60 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 1000 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Info] File saved successfully!
>>> file = open("save_test6.json", "r")
>>> save_test6_object = json.load(file)
>>> _ = format_date(save_test6_object["date"])
>>> del save_test6_object["date"]
>>> save_test6_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"coffee-to-water", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total': 60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'cups': 2,'digits': 3, 'water': {'total':1000, 'cup':500, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)},"warnings":[], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test6.yaml", '--save-format', "YamL", "--mode", "coffee-to-water", "--coffee", "30", "--cups", "2"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Coffee --> Water
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 2
<BLANKLINE>
Coffee:
    - Cup:   30 g
    - Total: 60 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 1000 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Info] File saved successfully!
>>> file = open("save_test6.yaml", "r")
>>> save_test6_object = yaml.safe_load(file)
>>> _ = format_date(save_test6_object["date"])
>>> del save_test6_object["date"]
>>> save_test6_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"coffee-to-water", 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total': 60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'cups': 2,'digits': 3, 'water': {'total':1000, 'cup':500, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)},"warnings":[], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "f://", '--save-format', "json"])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Error] Failed to save file!
>>> args = parser.parse_args(["--method", 'V60', '--grind', '50', '--save-path', "save_test8.txt", '--mode', 'ratio'])
>>> run_program(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
...
<BLANKLINE>
Mode: Water & Coffee --> Ratio
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
<BLANKLINE>
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Info] File saved successfully!
<BLANKLINE>
>>> file = open("save_test8.txt", "r")
>>> print(file.read())
<BLANKLINE>
...
<BLANKLINE>
Mode: Water & Coffee --> Ratio
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 1
<BLANKLINE>
Coffee:
<BLANKLINE>
    - Cup:   15 g
    - Total: 15 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 250 g
    - Total: 250 g
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 50 um (Extra-Fine)
<BLANKLINE>
Temperature: 91 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
<BLANKLINE>
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', "--water-ratio", '500', "--coffee-ratio", '23', "--water", '5000'])
>>> params = load_params(args)
>>> params = get_result(params, enable_filter=False)
>>> params["water"]["cup"]
5000.0
>>> params["water"]["total"]
5000.0
>>> params["water"]["ratio"]
500.0
>>> params["coffee"]["ratio"]
23.0
>>> params["method"]
'v60'
>>> params = filter_params(params)
>>> params["water"]["ratio"]
500
>>> params["coffee"]["ratio"]
23
>>> params["water"]["total"]
5000
>>> params["cups"]
1
>>> args = parser.parse_args(["--method", 'v60', "--water-ratio", '500', "--coffee-ratio", '23', "--coffee", '230', "--mode", "coffee-to-water"])
>>> params = load_params(args)
>>> params = get_result(params, enable_filter=False)
>>> params["coffee"]["cup"]
230.0
>>> params["coffee"]["total"]
230.0
>>> params["water"]["cup"]
5000.0
>>> params["water"]["total"]
5000.0
>>> params["water"]["ratio"]
500.0
>>> params["coffee"]["ratio"]
23.0
>>> params["method"]
'v60'
>>> params = filter_params(params)
>>> params["water"]["ratio"]
500
>>> params["coffee"]["ratio"]
23
>>> params["water"]["total"]
5000
>>> params["coffee"]["total"]
230
>>> params["cups"]
1
>>> args = parser.parse_args(["--method", 'v60', "--water", '500', "--coffee", '230', "--mode", "ratio", "--cup", "2"])
>>> params = load_params(args)
>>> params = get_result(params, enable_filter=False)
>>> params["coffee"]["cup"]
230.0
>>> params["coffee"]["total"]
460.0
>>> params["water"]["cup"]
500.0
>>> params["water"]["total"]
1000.0
>>> params["water"]["ratio"]
50
>>> params["coffee"]["ratio"]
23
>>> params["method"]
'v60'
>>> params = filter_params(params)
>>> params["water"]["ratio"]
50
>>> params["coffee"]["ratio"]
23
>>> params["water"]["total"]
1000
>>> params["coffee"]["total"]
460
>>> params["cups"]
2
>>> args = parser.parse_args(["--method", 'v60', "--water-ratio", '500', "--coffee-ratio", '23', "--water", '5000000', "--water-unit", "mg"])
>>> params = load_params(args)
>>> params["water"]
5000000.0
>>> params["water_ratio"]
500.0
>>> params["coffee_ratio"]
23.0
>>> params["method"]
'v60'
>>> args = parser.parse_args(["--method", 'steep-and-release', "--digits", '1', "--water-unit", "mg"])
>>> params = load_params(args)
>>> ratio = params["coffee_ratio"] / params["water_ratio"]
>>> params["coffee"] = calculate_coffee(ratio=ratio, water=params["water"], water_unit=params["water_unit"], coffee_unit=params["coffee_unit"])
>>> params["water"]
255000
>>> params["coffee"]
15.9375
>>> params["water_ratio"]
16
>>> params["coffee_ratio"]
1
>>> params["method"]
'steep-and-release'
>>> args = parser.parse_args(["--method", 'steep-and-release', "--digits", '1'])
>>> params = load_params(args)
>>> params = get_result(params, enable_filter=False)
>>> params["water"]["cup"]
255
>>> params["water"]["total"]
255
>>> params["coffee"]["total"]
15.9375
>>> params["coffee"]["cup"]
15.9375
>>> params["water"]["ratio"]
16
>>> params["coffee"]["ratio"]
1
>>> params["method"]
'steep-and-release'
>>> params = filter_params(params)
>>> params["water"]["ratio"]
16
>>> params["coffee"]["ratio"]
1
>>> params["water"]["cup"]
255
>>> params["water"]["total"]
255
>>> params["coffee"]["total"]
15.9
>>> params["coffee"]["cup"]
15.9
>>> params["digits"]
1
>>> params["cups"]
1
>>> args = parser.parse_args(["--method", 'steep-and-release', "--digits", '1', "--cups", '3', "--temperature", '92', "--temperature-unit", 'F'])
>>> params = load_params(args)
>>> params = get_result(params, enable_filter=False)
>>> params["water"]["total"]
765
>>> params["water"]["cup"]
255
>>> params["coffee"]["total"]
47.8125
>>> params["water"]["ratio"]
16
>>> params["coffee"]["ratio"]
1
>>> params["method"]
'steep-and-release'
>>> params = filter_params(params)
>>> params["water"]["ratio"]
16
>>> params["coffee"]["ratio"]
1
>>> params["water"]["cup"]
255
>>> params["water"]["total"]
765
>>> params["coffee"]["total"]
47.8
>>> params["digits"]
1
>>> params["cups"]
3
>>> params["temperature"]["value"]
92
>>> params["temperature"]["unit"]
'F'
>>> args = parser.parse_args(["--method", 'steep-and-release', "--digits", '1', "--cups", '3', "--temperature-unit", 'F'])
>>> params = load_params(args)
>>> params["temperature"]
199.4
>>> params["temperature_unit"]
'F'
>>> args = parser.parse_args(["--method", 'steep-and-release', "--digits", '1', "--cups", '3', "--coffee-unit", "oz"])
>>> params = load_params(args)
>>> params = get_result(params, enable_filter=False)
>>> params["water"]["cup"]
255
>>> params["water"]["total"]
765
>>> params["coffee"]["total"]
1.686536305734375
>>> params["water"]["ratio"]
16
>>> params["coffee"]["ratio"]
1
>>> params["method"]
'steep-and-release'
>>> params = filter_params(params)
>>> params["water"]["ratio"]
16
>>> params["coffee"]["ratio"]
1
>>> params["water"]["cup"]
255
>>> params["water"]["total"]
765
>>> params["coffee"]["total"]
1.7
>>> params["digits"]
1
>>> params["cups"]
3
>>> args = parser.parse_args(["--methods-list"])
>>> run_program(args)
Methods list:
<BLANKLINE>
1. `aero-press` - AeroPress standard method
2. `aero-press-conc` - AeroPress concentrate method
3. `aero-press-inv` - AeroPress inverted method
4. `auto-drip` - Auto drip method
5. `chemex` - Chemex method
6. `clever-dripper` - Clever dripper method
7. `cold-brew` - Cold brew method
8. `cold-brew-conc` - Cold brew concentrate method
9. `cupping` - Cupping method
10. `custom` - Custom brewing method
11. `espresso` - Espresso method
12. `french-press` - French press method
13. `instant-coffee` - Instant coffee
14. `kalita-wave` - Kalita wave method
15. `lungo` - Lungo method
16. `moka-pot` - Moka pot method
17. `phin-filter` - Phin filter method
18. `pour-over` - Pour-over method
19. `ristretto` - Ristretto method
20. `siphon` - Siphon method
21. `steep-and-release` - Steep-and-release method
22. `turkish` - Turkish method
23. `v60` - V60 method
>>> args = parser.parse_args(["--coffee-units-list"])
>>> run_program(args)
Coffee units list:
<BLANKLINE>
1. `cb` - coffee bean
2. `ct` - carat
3. `cup` - cup
4. `dsp` - dessertspoon
5. `dwt` - pennyweight
6. `g` - gram
7. `gr` - grain
8. `kg` - kilogram
9. `lb` - pound
10. `mg` - milligram
11. `oz` - ounce
12. `t lb` - troy pound
13. `t oz` - troy ounce
14. `tbsp` - tablespoon
15. `tsp` - teaspoon
>>> args = parser.parse_args(["--water-units-list"])
>>> run_program(args)
Water units list:
<BLANKLINE>
1. `cc` - cubic centimeter
2. `cl` - centiliter
3. `ct` - carat
4. `cup` - cup
5. `dsp` - dessertspoon
6. `dwt` - pennyweight
7. `fl oz` - fluid ounce
8. `g` - gram
9. `gr` - grain
10. `kg` - kilogram
11. `l` - liter
12. `lb` - pound
13. `mg` - milligram
14. `ml` - milliliter
15. `oz` - ounce
16. `pt` - pint
17. `qt` - quart
18. `t lb` - troy pound
19. `t oz` - troy ounce
20. `tbsp` - tablespoon
21. `tsp` - teaspoon
>>> args = parser.parse_args(["--temperature-units-list"])
>>> run_program(args)
Temperature units list:
<BLANKLINE>
1. `C` - Celsius
2. `F` - Fahrenheit
3. `K` - Kelvin
>>> os.remove("save_test2.txt")
>>> os.remove("save_test3.txt")
>>> os.remove("save_test5.txt")
>>> os.remove("save_test6.txt")
>>> os.remove("save_test8.txt")
>>> os.remove("save_test2.json")
>>> os.remove("save_test3.json")
>>> os.remove("save_test5.json")
>>> os.remove("save_test6.json")
>>> os.remove("save_test2.yaml")
>>> os.remove("save_test3.yaml")
>>> os.remove("save_test5.yaml")
>>> os.remove("save_test6.yaml")
"""
