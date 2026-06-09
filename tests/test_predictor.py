import pytest

from diabetes_predictor.predictor import format_prediction, validate_features


def test_format_prediction_handles_binary_outputs():
    assert format_prediction(0) == "The person is not diabetic"
    assert format_prediction(1) == "The person is diabetic"


def test_validate_features_requires_eight_values():
    with pytest.raises(ValueError, match="8"):
        validate_features([1, 2, 3])


def test_validate_features_requires_numeric_values():
    with pytest.raises(TypeError, match="numeric"):
        validate_features([1, 2, 3, 4, 5, 6, 7, "bad"])
