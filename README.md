<div align="center">
<h1>MyCoffee: Brew Perfect Coffee Right from Your Terminal</h1>
<br/>
<a href="https://badge.fury.io/py/mycoffee"><img src="https://badge.fury.io/py/mycoffee.svg" alt="PyPI version" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
</div>			
				
## Overview	

<p align="justify">					
<strong>MyCoffee</strong> is a command-line tool for coffee enthusiasts who love brewing with precision. It helps you calculate the perfect coffee-to-water ratio for various brewing methods, ensuring you brew your ideal cup every time—right from your terminal.
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
		<td align="center"></td>
		<td align="center"></td>
		<td align="center"></td>
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 0.1](https://github.com/sepandhaghighi/mycoffee/archive/v0.1.zip) or [Latest Source](https://github.com/sepandhaghighi/mycoffee/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install mycoffee==0.1`						


## Usage

⚠️ You can use `mycoffee` or `python -m mycoffee` to run this program

### Version

```shell
> mycoffee --version

0.1
```

### Method

```shell
> mycoffee --method=v60
 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)



Method: `v60`

Cups: 1

Coffee: 14.52 gr

Water: 242 ml

Ratio: 3/50

Info: V60 method
```

* [Methods List](https://github.com/sepandhaghighi/mycoffee/blob/main/METHODS.md)
* `mycoffee --methods-list`

### Customize

```shell
> mycoffee --method=chemex --water=20 --cups=3 --coffee-ratio=2 --water-ratio=37

 __  __  _  _   ___  _____  ____  ____  ____  ____
(  \/  )( \/ ) / __)(  _  )( ___)( ___)( ___)( ___)
 )    (  \  / ( (__  )(_)(  )__)  )__)  )__)  )__)
(_/\/\_) (__)  \___)(_____)(__)  (__)  (____)(____)



Method: `chemex`

Cups: 3

Coffee: 1.081 gr

Water: 20.0 ml

Ratio: 2/37

Info: Chemex method
```

## Parameters

<table>
  <thead>
    <tr>
      <th align="center">Parameter</th>
      <th align="center">Description</th>
      <th align="center">Type</th>
      <th align="center">Required</th>
      <th align="center">Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code>--method</code></td>
      <td align="center">Specifies the coffee brewing method</td>
      <td align="center">String</td>
      <td align="center">No</td>
      <td align="center"><code>custom</code></td>
    </tr>
    <tr>
      <td align="center"><code>--water</code></td>
      <td align="center">Sets the amount of water in each cup</td>
      <td align="center">Float</td>
      <td align="center">No</td>
      <td align="center"><code>240</code></td>
    </tr>
    <tr>
      <td align="center"><code>--cups</code></td>
      <td align="center">Indicates the number of cups</td>
      <td align="center">Integer</td>
      <td align="center">No</td>
      <td align="center"><code>1</code></td>
    </tr>
    <tr>
      <td align="center"><code>--coffee-ratio</code></td>
      <td align="center">Coefficient for the coffee component in the ratio</td>
      <td align="center">Integer</td>
      <td align="center">No</td>
      <td align="center"><code>1</code></td>
    </tr>
    <tr>
      <td align="center"><code>--water-ratio</code></td>
      <td align="center">Coefficient for the water component in the ratio</td>
      <td align="center">Integer</td>
      <td align="center">No</td>
      <td align="center"><code>17</code></td>
    </tr>
    <tr>
      <td align="center"><code>--info</code></td>
      <td align="center">Provides information about the brewing method</td>
      <td align="center">String</td>
      <td align="center">No</td>
      <td align="center"><code>Custom brewing method</code></td>
    </tr>
  </tbody>
</table>




## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template
 			

## References

<blockquote>1- </blockquote>


## Show your support
								
<h3>Star this repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to our project</h3>	

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

