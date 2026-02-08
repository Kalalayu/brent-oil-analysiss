import unittest
import pandas as pd
import numpy as np
from src.utils import adf_test

class TestUtils(unittest.TestCase):
    def test_adf_test_stationary(self):
        # Generate longer stationary series
        np.random.seed(42)
        data = pd.Series(np.random.normal(0, 1, 100))  # 100 points
        result = adf_test(data)
        self.assertIn('ADF Statistic', result)
        self.assertIn('p-value', result)

if __name__ == "__main__":
    unittest.main()
