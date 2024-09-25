# -*- coding: utf-8 -*-
"""
>>> from mycoffee.functions import *
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
>>> steep_and_release_params = load_method_params("steep-and-release") # https://squaremileblog.com/brew-guide-clever-dripper/
>>> steep_and_release_params["coffee_ratio"] == 1
True
>>> steep_and_release_params["water_ratio"] == 16
True
>>> steep_and_release_params["water"] == 255
True
>>> steep_and_release_coffee = calc_coffee(steep_and_release_params)
>>> steep_and_release_coffee == 15.937
True
"""
