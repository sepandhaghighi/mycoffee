# -*- coding: utf-8 -*-
"""
>>> import os
>>> import json
>>> import yaml
>>> import io
>>> import contextlib
>>> import argparse
>>> from mycoffee.functions import *
>>> from mycoffee.params import *
>>> f = io.StringIO()
>>> with contextlib.redirect_stdout(f):
...	    print_mycoffee_info()
>>> MY_COFFEE_OVERVIEW in f.getvalue()
True
>>> MY_COFFEE_REPO in f.getvalue()
True
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
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "C", "grind": 500, "temperature":93, "mode":"water-to-coffee"}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> file.close()
>>> save_details = save_result(result_params, "save_test1.json", "json")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test1.json", "r")
>>> save_test1_object = json.load(file)
>>> _ = format_date(save_test1_object["date"])
>>> del save_test1_object["date"]
>>> save_test1_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"water-to-coffee", 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g','ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> save_details = save_result(result_params, "save_test1.yaml", "yaml")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test1.yaml", "r")
>>> save_test1_object = yaml.safe_load(file)
>>> _ = format_date(save_test1_object["date"])
>>> del save_test1_object["date"]
>>> save_test1_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"water-to-coffee", 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g','ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> input_params = {"method":"v60", "cups":2, "coffee":30, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "C", "grind": 500, "temperature":93, "mode":"ratio"}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
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
>>> save_details = save_result(result_params, "save_test7.txt")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test7.txt", "r")
>>> print(file.read())
<BLANKLINE>
...
<BLANKLINE>
Mode: Water & Coffee --> Ratio
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
>>> file.close()
>>> save_details = save_result(result_params, "save_test7.json", "json")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test7.json", "r")
>>> save_test4_object = json.load(file)
>>> _ = format_date(save_test4_object["date"])
>>> del save_test4_object["date"]
>>> save_test4_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"ratio", 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g','ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> save_details = save_result(result_params, "save_test7.yaml", "yaml")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test7.yaml", "r")
>>> save_test4_object = yaml.safe_load(file)
>>> _ = format_date(save_test4_object["date"])
>>> del save_test4_object["date"]
>>> save_test4_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"ratio", 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g','ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> input_params = {"method":"v60", "cups":2, "coffee":30, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "C", "grind": 500, "temperature":93, "mode":"coffee-to-water"}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 93 C
<BLANKLINE>
Message: V60 method
<BLANKLINE>
>>> save_details = save_result(result_params, "save_test4.txt")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test4.txt", "r")
>>> print(file.read())
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 93 C
<BLANKLINE>
Message: V60 method
>>> file.close()
>>> save_details = save_result(result_params, "save_test4.json", "json")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test4.json", "r")
>>> save_test4_object = json.load(file)

>>> _ = format_date(save_test4_object["date"])
>>> del save_test4_object["date"]
>>> save_test4_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"coffee-to-water", 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g','ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> save_details = save_result(result_params, "save_test4.yaml", "yaml")
>>> save_details["status"]
True
>>> save_details["message"] == "[Info] File saved successfully!"
True
>>> file = open("save_test4.yaml", "r")
>>> save_test4_object = yaml.safe_load(file)
>>> _ = format_date(save_test4_object["date"])
>>> del save_test4_object["date"]
>>> save_test4_object == {'mycoffee_version': MY_COFFEE_VERSION, "mode":"coffee-to-water", 'temperature': {'value':93, 'unit':'C'}, 'method': 'v60', 'water': {'cup':500, 'total':1000, 'unit':'g','ratio':50}, 'cups': 2, 'digits': 3, 'coffee': {'total':60, 'cup': 30, 'unit': 'g', 'ratio': 3}, 'message': 'V60 method', 'grind': {'value':500, 'unit':'um', 'type':get_grind_type(500)},'warnings': [], 'ratio': 0.06, 'strength': get_brew_strength(0.06)}
True
>>> file.close()
>>> save_details = save_result({}, 2)
>>> save_details["status"]
False
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "F", "grind": 500, "temperature":65, "mode":"water-to-coffee"}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
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
>>> input_params = {"method":"v60", "cups":2, "coffee":30, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature_unit": "F", "grind": 500, "temperature":65, "mode":"coffee-to-water"}
>>> result_params = get_result(input_params)
>>> print_result(result_params)
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
Grind: 500 um (Medium-Fine)
<BLANKLINE>
Temperature: 65 F
<BLANKLINE>
Message: V60 method
<BLANKLINE>
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 3, "water_ratio":50, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 600, "temperature":95, "temperature_unit": "C", "mode":"water-to-coffee"}
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> input_params = {"method":"v60", "cups":2, "water":0.5, "coffee_ratio": 3, "water_ratio":50, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "kg", "grind": 700, "temperature":95, "temperature_unit": "C", "mode":"water-to-coffee"}
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 6, "water_ratio":1000, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 500, "temperature":95, "temperature_unit": "C", "mode":"water-to-coffee"}
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1, "water_ratio":18, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 1400, "temperature":95,"temperature_unit": "C", "mode":"water-to-coffee"}
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1, "water_ratio":18, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature": 50.2, "temperature_unit": "C", "mode":"water-to-coffee"}
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1, "water_ratio":18, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature": 122.36, "temperature_unit": "F", "mode":"water-to-coffee"}
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
<BLANKLINE>
...
<BLANKLINE>
Mode: Water --> Coffee
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
>>> input_params = {"method":"custom", "cups":2, "water":500, "coffee_ratio": 6, "water_ratio":1000, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "temperature": 94, "temperature_unit": "C", "grind": 700, "mode":"water-to-coffee"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
True
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1.2, "water_ratio":18.4, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature":94, "temperature_unit": "C", "mode":"water-to-coffee"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
True
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> input_params = {"method":"v60", "cups":2, "water":500, "coffee_ratio": 1.2, "water_ratio":50.1, "message":"", "digits":3, "coffee_unit": "g", "water_unit": "g", "grind": 20, "temperature":94, "temperature_unit": "C", "mode":"water-to-coffee"}
>>> result_params = get_result(input_params)
>>> check_ratio_limits(method=result_params["method"], ratio=result_params["ratio"])
False
>>> check_grind_limits(method=result_params["method"], grind=result_params["grind"]["value"])
False
>>> check_temperature_limits(method=result_params["method"], temperature=result_params["temperature"]["value"], temperature_unit=result_params["temperature"]["unit"])
True
>>> chemex_params = load_method_params("chemex")
>>> chemex_params == {'message': 'Chemex method', 'water': 240, 'coffee': 16, 'cups': 1, 'coffee_ratio': 1, 'water_ratio': 15, 'digits': 3, 'coffee_unit': 'g', 'water_unit': 'g', 'grind': 670, 'temperature':94, "temperature_unit": "C", "mode":"water-to-coffee"}
True
>>> show_methods_list()
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
>>> calculate_coffee(ratio=test_params["ratio"], water=test_params["water"], water_unit=test_params["water_unit"], coffee_unit=test_params["coffee_unit"])
20.099999999999998
>>> test_params = {"method":"v60", "cups":2, "water":335, "coffee_ratio": 3, "water_ratio":50, "message":"V60 method", 'coffee_unit': 'g', 'water_unit': 'g', "ratio": 3/50}
>>> calculate_coffee(ratio=test_params["ratio"], water=test_params["water"], water_unit=test_params["water_unit"], coffee_unit=test_params["coffee_unit"])
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
>>> os.remove("save_test4.txt")
>>> os.remove("save_test7.txt")
>>> os.remove("save_test1.json")
>>> os.remove("save_test4.json")
>>> os.remove("save_test7.json")
>>> os.remove("save_test1.yaml")
>>> os.remove("save_test4.yaml")
>>> os.remove("save_test7.yaml")
"""
