"""
This module contains helpers for data processing.
"""

import numpay as np


def get_numerical_features(df):
    return df.select_dtypes(include=[np.number]).columns
