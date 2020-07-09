def weight(self, col):
    """
    Weight Pandas Dataframes

    Weighting is done by repeating rows as many times as defined in 'col'.
    This means that absolute weighting should be used instead of relative
    weighting, as it's not possible to repeat rows fractional times. Weights
    are rounded to integers, which might cause minor inaccuracies.

    If dataframe / weights are large, weighting should be applied to individual
    columns in turn, instead of the whole dataframe, as this might cause
    memory issues.

    Usage:
        df.col.pipe(weight, df.weights).describe()

        or by monkey patching Series/Dataframe:
            pd.Series.weight = weight
            pd.DataFrame.weight = weight

        df.col.weight(df.weights).describe()
    """

    try:
        weights = col[self.index]
    except TypeError:
        raise TypeError('Weights must be given as Pandas Series')
    try:
        weights = weights.round().fillna(0)
    except TypeError:
        raise TypeError('Weights must be numeric')
    weighted_index = self.index.repeat(weights)
    return self.reindex(weighted_index)
