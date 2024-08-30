# -*- coding: utf-8 -*-
"""
>>> import argparse
>>> from mycoffee.functions import *
>>> from mycoffee.params import *
>>> test_params = {"method":"v60", "cups":2, "coffee":30, "water":500, "coffee_ratio": 3, "water_ratio":50, "info":"V60 method"}
>>> print_message(test_params)
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
Coffee: 30 gr
<BLANKLINE>
Water: 500 gr
<BLANKLINE>
Ratio: 3/50
<BLANKLINE>
Info: V60 method
<BLANKLINE>
>>> test_params = {"method":"v60", "cups":2, "coffee":30, "water":500, "coffee_ratio": 3, "water_ratio":50, "info":""}
>>> print_message(test_params)
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
Coffee: 30 gr
<BLANKLINE>
Water: 500 gr
<BLANKLINE>
Ratio: 3/50
<BLANKLINE>
Info: Nothing :)
<BLANKLINE>
>>> chemex_params = load_method_params("chemex")
>>> chemex_params == {'info': 'Chemex method', 'water': 240, 'cups': 1, 'coffee_ratio': 1, 'water_ratio': 15}
True
>>> show_methods_list()
Methods list:
<BLANKLINE>
1. `chemex` - Chemex method
2. `custom` - Custom brewing method
3. `espresso` - Espresso method
4. `french-press` - French press method
5. `siphon` - Siphon method
6. `v60` - V60 method
>>> test_params = {"method":"v60", "cups":2, "coffee":30, "water":335, "coffee_ratio": 3, "water_ratio":50, "info":"V60 method"}
>>> coffee_calc(test_params)
20.1
>>> coffee_calc(test_params, digit=0)
20.0
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('--method', help='brewing method', type=str, choices=sorted(METHODS_MAP), default="custom")
>>> _ = parser.add_argument('--info', help='brewing method info', type=str)
>>> _ = parser.add_argument('--coffee-ratio', help='coffee ratio', type=int)
>>> _ = parser.add_argument('--water-ratio', help='water ratio', type=int)
>>> _ = parser.add_argument('--water', help='water(ml)', type=float)
>>> _ = parser.add_argument('--cups', help='number of cups', type=int)
>>> _ = parser.add_argument('--methods-list', help='brewing methods list', nargs="?", const=1)
>>> _ = parser.add_argument('--version', help='version', nargs="?", const=1)
>>> args = parser.parse_args({"--version":True})
>>> run(args)
0.1
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
Coffee: 14.52 gr
<BLANKLINE>
Water: 242 gr
<BLANKLINE>
Ratio: 3/50
<BLANKLINE>
Info: V60 method
<BLANKLINE>
>>> args = parser.parse_args(["--method", 'v60', "--water-ratio", '500', "--coffee-ratio", '23', "--water", '5000'])
>>> params = load_params(args)
>>> params["water"]
5000.0
>>> params["water_ratio"]
500
>>> params["coffee_ratio"]
23
>>> params["method"]
'v60'
>>> args = parser.parse_args(["--methods-list"])
>>> run(args)
Methods list:
<BLANKLINE>
1. `chemex` - Chemex method
2. `custom` - Custom brewing method
3. `espresso` - Espresso method
4. `french-press` - French press method
5. `siphon` - Siphon method
6. `v60` - V60 method
"""
