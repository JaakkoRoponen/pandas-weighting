import unittest

import pandas as pd
from pandas_weighting import weight

pd.Series.weight = weight
pd.DataFrame.weight = weight

df = pd.DataFrame({
    'val': [1, 2, 3, 4, 5, 6],
    'val2': [10, 20, 30, 40, 50, 60],
    'weights': [3, 2, 1, 1, 0, None],
})


class TestWeighting(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(
            df.val.mean(),
            (1 + 2 + 3 + 4 + 5 + 6) / 6)  # 3.5

    def test_weighted_mean(self):
        self.assertEqual(
            df.val.weight(df.weights).mean(),
            (3 * 1 + 2 * 2 + 3 + 4) / 7)  # 2.0

    def test_df_weighted_mean(self):
        means = df[['val', 'val2']].weight(df.weights).mean()
        self.assertEqual(
            means[1],
            (3 * 10 + 2 * 20 + 30 + 40) / 7)  # 20.0

    def test_value_counts(self):
        self.assertListEqual(
            df.val.weight(df.weights).value_counts().to_list(),
            [3, 2, 1, 1])

    def test_piping(self):
        try:
            df.val.pipe(weight, df.weights)
        except:  # noqa
            self.fail('piping raised exception unexpectedly')


if __name__ == '__main__':
    unittest.main()
