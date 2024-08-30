# -*- coding: utf-8 -*-
"""
>>> from mycoffee.functions import *
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
Water: 500 ml
<BLANKLINE>
Ratio: 3/50
<BLANKLINE>
Info: V60 method
<BLANKLINE>
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
Water: 500 ml
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
"""
