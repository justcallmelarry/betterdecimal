from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from typing import Any, Tuple, Type, Union


class Number(Decimal):
    def __new__(cls: Type[Number], value: Union[int, str, float, Decimal] = "0") -> Number:
        if isinstance(value, float):
            return Decimal.__new__(cls, str(value))

        return Decimal.__new__(cls, value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"

    def __add__(self, other: Union[int, float, Decimal]) -> Number:
        if isinstance(other, float):
            return self.__class__(Decimal.__add__(self, Decimal(str(other))))

        return self.__class__(Decimal.__add__(self, other))

    def __radd__(self, other: Union[int, float, Decimal]) -> Number:
        return self.__add__(other)

    def __mul__(self, other: Union[int, float, Decimal]) -> Number:
        if isinstance(other, float):
            return self.__class__(Decimal.__mul__(self, Decimal(str(other))))

        return self.__class__(Decimal.__mul__(self, other))

    def __rmul__(self, other: Union[int, float, Decimal]) -> Number:
        return self.__mul__(other)

    def __sub__(self, other: Union[int, float, Decimal]) -> Number:
        if isinstance(other, float):
            return self.__class__(Decimal.__sub__(self, Decimal(str(other))))

        return self.__class__(Decimal.__sub__(self, other))

    def __rsub__(self, other: Union[int, float, Decimal]) -> Number:
        number_other = Number(other)

        return self.__class__(number_other - self)

    def __truediv__(self, other: Union[int, float, Decimal]) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__truediv__(self, number_other))

    def __rtruediv__(self, other: Union[int, float, Decimal]) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__rtruediv__(self, number_other))

    def __floordiv__(self, other: Union[int, float, Decimal]) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__floordiv__(self, number_other))

    def __rfloordiv__(self, other: Union[int, float, Decimal]) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__rfloordiv__(self, number_other))

    def __mod__(self, other: Union[int, float, Decimal]) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__mod__(self, number_other))

    def __divmod__(self, other: Union[int, float, Decimal]) -> Tuple[Number, Number]:
        number_other = Number(other)

        result = Decimal.__divmod__(self, number_other)

        return self.__class__(result[0]), self.__class__(result[1])

    def __pow__(self, other: Union[int, float, Decimal], mod: Any = None) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__pow__(self, number_other))

    def __rpow__(self, other: Union[int, float, Decimal], mod: Any = None) -> Number:
        number_other = Number(other)

        return self.__class__(Decimal.__rpow__(self, number_other))

    def __round__(self, ndigits: int = 0) -> Any:
        """
        Returning `Any` due to Decimal supertype
        """
        if ndigits > 0:
            decimal_format = "." + "0" * (ndigits - 1) + "1"
        else:
            decimal_format = "1"

        return self.__class__(self.quantize(Decimal(decimal_format), rounding=ROUND_HALF_UP))

    def __neg__(self) -> Number:
        return self.__class__(Decimal.__neg__(self))

    def __pos__(self) -> Number:
        return self.__class__(Decimal.__pos__(self))

    def __abs__(self) -> Number:
        return self.__class__(abs(Decimal.__abs__(self)))
