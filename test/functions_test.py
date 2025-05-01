# -*- coding: utf-8 -*-
"""
>>> import os
>>> import json
>>> import argparse
>>> from mycoffee.functions import *
>>> from mycoffee.params import *
>>> convert_coffee(122, "g")
122
>>> convert_coffee(122, "cb")
921
>>> convert_water(1, "g")
1
>>> convert_water(1, "kg")
0.001
>>> convert_water(1, "kg", False)
0.001
>>> convert_water(1, "kg", True)
1000.0
>>> get_grind_type(100)
'Extra-Fine'
>>> get_brew_strength(1/60)
'Very Weak'
>>> get_brew_strength(1/30)
'Weak'
>>> get_brew_strength(1/22)
'Medium'
>>> get_brew_strength(1/15)
'Strong'
>>> get_brew_strength(1/2)
'Very Strong'
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "C", "grind": 500, "temperature":93}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 93 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
>>> save_details = save_result(result_params, "save_test1.txt")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test1.txt", "r")
>>> print(file.read())
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 93 C
<BLANKLINE>
Message: V60 method
>>> file.close()
>>> save_details = save_result(result_params, "save_test1.json", "json")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test1.json", "r")
>>> save_test1_object = json.load(file)
>>> save_test1_object == {'mycoffee_version': MY_COFFEE_VERSION, 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g', 'ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> save_details = save_result({}, 2)
>>> save_details["status"]
False
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "F", "grind": 500, "temperature":65}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 65 F
<BLANKLINE>
Message: V60 method
<BLANKLINE>
[Warning] The temperature is not within the recommended range. For `v60`, the temperature can be anywhere between `185 F` and `203 F`
>>> print_result(result_params, ignore_warnings=True)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 65 F
<BLANKLINE>
Message: V60 method
<BLANKLINE>
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 600, "temperature":95, "temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
True
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
Grind: 600 um (Medium-Fine)
<BLANKLINE>
Temperature: 95 C
<BLANKLINE>
Message: Nothing :)
<BLANKLINE>
>>> input_params = {"method":"v60", "cups":2, "water":0.5, "coffee_ratio": 3, "water_ratio":50, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "kg", "grind": 700, "temperature":95, "temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
True
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
    - Cup: 0.5 kg
    - Total: 1 kg
<BLANKLINE>
Ratio: 3/50 (0.06)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 700 um (Medium)
<BLANKLINE>
Temperature: 95 C
<BLANKLINE>
Message: Nothing :)
<BLANKLINE>
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 6, "water_ratio":1000, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 500, "temperature":95, "temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
False
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
True
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 2
<BLANKLINE>
Coffee:
    - Cup:   3 g
    - Total: 6 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 1000 g
<BLANKLINE>
Ratio: 6/1000 (0.006)
<BLANKLINE>
Strength: Very Weak
<BLANKLINE>
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 95 C
<BLANKLINE>
Message: Nothing :)
<BLANKLINE>
[Warning] The ratio is not within the recommended range. For `v60`, the ratio can be anywhere between `1/18` and `1/14`
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1, "water_ratio":18, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 1400, "temperature":95,"temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 2
<BLANKLINE>
Coffee:
    - Cup:   27.778 g
    - Total: 55.556 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 1000 g
<BLANKLINE>
Ratio: 1/18 (0.056)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 1400 um (Extra-Coarse)
<BLANKLINE>
Temperature: 95 C
<BLANKLINE>
Message: Nothing :)
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1, "water_ratio":18, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature": 50.2, "temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
False
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 2
<BLANKLINE>
Coffee:
    - Cup:   27.778 g
    - Total: 55.556 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 1000 g
<BLANKLINE>
Ratio: 1/18 (0.056)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 20 um (Extra-Fine)
<BLANKLINE>
Temperature: 50.2 C
<BLANKLINE>
Message: Nothing :)
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Warning] The temperature is not within the recommended range. For `v60`, the temperature can be anywhere between `85 C` and `95 C`
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1, "water_ratio":18, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature": 122.36, "temperature_unit": "F"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
False
>>> print_result(result_params)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Method: `v60`
<BLANKLINE>
Cups: 2
<BLANKLINE>
Coffee:
    - Cup:   27.778 g
    - Total: 55.556 g
<BLANKLINE>
Water:
<BLANKLINE>
    - Cup: 500 g
    - Total: 1000 g
<BLANKLINE>
Ratio: 1/18 (0.056)
<BLANKLINE>
Strength: Medium
<BLANKLINE>
Grind: 20 um (Extra-Fine)
<BLANKLINE>
Temperature: 122.36 F
<BLANKLINE>
Message: Nothing :)
<BLANKLINE>
[Warning] The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`
[Warning] The temperature is not within the recommended range. For `v60`, the temperature can be anywhere between `185 F` and `203 F`
>>> input_params = {"method":"custom", "cups":2, "water":500, "coffee_ratio": 6, "water_ratio":1000, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature": 94, "temperature_unit": "C", "grind": 700}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
True
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1.2, "water_ratio":18.4, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature":94, "temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1.2, "water_ratio":50.1, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature":94, "temperature_unit": "C"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
False
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> chemex_params = load_method_params("chemex")
>>> chemex_params == {'message': 'Chemex method', 'water': 240, 'cups': 1, 'coffee_ratio': 1, 'water_ratio': 15, 'digits': 3, 'coffee_unit': 'g', 'water_unit': 'g', 'grind': 670, 'temperature':94, "temperature_unit": "C"}
True
>>> show_methods_list()
Methods list:
<BLANKLINE>
1. `aero-press` - AeroPress standard method
2. `aero-press-conc` - AeroPress concentrate method
3. `aero-press-inv` - AeroPress inverted method
4. `auto-drip` - Auto drip method
5. `chemex` - Chemex method
6. `cold-brew` - Cold brew method
7. `cold-brew-conc` - Cold brew concentrate method
8. `cupping` - Cupping method
9. `custom` - Custom brewing method
10. `espresso` - Espresso method
11. `french-press` - French press method
12. `lungo` - Lungo method
13. `moka-pot` - Moka pot method
14. `pour-over` - Pour-over method
15. `ristretto` - Ristretto method
16. `siphon` - Siphon method
17. `steep-and-release` - Steep-and-release method
18. `turkish` - Turkish method
19. `v60` - V60 method
>>> show_coffee_units_list()
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
>>> show_water_units_list()
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
>>> show_temperature_units_list()
Temperature units list:
<BLANKLINE>
1. `C` - Celsius
2. `F` - Fahrenheit
3. `K` - Kelvin
>>> test_params = {"method":"v60", "cups":1, "water":335, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", 'coffee_unit': 'g', 'water_unit': 'g', "ratio": 3/50}
>>> calc_coffee(ratio=test_params["ratio"], water=test_params["water"], water_unit=test_params["water_unit"], coffee_unit=test_params["coffee_unit"])
20.099999999999998
>>> test_params = {"method":"v60", "cups":2, "water":335, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", 'coffee_unit': 'g', 'water_unit': 'g', "ratio": 3/50}
>>> calc_coffee(ratio=test_params["ratio"], water=test_params["water"], water_unit=test_params["water_unit"], coffee_unit=test_params["coffee_unit"])
20.099999999999998
>>> test_params = {"method":"v60", "ratio": 3/50, "cups":2, "coffee":{"total":40.2, "cup":20.1, "ratio":3.0, "unit":'g'}, "water":{"cup":335.0, "total":670, "ratio":50.0}, "message":"", "digits":3, "temperature":{"value":94.0, "unit": "C"}}
>>> test_params = filter_params(test_params)
>>> test_params["coffee"]["total"]
40.2
>>> test_params["coffee"]["cup"]
20.1
>>> test_params["water"]["ratio"]
50
>>> test_params["coffee"]["ratio"]
3
>>> test_params["water"]["cup"]
335
>>> test_params["water"]["total"]
670
>>> test_params["temperature"]["value"]
94
>>> test_params["message"]
'Nothing :)'
>>> test_params = {"method":"v60", "ratio": 3.12345/50.12345, "cups":2, "coffee":{"total": 41.76653202852158, "cup": 20.88326601426079, "ratio":3.12345, "unit":'g'}, "water":{"cup":335.12345, "total":670.2469, "ratio":50.12345},"message":"","digits":2,"temperature": {"value":94.2, "unit": "C"}}
>>> test_params = filter_params(test_params)
>>> test_params["coffee"]["total"]
41.77
>>> test_params["coffee"]["cup"]
20.88
>>> test_params["coffee"]["ratio"]
3.12
>>> test_params["water"]["ratio"]
50.12
>>> test_params["water"]["cup"]
335.12
>>> test_params["water"]["total"]
670.25
>>> test_params["temperature"]["value"]
94.2
>>> is_int(12.1)
False
>>> is_int(12.123)
False
>>> is_int(12.0)
True
>>> is_int(15)
True
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('--method', help='brewing method', type=str.lower, choices=sorted(METHODS_MAP), default="custom")
>>> _ = parser.add_argument('--message', help='extra information about the brewing method', type=str)
>>> _ = parser.add_argument('--coffee-ratio', help='coffee ratio', type=validate_positive_float)
>>> _ = parser.add_argument('--water-ratio', help='water ratio', type=validate_positive_float)
>>> _ = parser.add_argument('--water', help='water', type=validate_positive_float)
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
>>> _ = parser.add_argument('--save-path', help='file path to save', type=str)
>>> _ = parser.add_argument('--save-format', help='file format', type=str.lower, choices=FILE_FORMATS_LIST, default="text")
>>> args = parser.parse_args({"--version":True})
>>> run(args)
1.8
>>>
>>> args = parser.parse_args(["--method", 'v60'])
>>> run(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
>>> run(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
>>> run(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
>>> save_test2_object == {'mycoffee_version': MY_COFFEE_VERSION, 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total':15, 'cup':15, 'unit':'g', 'ratio':3}, 'cups': 1,'digits': 3,'water': {'cup':250, 'total':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)}, 'warnings': ['The grind size is not within the recommended range. For `v60`, the grind size can be anywhere between `400 um` and `700 um`'], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test3.txt"])
>>> run(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "save_test3.json", '--save-format', "json"])
>>> run(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
>>> save_test3_object == {'mycoffee_version': MY_COFFEE_VERSION, 'temperature': {'value':91, 'unit':'C'}, 'method': 'v60', 'coffee': {'total': 15, 'cup': 15, 'unit': 'g', 'ratio': 3}, 'cups': 1,'digits': 3, 'water': {'total':250, 'cup':250, 'unit':'g', 'ratio':50}, 'message': 'V60 method', 'grind': {'value':50, 'unit': 'um', 'type': get_grind_type(50)},"warnings":[], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> args = parser.parse_args(["--method", 'v60', '--grind', '50', '--ignore-warnings',  '--save-path', "f://", '--save-format', "json"])
>>> run(args)
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)
<BLANKLINE>
<BLANKLINE>
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
>>> params["coffee"] = calc_coffee(ratio=ratio, water=params["water"], water_unit=params["water_unit"], coffee_unit=params["coffee_unit"])
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
>>> run(args)
Methods list:
<BLANKLINE>
1. `aero-press` - AeroPress standard method
2. `aero-press-conc` - AeroPress concentrate method
3. `aero-press-inv` - AeroPress inverted method
4. `auto-drip` - Auto drip method
5. `chemex` - Chemex method
6. `cold-brew` - Cold brew method
7. `cold-brew-conc` - Cold brew concentrate method
8. `cupping` - Cupping method
9. `custom` - Custom brewing method
10. `espresso` - Espresso method
11. `french-press` - French press method
12. `lungo` - Lungo method
13. `moka-pot` - Moka pot method
14. `pour-over` - Pour-over method
15. `ristretto` - Ristretto method
16. `siphon` - Siphon method
17. `steep-and-release` - Steep-and-release method
18. `turkish` - Turkish method
19. `v60` - V60 method
>>> args = parser.parse_args(["--coffee-units-list"])
>>> run(args)
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
>>> run(args)
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
>>> run(args)
Temperature units list:
<BLANKLINE>
1. `C` - Celsius
2. `F` - Fahrenheit
3. `K` - Kelvin
>>> validate_positive_int("2")
2
>>> validate_positive_int("2.0")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive int value: '2.0'
>>> validate_positive_int("a")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive int value: 'a'
>>> validate_positive_int("-20")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive int value: '-20'
>>> validate_positive_int("0")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive int value: '0'
>>> validate_positive_float("2")
2.0
>>> validate_positive_float("0")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive float value: '0'
>>> validate_positive_float("-20")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive float value: '-20'
>>> validate_positive_float("a")
Traceback (most recent call last):
    ...
argparse.ArgumentTypeError: invalid positive float value: 'a'
>>> os.remove("save_test1.txt")
>>> os.remove("save_test2.txt")
>>> os.remove("save_test3.txt")
>>> os.remove("save_test1.json")
>>> os.remove("save_test2.json")
>>> os.remove("save_test3.json")
"""
