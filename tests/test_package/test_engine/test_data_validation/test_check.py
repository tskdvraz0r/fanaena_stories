import typing

import pytest

from packages.engine.data_validation.check import Check


class TestCheck:

    @staticmethod
    @pytest.mark.parametrize(
        ["test_value", "test_expected_type"],
        [
            ("string", str),
            (1, int),
            (1.0, float),
            ([], list),
            ((), tuple),
            ({}, dict)
        ]
    )
    def test_value_type(
            test_value: typing.Any,
            test_expected_type: typing.Any
    ) -> None:
        Check.value_type(
            value=test_value,
            expected_type=test_expected_type
        )

    @staticmethod
    @pytest.mark.parametrize(
        ["test_value", "test_available_values"],
        [
            (True, [True, False]),
            (False, [0, 1]),
            ("string", ["test", "case", "based", "on", "string"]),
            ("string", "test case based on string"),
            (13, [1, 3, 5, 7, 9, 11, 13]),
            (13.0, [1, 3, 5, 7, 9, 11, 13]),
            (13.0, [1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0]),
        ]
    )
    def test_value_is_available(
            test_value: typing.Any,
            test_available_values: typing.Any
    ) -> None:
        Check.value_is_available(
            value=test_value,
            available_values=test_available_values
        )
