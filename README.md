# Weight Pandas Dataframes

pandas-weighting enables general level weighting (similar to spss) of
dataframes. This makes it possible to calculate weighted means, frequencies
etc. statistical figures without the need to write separate functions for
applying weighting.

Weighting is done by repeating rows as many times as defined in 'weight'
column. There are a few drawbacks related to weighting data this way:

* Absolute weighting (all weights are above one, the sum of the weighted cases
is more than sum of the unweighted cases) must be used instead of relative
weighting (some weights are below zero, the sum of the weighted cases is the
same as the sum of the unweighted cases), as it's not possible to repeat rows
fractional times.

* Weights are rounded to integers, which might cause inaccuracies, especially if
the weights are small.

* If dataframe / weights are large, weighting should be applied to individual
columns in turns, instead of the whole dataframe, as this might cause
memory issues.

## Usage

```python
from pandas_weighting.func import weight

df.col.pipe(weight, df.weights).describe()
```

or by monkey patching Series/Dataframe:

```python
pd.Series.weight = weight
pd.DataFrame.weight = weight

df.col.weight(df.weights).describe()
```

## Example

```python
import pandas as pd
from pandas_weighting.func import weight

pd.Series.weight = weight
pd.DataFrame.weight = weight

df = pd.DataFrame({
    'val': [1, 2, 3, 4, 5, 6],
    'weights': [3, 2, 1, 1, 0, None],
})

# mean 3.5 =(1+2+3+4+5+6)/6
df.val.mean()

# weighted mean 2.0 =(3*1+2*2+1*3+1*4)/(3+2+1+1)
df.val.weight(df.weights).mean()
```
