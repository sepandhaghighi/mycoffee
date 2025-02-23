# -*- coding: utf-8 -*-
"""
>>> from fractions import Fraction
>>> from mycoffee.functions import *
>>> from mycoffee.params import METHODS_MAP
>>> v60_params = load_method_params("v60") # https://www.origincoffee.co.uk/blogs/journal/brewing-at-home-v60
>>> v60_params["coffee_ratio"] == 3
True
>>> v60_params["water_ratio"] == 50
True
>>> v60_params["water"] == 250
True
>>> v60_coffee = calc_coffee(v60_params)
>>> v60_coffee == 15
True
>>> METHODS_MAP["v60"]["ratio_upper_limit"] == Fraction(1, 14)
True
>>> METHODS_MAP["v60"]["ratio_lower_limit"] == Fraction(1, 18)
True
>>> METHODS_MAP["v60"]["grind_upper_limit"] == 700
True
>>> METHODS_MAP["v60"]["grind_lower_limit"] == 400
True
>>> v60_params["grind"] == 550 # https://honestcoffeeguide.com/coffee-grind-size-chart/#v60
True
>>> METHODS_MAP["v60"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["v60"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> v60_params["temperature"] == 91 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> chemex_params = load_method_params("chemex") # https://honestcoffeeguide.com/coffee-to-water-ratio-calculator
>>> chemex_params["coffee_ratio"] == 1
True
>>> chemex_params["water_ratio"] == 15
True
>>> chemex_params["water"] == 240
True
>>> chemex_coffee = calc_coffee(chemex_params)
>>> chemex_coffee == 16
True
>>> METHODS_MAP["chemex"]["ratio_upper_limit"] == Fraction(1, 10)
True
>>> METHODS_MAP["chemex"]["ratio_lower_limit"] == Fraction(1, 21)
True
>>> METHODS_MAP["chemex"]["grind_upper_limit"] == 930
True
>>> METHODS_MAP["chemex"]["grind_lower_limit"] == 410
True
>>> chemex_params["grind"] == 670 # https://honestcoffeeguide.com/coffee-grind-size-chart/#pourover
True
>>> METHODS_MAP["chemex"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["chemex"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> chemex_params["temperature"] == 94 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> espresso_params = load_method_params("espresso") # https://honestcoffeeguide.com/coffee-to-water-ratio-calculator
>>> espresso_params["coffee_ratio"] == 1
True
>>> espresso_params["water_ratio"] == 2
True
>>> espresso_params["water"] == 36
True
>>> espresso_coffee = calc_coffee(espresso_params)
>>> espresso_coffee == 18
True
>>> METHODS_MAP["espresso"]["ratio_upper_limit"] == Fraction(2, 3)
True
>>> METHODS_MAP["espresso"]["ratio_lower_limit"] == Fraction(2, 5)
True
>>> METHODS_MAP["espresso"]["grind_upper_limit"] == 380
True
>>> METHODS_MAP["espresso"]["grind_lower_limit"] == 180
True
>>> espresso_params["grind"] == 280 # https://honestcoffeeguide.com/coffee-grind-size-chart/#espresso
True
>>> METHODS_MAP["espresso"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["espresso"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> espresso_params["temperature"] == 92 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> siphon_params = load_method_params("siphon") # https://bluebottlecoffee.com/us/eng/brew-guides/siphon
>>> siphon_params["coffee_ratio"] == 1
True
>>> siphon_params["water_ratio"] == 15
True
>>> siphon_params["water"] == 240
True
>>> siphon_coffee = calc_coffee(siphon_params)
>>> siphon_coffee == 16
True
>>> METHODS_MAP["siphon"]["ratio_upper_limit"] == Fraction(1, 12)
True
>>> METHODS_MAP["siphon"]["ratio_lower_limit"] == Fraction(1, 16)
True
>>> METHODS_MAP["siphon"]["grind_upper_limit"] == 800
True
>>> METHODS_MAP["siphon"]["grind_lower_limit"] == 375
True
>>> siphon_params["grind"] == 588 # https://honestcoffeeguide.com/coffee-grind-size-chart/#siphon
True
>>> METHODS_MAP["siphon"]["temperature_upper_limit"] == 94 # https://unionroasted.com/blogs/brewing-guides/syphon
True
>>> METHODS_MAP["siphon"]["temperature_lower_limit"] == 91 # https://unionroasted.com/blogs/brewing-guides/syphon
True
>>> siphon_params["temperature"] == 93 # https://unionroasted.com/blogs/brewing-guides/syphon
True
>>> french_press_params = load_method_params("french-press") # https://useandcares.hamiltonbeach.com/files/840230401.pdf
>>> french_press_params["coffee_ratio"] == 1
True
>>> french_press_params["water_ratio"] == 15
True
>>> french_press_params["water"] == 120
True
>>> french_press_coffee = calc_coffee(french_press_params)
>>> french_press_coffee == 8
True
>>> METHODS_MAP["french-press"]["ratio_upper_limit"] == Fraction(1, 12)
True
>>> METHODS_MAP["french-press"]["ratio_lower_limit"] == Fraction(1, 18)
True
>>> METHODS_MAP["french-press"]["grind_upper_limit"] == 1300
True
>>> METHODS_MAP["french-press"]["grind_lower_limit"] == 690
True
>>> french_press_params["grind"] == 995 # https://honestcoffeeguide.com/coffee-grind-size-chart/#french-press
True
>>> METHODS_MAP["french-press"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["french-press"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> french_press_params["temperature"] == 90 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> pour_over_params = load_method_params("pour-over") # https://www.nicolebattefeld.com/post/best-recipes-2022
>>> pour_over_params["coffee_ratio"] == 1
True
>>> pour_over_params["water_ratio"] == 15
True
>>> pour_over_params["water"] == 240
True
>>> pour_over_coffee = calc_coffee(pour_over_params)
>>> pour_over_coffee == 16
True
>>> METHODS_MAP["pour-over"]["ratio_upper_limit"] == Fraction(1, 14)
True
>>> METHODS_MAP["pour-over"]["ratio_lower_limit"] == Fraction(1, 16)
True
>>> METHODS_MAP["pour-over"]["grind_upper_limit"] == 930
True
>>> METHODS_MAP["pour-over"]["grind_lower_limit"] == 410
True
>>> pour_over_params["grind"] == 670 # https://honestcoffeeguide.com/coffee-grind-size-chart/#pourover
True
>>> METHODS_MAP["pour-over"]["temperature_upper_limit"] == 93  # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["pour-over"]["temperature_lower_limit"] == 90 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> pour_over_params["temperature"] == 92 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> auto_drip_params = load_method_params("auto-drip") # https://wonderstate.com/pages/auto-drip
>>> auto_drip_params["coffee_ratio"] == 1
True
>>> auto_drip_params["water_ratio"] == 16
True
>>> auto_drip_params["water"] == 128
True
>>> auto_drip_coffee = calc_coffee(auto_drip_params)
>>> auto_drip_coffee == 8
True
>>> METHODS_MAP["auto-drip"]["ratio_upper_limit"] == Fraction(1, 14)
True
>>> METHODS_MAP["auto-drip"]["ratio_lower_limit"] == Fraction(1, 17)
True
>>> METHODS_MAP["auto-drip"]["grind_upper_limit"] == 900
True
>>> METHODS_MAP["auto-drip"]["grind_lower_limit"] == 300
True
>>> auto_drip_params["grind"] == 600 # https://honestcoffeeguide.com/coffee-grind-size-chart/#filter-coffee-machine
True
>>> METHODS_MAP["auto-drip"]["temperature_upper_limit"] == 96  # https://counterculturecoffee.com/blogs/counter-culture-coffee/guide-to-home-coffee-makers
True
>>> METHODS_MAP["auto-drip"]["temperature_lower_limit"] == 90 # https://counterculturecoffee.com/blogs/counter-culture-coffee/guide-to-home-coffee-makers
True
>>> auto_drip_params["temperature"] == 93 # https://counterculturecoffee.com/blogs/counter-culture-coffee/guide-to-home-coffee-makers
True
>>> cold_brew_params = load_method_params("cold-brew") # https://counterculturecoffee.com/blogs/counter-culture-coffee/guide-to-cold-brew
>>> cold_brew_params["coffee_ratio"] == 1
True
>>> cold_brew_params["water_ratio"] == 11
True
>>> cold_brew_params["water"] == 242
True
>>> cold_brew_coffee = calc_coffee(cold_brew_params)
>>> cold_brew_coffee == 22
True
>>> METHODS_MAP["cold-brew"]["ratio_upper_limit"] == Fraction(1, 8)
True
>>> METHODS_MAP["cold-brew"]["ratio_lower_limit"] == Fraction(1, 15)
True
>>> METHODS_MAP["cold-brew"]["grind_upper_limit"] == 1400
True
>>> METHODS_MAP["cold-brew"]["grind_lower_limit"] == 800
True
>>> cold_brew_params["grind"] == 1100 # https://honestcoffeeguide.com/coffee-grind-size-chart/#cold-brew
True
>>> METHODS_MAP["cold-brew"]["temperature_upper_limit"] == 40 # https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water
True
>>> METHODS_MAP["cold-brew"]["temperature_lower_limit"] == 0 # https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water
True
>>> cold_brew_params["temperature"] == 20 # https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water
True
>>> cold_brew_conc_params = load_method_params("cold-brew-conc") # https://www.thespruceeats.com/cold-brew-concentrate-recipe-5197494
>>> cold_brew_conc_params["coffee_ratio"] == 1
True
>>> cold_brew_conc_params["water_ratio"] == 5
True
>>> cold_brew_conc_params["water"] == 120
True
>>> cold_brew_conc_coffee = calc_coffee(cold_brew_conc_params)
>>> cold_brew_conc_coffee == 24
True
>>> METHODS_MAP["cold-brew-conc"]["ratio_upper_limit"] == Fraction(1, 4)
True
>>> METHODS_MAP["cold-brew-conc"]["ratio_lower_limit"] == Fraction(1, 6)
True
>>> METHODS_MAP["cold-brew-conc"]["grind_upper_limit"] == 1400
True
>>> METHODS_MAP["cold-brew-conc"]["grind_lower_limit"] == 800
True
>>> cold_brew_conc_params["grind"] == 1100 # https://honestcoffeeguide.com/coffee-grind-size-chart/#cold-brew
True
>>> METHODS_MAP["cold-brew-conc"]["temperature_upper_limit"] == 40 # https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water
True
>>> METHODS_MAP["cold-brew-conc"]["temperature_lower_limit"] == 0 # https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water
True
>>> cold_brew_conc_params["temperature"] == 20 # https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water
True
>>> moka_pot_params = load_method_params("moka-pot") # https://bakedbrewedbeautiful.com/how-to-make-coffee-in-moka-pot
>>> moka_pot_params["coffee_ratio"] == 1
True
>>> moka_pot_params["water_ratio"] == 10
True
>>> moka_pot_params["water"] == 60
True
>>> moka_pot_coffee = calc_coffee(moka_pot_params)
>>> moka_pot_coffee == 6
True
>>> METHODS_MAP["moka-pot"]["ratio_upper_limit"] == Fraction(1, 7)
True
>>> METHODS_MAP["moka-pot"]["ratio_lower_limit"] == Fraction(1, 12)
True
>>> METHODS_MAP["moka-pot"]["grind_upper_limit"] == 660
True
>>> METHODS_MAP["moka-pot"]["grind_lower_limit"] == 360
True
>>> moka_pot_params["grind"] == 510 # https://honestcoffeeguide.com/coffee-grind-size-chart/#moka-pot
True
>>> METHODS_MAP["moka-pot"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["moka-pot"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> moka_pot_params["temperature"] == 93 # https://honestcoffeeguide.com/what-temperature-to-brew-a-moka-pot
True
>>> ristretto_params = load_method_params("ristretto") # https://honestcoffeeguide.com/coffee-to-water-ratio-calculator
>>> ristretto_params["coffee_ratio"] == 1
True
>>> ristretto_params["water_ratio"] == 1
True
>>> ristretto_params["water"] == 18
True
>>> ristretto_coffee = calc_coffee(ristretto_params)
>>> ristretto_coffee == 18
True
>>> METHODS_MAP["ristretto"]["ratio_upper_limit"] == Fraction(1, 1)
True
>>> METHODS_MAP["ristretto"]["ratio_lower_limit"] == Fraction(2, 3)
True
>>> METHODS_MAP["ristretto"]["grind_upper_limit"] == 380
True
>>> METHODS_MAP["ristretto"]["grind_lower_limit"] == 180
True
>>> ristretto_params["grind"] == 280 # https://honestcoffeeguide.com/coffee-grind-size-chart/#espresso
True
>>> METHODS_MAP["ristretto"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["ristretto"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> ristretto_params["temperature"] == 92 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> lungo_params = load_method_params("lungo") # https://honestcoffeeguide.com/coffee-to-water-ratio-calculator
>>> lungo_params["coffee_ratio"] == 1
True
>>> lungo_params["water_ratio"] == 4
True
>>> lungo_params["water"] == 72
True
>>> lungo_coffee = calc_coffee(lungo_params)
>>> lungo_coffee == 18
True
>>> METHODS_MAP["lungo"]["ratio_upper_limit"] == Fraction(2, 5)
True
>>> METHODS_MAP["lungo"]["ratio_lower_limit"] == Fraction(1, 4)
True
>>> METHODS_MAP["lungo"]["grind_upper_limit"] == 380
True
>>> METHODS_MAP["lungo"]["grind_lower_limit"] == 180
True
>>> lungo_params["grind"] == 280 # https://honestcoffeeguide.com/coffee-grind-size-chart/#espresso
True
>>> METHODS_MAP["lungo"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["lungo"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> lungo_params["temperature"] == 92 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> turkish_params = load_method_params("turkish") # https://www.drinktrade.com/blogs/education/how-to-make-turkish-coffee
>>> turkish_params["coffee_ratio"] == 1
True
>>> turkish_params["water_ratio"] == 10
True
>>> turkish_params["water"] == 50
True
>>> turkish_coffee = calc_coffee(turkish_params)
>>> turkish_coffee == 5
True
>>> METHODS_MAP["turkish"]["ratio_upper_limit"] == Fraction(1, 8)
True
>>> METHODS_MAP["turkish"]["ratio_lower_limit"] == Fraction(1, 12)
True
>>> METHODS_MAP["turkish"]["grind_upper_limit"] == 220
True
>>> METHODS_MAP["turkish"]["grind_lower_limit"] == 40
True
>>> turkish_params["grind"] == 130 # https://honestcoffeeguide.com/coffee-grind-size-chart/#turkish-coffee
True
>>> METHODS_MAP["turkish"]["temperature_upper_limit"] == 95 # https://ravecoffee.co.uk/blogs/news/how-to-brew-coffee-using-an-ibrik-cezve-for-turkish-style-coffee
True
>>> METHODS_MAP["turkish"]["temperature_lower_limit"] == 90 # https://ravecoffee.co.uk/blogs/news/how-to-brew-coffee-using-an-ibrik-cezve-for-turkish-style-coffee
True
>>> turkish_params["temperature"] == 90 # https://ravecoffee.co.uk/blogs/news/how-to-brew-coffee-using-an-ibrik-cezve-for-turkish-style-coffee
True
>>> cupping_params = load_method_params("cupping") # https://www.horshamcoffeeroaster.co.uk/pages/how-to-cup-coffee
>>> cupping_params["coffee_ratio"] == 11
True
>>> cupping_params["water_ratio"] == 200
True
>>> cupping_params["water"] == 150
True
>>> cupping_coffee = calc_coffee(cupping_params)
>>> cupping_coffee == 8.25
True
>>> METHODS_MAP["cupping"]["ratio_upper_limit"] == Fraction(1, 17)
True
>>> METHODS_MAP["cupping"]["ratio_lower_limit"] == Fraction(1, 19)
True
>>> METHODS_MAP["cupping"]["grind_upper_limit"] == 850
True
>>> METHODS_MAP["cupping"]["grind_lower_limit"] == 460
True
>>> cupping_params["grind"] == 655 # https://honestcoffeeguide.com/coffee-grind-size-chart/#cupping
True
>>> METHODS_MAP["cupping"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["cupping"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> cupping_params["temperature"] == 93 # https://www.diffordsguide.com/g/1113/coffee/cupping
True
>>> aero_press_params = load_method_params("aero-press") # https://aeroprecipe.com/recipes/tetsu-kasuya-aeropress-recipe
>>> aero_press_params["coffee_ratio"] == 1
True
>>> aero_press_params["water_ratio"] == 15
True
>>> aero_press_params["water"] == 135
True
>>> aero_press_coffee = calc_coffee(aero_press_params)
>>> aero_press_coffee == 9
True
>>> METHODS_MAP["aero-press"]["ratio_upper_limit"] == Fraction(1, 12)
True
>>> METHODS_MAP["aero-press"]["ratio_lower_limit"] == Fraction(1, 18)
True
>>> METHODS_MAP["aero-press"]["grind_upper_limit"] == 960
True
>>> METHODS_MAP["aero-press"]["grind_lower_limit"] == 320
True
>>> aero_press_params["grind"] == 640 # https://honestcoffeeguide.com/coffee-grind-size-chart/#aeropress
True
>>> METHODS_MAP["aero-press"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["aero-press"]["temperature_lower_limit"] == 90 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> aero_press_params["temperature"] == 93 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> aero_press_conc_params = load_method_params("aero-press-conc") # https://www.seattlecoffeegear.com/pages/product-resource/aero-press-product-resources
>>> aero_press_conc_params["coffee_ratio"] == 1
True
>>> aero_press_conc_params["water_ratio"] == 6
True
>>> aero_press_conc_params["water"] == 90
True
>>> aero_press_conc_coffee = calc_coffee(aero_press_conc_params)
>>> aero_press_conc_coffee == 15
True
>>> METHODS_MAP["aero-press-conc"]["ratio_upper_limit"] == Fraction(1, 5)
True
>>> METHODS_MAP["aero-press-conc"]["ratio_lower_limit"] == Fraction(1, 7)
True
>>> METHODS_MAP["aero-press-conc"]["grind_upper_limit"] == 960
True
>>> METHODS_MAP["aero-press-conc"]["grind_lower_limit"] == 320
True
>>> aero_press_conc_params["grind"] == 640 # https://honestcoffeeguide.com/coffee-grind-size-chart/#aeropress
True
>>> METHODS_MAP["aero-press-conc"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["aero-press-conc"]["temperature_lower_limit"] == 90 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> aero_press_conc_params["temperature"] == 93 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> aero_press_inv_params = load_method_params("aero-press-inv") # https://aeroprecipe.com/recipes/all-about-the-intervals
>>> aero_press_inv_params["coffee_ratio"] == 1
True
>>> aero_press_inv_params["water_ratio"] == 12
True
>>> aero_press_inv_params["water"] == 132
True
>>> aero_press_inv_coffee = calc_coffee(aero_press_inv_params)
>>> aero_press_inv_coffee == 11
True
>>> METHODS_MAP["aero-press-inv"]["ratio_upper_limit"] == Fraction(1, 10)
True
>>> METHODS_MAP["aero-press-inv"]["ratio_lower_limit"] == Fraction(1, 14)
True
>>> METHODS_MAP["aero-press-inv"]["grind_upper_limit"] == 960
True
>>> METHODS_MAP["aero-press-inv"]["grind_lower_limit"] == 320
True
>>> aero_press_inv_params["grind"] == 640 # https://honestcoffeeguide.com/coffee-grind-size-chart/#aeropress
True
>>> METHODS_MAP["aero-press-inv"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["aero-press-inv"]["temperature_lower_limit"] == 90 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> aero_press_inv_params["temperature"] == 93 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> steep_and_release_params = load_method_params("steep-and-release") # https://squaremileblog.com/brew-guide-clever-dripper/
>>> steep_and_release_params["coffee_ratio"] == 1
True
>>> steep_and_release_params["water_ratio"] == 16
True
>>> steep_and_release_params["water"] == 255
True
>>> steep_and_release_coffee = calc_coffee(steep_and_release_params)
>>> steep_and_release_coffee == 15.9375
True
>>> METHODS_MAP["steep-and-release"]["ratio_upper_limit"] == Fraction(1, 14)
True
>>> METHODS_MAP["steep-and-release"]["ratio_lower_limit"] == Fraction(1, 17)
True
>>> METHODS_MAP["steep-and-release"]["grind_upper_limit"] == 825
True
>>> METHODS_MAP["steep-and-release"]["grind_lower_limit"] == 450
True
>>> steep_and_release_params["grind"] == 638 # https://honestcoffeeguide.com/coffee-grind-size-chart/#steepandrelease
True
>>> METHODS_MAP["steep-and-release"]["temperature_upper_limit"] == 95 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> METHODS_MAP["steep-and-release"]["temperature_lower_limit"] == 85 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> steep_and_release_params["temperature"] == 93 # https://honestcoffeeguide.com/best-temperature-to-brew-coffee/
True
>>> custom_params = load_method_params("custom")
>>> custom_params["coffee_ratio"] == 1
True
>>> custom_params["water_ratio"] == 17
True
>>> custom_params["water"] == 240
True
>>> custom_params["coffee_unit"] == "g"
True
>>> custom_coffee_g = calc_coffee(custom_params)
>>> custom_coffee_g == 14.117647058823529
True
>>> custom_params["coffee_unit"] = "oz" # https://www.rapidtables.com/convert/weight/gram-to-ounce.html?x=14.117647058823529
>>> custom_coffee_oz = calc_coffee(custom_params)
>>> custom_coffee_oz == 0.4979853451764706
True
>>> custom_params["coffee_unit"] = "lb" # https://www.rapidtables.com/convert/weight/gram-to-pound.html?x=14.117647058823529
>>> custom_coffee_lb = calc_coffee(custom_params)
>>> custom_coffee_lb == 0.03112408407317647
True
>>> custom_params["coffee_unit"] = "mg" # https://www.rapidtables.com/convert/weight/gram-to-mg.html?x=14.117647058823529
>>> custom_coffee_mg = calc_coffee(custom_params)
>>> custom_coffee_mg == 14117.64705882353
True
>>> custom_params["coffee_unit"] = "kg" # https://www.rapidtables.com/convert/weight/gram-to-kg.html?x=14.117647058823529
>>> custom_coffee_kg = calc_coffee(custom_params)
>>> custom_coffee_kg == 0.01411764705882353
True
>>> custom_params["coffee_unit"] = "cb" # https://honestcoffeeguide.com/whole-bean-to-ground-coffee-ratio/
>>> custom_coffee_cb = calc_coffee(custom_params)
>>> custom_coffee_cb == 107
True
>>> custom_params["coffee_unit"] = "tbsp" # https://www.howmany.wiki/wv/
>>> custom_coffee_tbsp = calc_coffee(custom_params)
>>> custom_coffee_tbsp == 2.6157176470588235
True
>>> custom_params["coffee_unit"] = "tsp" # https://www.howmany.wiki/wv/
>>> custom_coffee_tsp = calc_coffee(custom_params)
>>> custom_coffee_tsp == 7.847294117647058
True
>>> custom_params["coffee_unit"] = "dsp" # https://www.howmany.wiki/wv/
>>> custom_coffee_dsp = calc_coffee(custom_params)
>>> custom_coffee_dsp == 3.923576470588235
True
>>> custom_params["coffee_unit"] = "cup" # https://www.howmany.wiki/wv/
>>> custom_coffee_cup = calc_coffee(custom_params)
>>> custom_coffee_cup == 0.16348235294117647
True
>>> convert_water(240, "g") == 240 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "g", True) == 240.0 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "kg") == 0.24 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "kg", True) == 240000.0 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "mg") == 240000 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "mg", True) == 0.24 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "oz") == 8.465750868 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "oz", True) == 6803.885549919067 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "lb") == 0.5291094292440001 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "lb", True) == 108862.16879993954 # https://www.calculator.net/weight-calculator.html
True
>>> convert_water(240, "ml") == 240 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "ml", True) == 240.0 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "l") == 0.24 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "l", True) == 240000.0 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "tbsp") == 16.230719999999998 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "tbsp", True) == 3548.8259300881296 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "tsp") == 48.6912 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "tsp", True) == 1182.9652996845425 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "dsp") == 24.3456 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "dsp", True) == 2365.930599369085 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "cup") == 1.014432 # https://www.howmany.wiki/wv/
True
>>> convert_water(240, "cup", True) == 56780.54320052995 # https://www.howmany.wiki/wv/
True
>>> round(convert_water(240, "pt"), 5) == 0.50721 # https://www.inchcalculator.com/convert/milliliter-to-pint/
True
>>> int(convert_water(240, "pt", True)) == 113562 # https://www.inchcalculator.com/convert/pint-to-milliliter/
True
>>> round(convert_water(240, "qt"), 4) == 0.2536 # https://www.inchcalculator.com/convert/milliliter-to-quart/
True
>>> int(convert_water(240, "qt", True)) == 227124 # https://www.inchcalculator.com/convert/quart-to-milliliter/
True
>>> round(convert_water(240, "fl oz"), 5) ==  8.11536 # https://www.inchcalculator.com/convert/milliliter-to-fluid-ounce/
True
>>> round(convert_water(240, "fl oz", True), 2) ==  7097.65 # https://www.inchcalculator.com/convert/fluid-ounce-to-milliliter/
True
>>> round(convert_water(240, "t oz"), 4) == 7.7162 # https://www.metric-conversions.org/weight/grams-to-troy-ounces.htm
True
>>> round(convert_water(240, "t oz", True), 1) == 7464.8 # https://www.metric-conversions.org/weight/troy-ounces-to-grams.htm
True
>>> round(convert_coffee(240, "t oz"), 4) == 7.7162 # https://www.metric-conversions.org/weight/grams-to-troy-ounces.htm
True
>>> round(convert_coffee(240, "gr"), 1) == 3703.8 # https://www.metric-conversions.org/weight/grams-to-grains.htm
True
>>> round(convert_water(240, "gr"), 1) == 3703.8 # https://www.metric-conversions.org/weight/grams-to-grains.htm
True
>>> round(convert_water(240, "gr", True), 3) == 15.552 # https://www.metric-conversions.org/weight/grains-to-grams.htm
True
>>> round(convert_coffee(240, "ct"), 1) == 1200.0 # https://www.metric-conversions.org/weight/grams-to-carats.htm
True
>>> round(convert_water(240, "ct"), 1) == 1200.0 # https://www.metric-conversions.org/weight/grams-to-carats.htm
True
>>> round(convert_water(240, "ct", True), 1) == 48.0 # https://www.metric-conversions.org/weight/carats-to-grams.htm
True
>>> round(convert_water(240, "cc"), 1) == 240.0 # https://www.metric-conversions.org/volume/milliliters-to-cubic-centimeters.htm
True
>>> round(convert_water(240, "cc", True), 1) == 240.0 # https://www.metric-conversions.org/volume/cubic-centimeters-to-milliliters.htm
True
>>> round(convert_water(240, "cl"), 1) == 24.0 # https://www.metric-conversions.org/volume/milliliters-to-centiliters.htm
True
>>> round(convert_water(240, "cl", True), 1) == 2400.0 # https://www.metric-conversions.org/volume/centiliters-to-milliliters.htm
True
>>> round(convert_coffee(240, "t lb"), 3) == 0.643 # https://www.metric-conversions.org/weight/grams-to-troy-pounds.htm
True
>>> round(convert_water(240, "t lb"), 3) == 0.643 # https://www.metric-conversions.org/weight/grams-to-troy-pounds.htm
True
>>> round(convert_water(240, "t lb", True), 1) == 89578.0 # https://www.metric-conversions.org/weight/troy-pounds-to-grams.htm
True
>>> round(convert_coffee(240, "dwt"), 2) == 154.32 # https://www.metric-conversions.org/weight/grams-to-pennyweights.htm
True
>>> round(convert_water(240, "dwt"), 2) == 154.32 # https://www.metric-conversions.org/weight/grams-to-pennyweights.htm
True
>>> round(convert_water(240, "dwt", True), 2) == 373.24 # https://www.metric-conversions.org/weight/pennyweights-to-grams.htm
True
>>> get_grind_type(100) == "Extra-Fine" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> get_grind_type(300) == "Fine" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> get_grind_type(500) == "Medium-Fine" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> get_grind_type(700) == "Medium" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> get_grind_type(900) == "Medium-Coarse" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> get_grind_type(1100) == "Coarse" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> get_grind_type(1300) == "Extra-Coarse" # https://honestcoffeeguide.com/coffee-grind-size-chart/
True
>>> convert_temperature(60, "C", "C")
60
>>> convert_temperature(60.0, "F", "F")
60
>>> convert_temperature(60, "K", "K")
60
>>> convert_temperature(62.2, "K", "K")
62.2
>>> convert_temperature(60, "C", "F") # https://www.inchcalculator.com/convert/temperature/
140
>>> convert_temperature(60, "C", "K") # https://www.inchcalculator.com/convert/temperature/
333.15
>>> convert_temperature(60, "F", "C") # https://www.inchcalculator.com/convert/temperature/
15.556
>>> convert_temperature(60, "F", "K") # https://www.inchcalculator.com/convert/temperature/
288.706
>>> convert_temperature(60, "K", "C") # https://www.inchcalculator.com/convert/temperature/
-213.15
>>> convert_temperature(60, "K", "F") # https://www.inchcalculator.com/convert/temperature/
-351.67
"""
