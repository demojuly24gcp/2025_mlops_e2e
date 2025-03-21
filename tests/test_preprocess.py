
from unittest import TestCase
import pandas as pd
import numpy as np
from preprocess import (
    DataProcessor,
    feature_columns_names,
    label_column,
    feature_columns_dtype,
    label_column_dtype,
)

class TestPreProcess(TestCase):
    def test_process_data(self):
        expected_output = [
            [10, 1.34, -0.27, -1.22, 1.22, 1.41, -1.22, 0, 0, 0, 1],
            [7, -0.27, -1.07,  0, 0, -0.71, 1.22, 0, 1, 0, 0],
            [5, -1.07, 1.34, 1.22, -1.22, -0.71, 0, 0, 0, 1, 0]
        ]
        input_df = pd.DataFrame(
            [
                ["M", 5, 0.3, 1, 0.3, 2, 1, 0, 10],
                ["F", 3, 0.2, 2, 0.2, 1, 3, 0, 7],
                ["I", 2, 0.5, 3, 0.1, 1, 2, 0, 5]
            ],
            columns=feature_columns_names + [label_column],
        )
        input_df = input_df.astype(
            DataProcessor.merge_two_dicts(feature_columns_dtype, label_column_dtype)
        )
        data_processor = DataProcessor(input_df)
        output_data = data_processor.process()
        round_output = np.around(output_data, 2)
        np.testing.assert_array_equal(round_output, expected_output)

