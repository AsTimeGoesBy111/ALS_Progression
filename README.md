ALS (Amyotrophic Lateral Sclerosis) is a fatal motor neuron disease with substantial heterogeneity in genomics as well as clinical features. ALS is usually very progressive with very short survival after onset. Here we applied machine learning approaches to predict rate of progression based on available clinical data for ~5000 patients.


##     Pipeline 
##  Data Format

1. Data introduction
We have ~5000000 lines of data about all features including demographics, clinical trial as well as lab test results for ~5000 ALS patients provided by PRO-ACT(Pooled Resource Open-Access ALS Clinical Trial Database).

Have a look at data?

89	144	Demographics	B17A1C73-0A2B-4091-842C-D5841EF339FD	1205	Sex	Male
329	144	Demographics	704CA13F-C1FA-49EC-A3BB-E6B00FA075FA	1205	Sex	Female
329	144	Demographics	704CA13F-C1FA-49EC-A3BB-E6B00FA075FA	1206	Race - American Indian/Alaska Native	
329	144	Demographics	704CA13F-C1FA-49EC-A3BB-E6B00FA075FA	1207	Race - Asian	
329	145	ALSFRS(R)	8F97FE2C-5B03-4491-AA3E-52883C47FCE6	1225	ALSFRS Delta	189
329	145	ALSFRS(R)	8F97FE2C-5B03-4491-AA3E-52883C47FCE6	1228	ALSFRS Total	25
329	145	ALSFRS(R)	31D06255-09B0-4265-9477-D872DC6DD78A	1225	ALSFRS Delta	212
329	145	ALSFRS(R)	31D06255-09B0-4265-9477-D872DC6DD78A	1228	ALSFRS Total	30
329	146	Laboratory Data	1150FF83-DA3B-436E-B444-D1CA2A22E08C	1234	Laboratory Delta	0
329	146	Laboratory Data	1150FF83-DA3B-436E-B444-D1CA2A22E08C	1250	Test Name	Sodium
329	146	Laboratory Data	1150FF83-DA3B-436E-B444-D1CA2A22E08C	1251	Test Result	138
329	146	Laboratory Data	1150FF83-DA3B-436E-B444-D1CA2A22E08C	1252	Test Unit	mmol/L


2. Feature engineering and Data cleaning
Static feature (show code)
Dynamic feature
Progression Rate(dong tu)

character features into numeric features
Merge df
Remove features with too many NaN
Then fill lin remaining NaN with median of that feature

(5372*134)


3. Random Forest training
Feature correlation
Random Forest train--Important features
cross validate and test results






# D3: Data-Driven Documents

<a href="https://d3js.org"><img src="https://d3js.org/logo.svg" align="left" hspace="10" vspace="6"></a>

**D3** (or **D3.js**) is a JavaScript library for visualizing data using web standards. D3 helps you bring data to life using SVG, Canvas and HTML. D3 combines powerful visualization and interaction techniques with a data-driven approach to DOM manipulation, giving you the full capabilities of modern browsers and the freedom to design the right visual interface for your data.

## Resources

* [API Reference](https://github.com/d3/d3/blob/master/API.md)
* [Release Notes](https://github.com/d3/d3/releases)
* [Gallery](https://github.com/d3/d3/wiki/Gallery)
* [Examples](http://bl.ocks.org/mbostock)
* [Wiki](https://github.com/d3/d3/wiki)

## Installing

If you use npm, `npm install d3`. Otherwise, download the [latest release](https://github.com/d3/d3/releases/latest). The released bundle supports anonymous AMD, CommonJS, and vanilla environments. You can load directly from [d3js.org](https://d3js.org), [CDNJS](https://cdnjs.com/libraries/d3), or [unpkg](https://unpkg.com/d3/). For example:

```html
<script src="https://d3js.org/d3.v4.js"></script>
```

For the minified version:

```html
<script src="https://d3js.org/d3.v4.min.js"></script>
```

You can also use the standalone D3 microlibraries. For example, [d3-selection](https://github.com/d3/d3-selection):

```html
<script src="https://d3js.org/d3-selection.v1.js"></script>
```

D3 is written using [ES2015 modules](http://www.2ality.com/2014/09/es6-modules-final.html). Create a [custom bundle using Rollup](http://bl.ocks.org/mbostock/bb09af4c39c79cffcde4), Webpack, or your preferred bundler. To import D3 into an ES2015 application, either import specific symbols from specific D3 modules:

```js
import {scaleLinear} from "d3-scale";
```

Or import everything into a namespace (here, `d3`):

```js
import * as d3 from "d3";
```

In Node:

```js
var d3 = require("d3");
```

You can also require individual modules and combine them into a `d3` object using [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign):

```js
var d3 = Object.assign({}, require("d3-format"), require("d3-geo"), require("d3-geo-projection"));
```


