from decimal import Decimal
from typing import Any

import pytest

from number import Number


@pytest.mark.parametrize(
    "input_data,expected_data",
    [
        (0, Number("0")),
        ("1.2345", Number(1.2345)),
        (1.2345, Number(1.2345)),
        ("1", Number(1)),
        (".01", Number(0.01)),
        (True, Number(1)),
        (Decimal("1.2345"), Number(1.2345)),
        (-1.23, Number(-1.23)),
    ],
)
def test_number_initiations(input_data: Any, expected_data: Number) -> None:
    num = Number(input_data)

    assert num == expected_data


def test_number_add() -> None:
    num = Number(5.0)

    # add Number + Number
    testnum = num + Number(1)
    assert testnum == Number(6)
    assert isinstance(testnum, Number)

    # add Number + Decimal
    testnum = num + Decimal("1.5")
    assert testnum == Number(6.5)
    assert isinstance(testnum, Number)

    # add float + Number
    testnum = 1.5 + num
    assert testnum == Number(6.5)
    assert isinstance(testnum, Number)


def test_number_sub() -> None:
    num = Number(5.0)

    # sub Number - Number
    testnum = num - Number(1)
    assert testnum == Number(4)
    assert isinstance(testnum, Number)

    # sub Number - Decimal
    testnum = num - Decimal("1.5")
    assert testnum == Number(3.5)
    assert isinstance(testnum, Number)

    # sub float - Number
    testnum = 1.5 - num
    assert testnum == Number(-3.5)
    assert isinstance(testnum, Number)


def test_number_div() -> None:
    num = Number(5.0)

    # div Number by Number
    testnum = Number(10) / num

    assert testnum == Number(2)
    assert isinstance(testnum, Number)

    # div Number by int
    testnum = num / 2

    assert testnum == Number(2.5)
    assert isinstance(testnum, Number)

    # div int by Number
    testnum = 10 / num

    assert testnum == Number(2)
    assert isinstance(testnum, Number)


def test_number_mul() -> None:
    num = Number(5.0)

    # mul Number by Number
    testnum = Number(10) * num

    assert testnum == Number(50)
    assert isinstance(testnum, Number)

    # mul Number by float
    testnum = num * 1.5

    assert testnum == Number(7.5)
    assert isinstance(testnum, Number)

    # mul Decimal by Number
    testnum = Decimal("1.5") * num

    assert testnum == Number(7.5)
    assert isinstance(testnum, Number)


def test_number_pow() -> None:
    num = Number(5.0)

    # pow Number by Number
    testnum = Number(10) ** num

    assert testnum == Decimal("10") ** Decimal("5")
    assert isinstance(testnum, Number)

    # pow Number by float
    testnum = num ** 1.5

    assert testnum == Decimal("5") ** Decimal("1.5")
    assert isinstance(testnum, Number)

    # pow Decimal by Number
    testnum = Decimal("1.5") ** num

    assert testnum == Decimal("1.5") ** Decimal("5")
    assert isinstance(testnum, Number)


def test_number_operators() -> None:
    num = Number(5.0)

    # greater/less than
    assert num > Number("1")
    assert num < 13.2
    assert Decimal("13.2") > num
    assert 1 < num

    # mod
    testnum = num % 2
    assert testnum == 1
    assert isinstance(testnum, Number)

    testnum = num % 5
    assert not testnum
    assert isinstance(testnum, Number)

    # neg
    testnum = -num
    assert testnum == Number(-5)
    assert isinstance(testnum, Number)

    # pos
    testnum = +num
    assert testnum == Number(5)
    assert isinstance(testnum, Number)

    # abs
    testnum = abs(num)
    assert testnum == Number(5)
    assert isinstance(testnum, Number)

    testnum = -num
    assert abs(testnum) == Number(5)
    assert isinstance(testnum, Number)


def test_number_rounding() -> None:
    # round
    num = Number(1.2345)

    testnum = round(num)
    assert testnum == 1
    assert isinstance(testnum, Number)

    testnum = round(num, 2)
    assert testnum == Number(1.23)
    assert isinstance(testnum, Number)

    testnum = round(num, 3)
    assert testnum == Number(1.235)
    assert isinstance(testnum, Number)
