<div align="center">
<img src="https://github.com/sepandhaghighi/mycoffee/raw/main/otherfiles/logo.png" width="500">
<h1>MyCoffee: Brew Perfect Coffee Right from Your Terminal</h1>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/mycoffee"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/mycoffee"></a>
<a href="https://badge.fury.io/py/mycoffee"><img src="https://badge.fury.io/py/mycoffee.svg" alt="PyPI version"></a>
<a href="https://codecov.io/gh/sepandhaghighi/mycoffee" ><img src="https://codecov.io/gh/sepandhaghighi/mycoffee/graph/badge.svg?token=ZelznFDSPA"></a>
</div>			
				
## Overview	

<p align="justify">					
<strong>MyCoffee</strong> is a command-line tool for coffee enthusiasts who love brewing with precision. It helps you calculate the perfect coffee-to-water ratio for various brewing methods, ensuring you brew your ideal cup every time-right from your terminal.
</p>

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/mycoffee"><img src="http://pepy.tech/badge/mycoffee"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/mycoffee"><img src="https://img.shields.io/github/stars/sepandhaghighi/mycoffee.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/mycoffee/actions/workflows/test.yml/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/mycoffee/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/mycoffee"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/mycoffee/badge" alt="CodeFactor"></a></td>
		<td align="center"><a href="https://codebeat.co/projects/github-com-sepandhaghighi-mycoffee-main"><img alt="codebeat badge" src="https://codebeat.co/badges/8cb2671b-7640-4ac7-bb3e-823bb26a2db2"></a></td>
		<td align="center"><a href="https://app.codacy.com/gh/sepandhaghighi/mycoffee/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ac0a8041879042d4a7925272ea3f7ba5"></a></td>
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 1.9](https://github.com/sepandhaghighi/mycoffee/archive/v1.9.zip) or [Latest Source](https://github.com/sepandhaghighi/mycoffee/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install mycoffee==1.9`						


## Usage

ℹ️ You can use `mycoffee` or `python -m mycoffee` to run this program

### Version

```console
> mycoffee --version

1.9
```

### Info

```console
> mycoffee --info

 __  __          ____          __   __
|  \/  | _   _  / ___|  ___   / _| / _|  ___   ___
| |\/| || | | || |     / _ \ | |_ | |_  / _ \ / _ \
| |  | || |_| || |___ | (_) ||  _||  _||  __/|  __/
|_|  |_| \__, | \____| \___/ |_|  |_|   \___| \___|
         |___/

__     __    _      ___
\ \   / / _ / |    / _ \
 \ \ / / (_)| |   | (_) |
  \ V /   _ | | _  \__, |
   \_/   (_)|_|(_)   /_/



MyCoffee is a command-line tool for coffee enthusiasts who love brewing with precision.
It helps you calculate the perfect coffee-to-water ratio for various brewing methods,
ensuring you brew your ideal cup every time-right from your terminal.

Repo : https://github.com/sepandhaghighi/mycoffee
```


### Method

```console
> mycoffee --method=v60
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)



Mode: Water --> Coffee

Method: `v60`

Cups: 1

Coffee:

    - Cup:   15 g
    - Total: 15 g

Water:

    - Cup: 250 g
    - Total: 250 g

Ratio: 3/50 (0.06)

Strength: Medium

Grind: 550 um (Medium-Fine)

Temperature: 91 C

Message: V60 method
```

* [Methods List](https://github.com/sepandhaghighi/mycoffee/blob/main/METHODS.md)
* `mycoffee --methods-list`

### Mode

#### Water to Coffee
```console
> mycoffee --method=v60 --mode="water-to-coffee" --water=300
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)



Mode: Water --> Coffee

Method: `v60`

Cups: 1

Coffee:

    - Cup:   18 g
    - Total: 18 g

Water:

    - Cup: 300 g
    - Total: 300 g

Ratio: 3/50 (0.06)

Strength: Medium

Grind: 550 um (Medium-Fine)

Temperature: 91 C

Message: V60 method
```

#### Coffee to Water
```console
> mycoffee --method=v60 --mode="coffee-to-water" --coffee=12
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)



Mode: Coffee --> Water

Method: `v60`

Cups: 1

Coffee:

    - Cup:   12 g
    - Total: 12 g

Water:

    - Cup: 200 g
    - Total: 200 g

Ratio: 3/50 (0.06)

Strength: Medium

Grind: 550 um (Medium-Fine)

Temperature: 91 C

Message: V60 method
```

### Customize

ℹ️ You can run `mycoffee --coffee-units-list` to view the supported coffee units

ℹ️ You can run `mycoffee --water-units-list` to view the supported water units

```console
> mycoffee --method=chemex --water=20 --cups=3 --coffee-ratio=2 --water-ratio=37 --coffee-unit="t oz" --water-unit="fl oz" --grind=750 --temperature=88

 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)



Mode: Water --> Coffee

Method: `chemex`

Cups: 3

Coffee:

    - Cup:   1.028 t oz
    - Total: 3.084 t oz

Water:

    - Cup: 20 fl oz
    - Total: 60 fl oz

Ratio: 2/37 (0.054)

Strength: Medium

Grind: 750 um (Medium)

Temperature: 88 C

Message: Chemex method
```

### Save

ℹ️ File format valid choices: [`text`, `json`]

ℹ️ The default file format is `text`

```console
> mycoffee --method=chemex --water=20 --cups=3 --coffee-ratio=2 --water-ratio=37 --save-path="profile1.txt" --save-format="text"
```

## Parameters

<table>
  <thead>
    <tr>
      <th align="center">Parameter</th>
      <th align="center">Description</th>
      <th align="center">Type</th>
      <th align="center">Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code>--mode</code></td>
      <td align="center">Specifies the conversion mode</td>
      <td align="center">String</td>
      <td align="center"><code>water-to-coffee</code></td>
    </tr>
    <tr>
      <td align="center"><code>--method</code></td>
      <td align="center">Specifies the coffee brewing method</td>
      <td align="center">String</td>
      <td align="center"><code>custom</code></td>
    </tr>
    <tr>
      <td align="center"><code>--water</code></td>
      <td align="center">Sets the amount of water in each cup</td>
      <td align="center">Positive float</td>
      <td align="center"><code>240</code></td>
    </tr>
    <tr>
      <td align="center"><code>--coffee</code></td>
      <td align="center">Sets the amount of coffee in each cup</td>
      <td align="center">Positive float</td>
      <td align="center"><code>14.118</code></td>
    </tr>
    <tr>
      <td align="center"><code>--cups</code></td>
      <td align="center">Indicates the number of cups</td>
      <td align="center">Positive integer</td>
      <td align="center"><code>1</code></td>
    </tr>
    <tr>
      <td align="center"><code>--grind</code></td>
      <td align="center">Grind size (um)</td>
      <td align="center">Positive integer</td>
      <td align="center"><code>700</code></td>
    </tr>
    <tr>
      <td align="center"><code>--temperature</code></td>
      <td align="center">Brewing temperature</td>
      <td align="center">Float</td>
      <td align="center"><code>90</code></td>
    </tr>
    <tr>
      <td align="center"><code>--coffee-ratio</code></td>
      <td align="center">Coefficient for the coffee component in the ratio</td>
      <td align="center">Positive float</td>
      <td align="center"><code>1</code></td>
    </tr>
    <tr>
      <td align="center"><code>--water-ratio</code></td>
      <td align="center">Coefficient for the water component in the ratio</td>
      <td align="center">Positive float</td>
      <td align="center"><code>17</code></td>
    </tr>
    <tr>
      <td align="center"><code>--message</code></td>
      <td align="center">Extra information about the brewing method</td>
      <td align="center">String</td>
      <td align="center"><code>Custom brewing method</code></td>
    </tr>
    <tr>
      <td align="center"><code>--digits</code></td>
      <td align="center">Number of digits up to which the result is rounded</td>
      <td align="center">Integer</td>
      <td align="center"><code>3</code></td>
    </tr>
    <tr>
      <td align="center"><code>--coffee-unit</code></td>
      <td align="center">Coffee unit</td>
      <td align="center">String</td>
      <td align="center"><code>g</code></td>
    </tr>
    <tr>
      <td align="center"><code>--water-unit</code></td>
      <td align="center">Water unit</td>
      <td align="center">String</td>
      <td align="center"><code>g</code></td>
    </tr>
    <tr>
      <td align="center"><code>--temperature-unit</code></td>
      <td align="center">Temperature unit</td>
      <td align="center">String</td>
      <td align="center"><code>C</code></td>
    </tr>
  </tbody>
</table>



## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template
 			

## References

<blockquote>1- <a href="https://honestcoffeeguide.com/coffee-to-water-ratio-calculator/">Coffee to water ratio calculator</a></blockquote>
<blockquote>2- <a href="https://www.origincoffee.co.uk/blogs/journal/brewing-at-home-v60">V60 Brew Guide</a></blockquote>
<blockquote>3- <a href="https://unionroasted.com/blogs/brewing-guides/chemex-pour-over">How to Brew Coffee with a Chemex</a></blockquote>
<blockquote>4- <a href="https://www.illy.com/en-us/coffee/coffee-preparation/how-to-use-a-french-press">Using French press for perfect coffee</a></blockquote>
<blockquote>5- <a href="https://www.haymancoffee.com/blogs/coffee-blog/how-to-brew-the-perfect-cup-of-siphon-coffee">How to Brew the Perfect Cup of Siphon Coffee</a></blockquote>
<blockquote>6- <a href="https://home.lamarzoccousa.com/using-espresso-brew-ratios/">Using Espresso Brew Ratios</a></blockquote>
<blockquote>7- <a href="https://www.nicolebattefeld.com/post/best-recipes-2022">My Best Coffee Recipes of 2022</a></blockquote>
<blockquote>8- <a href="https://wonderstate.com/pages/auto-drip">Auto Drip Brewing Guide</a></blockquote>
<blockquote>9- <a href="https://counterculturecoffee.com/blogs/counter-culture-coffee/guide-to-cold-brew">Guide To Cold Brew</a></blockquote>
<blockquote>10- <a href="https://www.thespruceeats.com/cold-brew-concentrate-recipe-5197494">Cold Brew Concentrate Recipe</a></blockquote>
<blockquote>11- <a href="https://bakedbrewedbeautiful.com/how-to-make-coffee-in-moka-pot/">How to Make Coffee in a Moka Pot</a></blockquote>
<blockquote>12- <a href="https://www.drinktrade.com/blogs/education/how-to-make-turkish-coffee">How to Make Turkish Coffee at Home</a></blockquote>
<blockquote>13- <a href="https://www.horshamcoffeeroaster.co.uk/pages/how-to-cup-coffee">How to Cup Coffee</a></blockquote>
<blockquote>14- <a href="https://aeroprecipe.com/recipes/tetsu-kasuya-aeropress-recipe">Tetsu Kasuya AeroPress Recipe</a></blockquote>
<blockquote>15- <a href="https://aeroprecipe.com/recipes/all-about-the-intervals">All about the intervals</a></blockquote>
<blockquote>16- <a href="https://squaremileblog.com/brew-guide-clever-dripper/">Clever Dripper; Square Mile Coffee</a></blockquote>
<blockquote>17- <a href="https://www.seattlecoffeegear.com/pages/product-resource/aero-press-product-resources">AeroPress Product User Manuals</a></blockquote>
<blockquote>18- <a href="https://www.rapidtables.com/convert/weight/index.html">RapidTables - Weight Converter</a></blockquote>
<blockquote>19- <a href="https://honestcoffeeguide.com/whole-bean-to-ground-coffee-ratio/">Whole bean to ground coffee calculator</a></blockquote>
<blockquote>20- <a href="https://www.howmany.wiki/wv/">Weight to Volume Converter for Recipes</a></blockquote>
<blockquote>21- <a href="https://chamberlaincoffee.com/blogs/inspiration/how-much-coffee-per-cup-this-is-how-you-get-it-right">How Much Coffee per Cup?</a></blockquote>
<blockquote>22- <a href="https://www.calculator.net/weight-calculator.html">Weight Calculator</a></blockquote>
<blockquote>23- <a href="https://www.inchcalculator.com/convert/volume/">Volume Conversion Calculator - Inch Calculator</a></blockquote>
<blockquote>24- <a href="https://www.metric-conversions.org/">Metric Conversion Charts and Calculators</a></blockquote>
<blockquote>25- <a href="https://honestcoffeeguide.com/coffee-grind-size-chart">Coffee grind size chart</a></blockquote>
<blockquote>26- <a href="https://honestcoffeeguide.com/best-temperature-to-brew-coffee/">The best temperature to brew coffee</a></blockquote>
<blockquote>27- <a href="https://unionroasted.com/blogs/brewing-guides/syphon">How to Brew Coffee with a Syphon</a></blockquote>
<blockquote>28- <a href="https://counterculturecoffee.com/blogs/counter-culture-coffee/guide-to-home-coffee-makers">Guide To Home Coffee Makers</a></blockquote>
<blockquote>29- <a href="https://perfectdailygrind.com/2021/07/can-you-brew-coffee-with-warm-water">Can you brew coffee with warm water?</a></blockquote>
<blockquote>30- <a href="https://ravecoffee.co.uk/blogs/news/how-to-brew-coffee-using-an-ibrik-cezve-for-turkish-style-coffee">How to Brew Coffee Using a Cezve</a></blockquote>
<blockquote>31- <a href="https://www.diffordsguide.com/g/1113/coffee/cupping">Coffee cupping</a></blockquote>
<blockquote>32- <a href="https://sablebrew.com/blogs/news/the-latest-method-to-brew-coffee-with-your-clever-dripper">The Latest Method to Brew Coffee with Your Clever Dripper</a></blockquote>
<blockquote>33- <a href="https://cafely.com/blogs/coffee-brew-guide/vietnamese-phin-drip">How to Make Vietnamese Coffee with Traditional Phin Drip Filter</a></blockquote>

## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>

