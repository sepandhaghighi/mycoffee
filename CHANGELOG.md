# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.2] - 2025-01-13
### Added
- 2 new water units
	1. Troy Pounds (`t lb`)
	2. Pennyweight (`dwt`)
- 2 new coffee units
	1. Troy Pounds (`t lb`)
	2. Pennyweight (`dwt`)
- `--grind` argument
- Grind upper limit
- Grind lower limit
- `check_grind_limits` function
### Changed
- `README.md` updated
- `METHODS.md` updated
## [1.1] - 2025-01-02
### Added
- 5 new water units
	1. Troy Ounce (`t oz`)
	2. Grain (`gr`)
	3. Carats (`ct`)
	4. Cubic Centimeters (`cc`)
	5. Centiliters (`cl`)
- 3 new coffee units
	1. Troy Ounce (`t oz`)
	2. Grain (`gr`)
	3. Carats (`ct`)
### Changed
- `README.md` updated
## [1.0] - 2024-12-17
### Added
- 3 new water units
	1. Pint (`pt`)
	2. Quart (`qt`)
	3. Fluid Ounce (`fl oz`)
### Changed
- `README.md` updated
## [0.9] - 2024-12-06
### Added
- 4 new water units
	1. Tablespoon (`tbsp`)
	2. Teaspoon (`tsp`)
	3. Dessertspoon (`dsp`)
	4. Cup (`cup`)
## [0.8] - 2024-11-29
### Added
- 1 new coffee unit
	1. Cup (`cup`)
- 6 new water units
	1. Milliliter (`ml`)
	2. Liter (`l`)
	3. Ounce (`oz`)
	4. Pound (`lb`)
	5. Milligram (`mg`)
	6. Kilogram (`kg`)
- `convert_water` function
- `show_water_units_list` function
- `--water-unit` argument
### Changed
- Test system modified
- `README.md` updated
## [0.7] - 2024-11-21
### Added
- 4 new coffee units
	1. Coffee beans (`cb`)
	2. Tablespoon (`tbsp`)
	3. Teaspoon (`tsp`)
	4. Dessertspoon (`dsp`)
- `convert_coffee` function
### Changed
- GitHub actions are limited to the `dev` and `main` branches
## [0.6] - 2024-10-18
### Added
- `show_coffee_units_list` function
- `--coffee-unit` argument
### Changed
- Test system modified
- Cups bug fixed
- `calc_coffee` function updated
- `README.md` updated
- `Python 3.13` added to `test.yml`
## [0.5] - 2024-10-08
### Added
- Ratio upper limit
- Ratio lower limit
- `check_ratio_limits` function
### Changed
- Test system modified
- `print_message` function renamed to `print_result`
## [0.4] - 2024-10-01
### Added
- 4 new methods
	1. AeroPress standard
	2. AeroPress concentrate
	3. AeroPress inverted
	4. Steep-and-release
- `--digits` argument
### Changed
- `README.md` updated
- Test system modified
- `filter_params` function updated
## [0.3] - 2024-09-24
### Added
- Logo
- 4 new methods
	1. Ristretto
	2. Lungo
	3. Turkish
	4. Cupping
## [0.2] - 2024-09-17
### Added
- 5 new methods
	1. Pour-over
	2. Auto drip
	3. Cold brew
	4. Cold brew concentrate
	5. Moka pot
- `is_int` function
- `filter_params` function
### Changed
- `README.md` updated
- `--coffee-ratio` type changed from `int` to `float`
- `--water-ratio` type changed from `int` to `float`
- `coffee_calc` function renamed to `calc_coffee`
- `print_message` function updated
- Test system modified
## [0.1] - 2024-09-02
### Added
- 6 new methods
	1. V60
	2. Espresso
	3. Chemex
	4. French-press
	5. Siphon
	6. Custom

[Unreleased]: https://github.com/sepandhaghighi/mycoffee/compare/v1.2...dev
[1.2]: https://github.com/sepandhaghighi/mycoffee/compare/v1.1...v1.2
[1.1]: https://github.com/sepandhaghighi/mycoffee/compare/v1.0...v1.1
[1.0]: https://github.com/sepandhaghighi/mycoffee/compare/v0.9...v1.0
[0.9]: https://github.com/sepandhaghighi/mycoffee/compare/v0.8...v0.9
[0.8]: https://github.com/sepandhaghighi/mycoffee/compare/v0.7...v0.8
[0.7]: https://github.com/sepandhaghighi/mycoffee/compare/v0.6...v0.7
[0.6]: https://github.com/sepandhaghighi/mycoffee/compare/v0.5...v0.6
[0.5]: https://github.com/sepandhaghighi/mycoffee/compare/v0.4...v0.5
[0.4]: https://github.com/sepandhaghighi/mycoffee/compare/v0.3...v0.4
[0.3]: https://github.com/sepandhaghighi/mycoffee/compare/v0.2...v0.3
[0.2]: https://github.com/sepandhaghighi/mycoffee/compare/v0.1...v0.2
[0.1]: https://github.com/sepandhaghighi/mycoffee/compare/c2d0bb4...v0.1



