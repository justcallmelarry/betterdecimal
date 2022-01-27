# `Better Decimal`
The power of `Decimal` with some quality of life improvements:
* Ability to enter floats: `Number(1.23)`
* Ability to do calculations with floats: `Number(1.5) * 1.5`
* Working rounding functionality: `round(Number(1.495), 2)`

Actually subclasses Decimal, so all other usecases can still be used as normal (for example `.quantize()` if you need )

## Installation with `pip`
Like you would install any other Python package, use `pip`, `poetry`, `pipenv` or your weapon of choice.
```
$ pip install number
```


## Usage and examples

#### Use-case
```
from number import Number

```
