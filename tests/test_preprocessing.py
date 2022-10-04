import pandas as pd

from modeltools.preprocessing import get_numerical_features


def test_get_numerical_features():
    """ Test the function only gets numeric fields and not strings"""

    df = pd.DataFrame({
        "numerical": [5],
        "categorical": ["rojo"]
    })

    assert get_numerical_features(df) == ['numerical']

    df = pd.DataFrame({
        "categorical": ["rojo"]
    })

    assert get_numerical_features(df) == []

