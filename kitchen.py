class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, converter, unit):
        if self.unit == unit:
            return self
        return Quantity(
            self.amount * converter.rate(self.unit, unit),
            unit,
        )

    def __eq__(self, other):
        if not isinstance(other, Quantity):
            return NotImplemented
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, converter, unit):
        left = self.left.reduce(converter, unit)
        right = self.right.reduce(converter, unit)
        return Quantity(left.amount + right.amount, unit)


class Converter:
    def __init__(self):
        self._rates = {}

    def add_rate(self, from_unit, to_unit, rate):
        self._rates[(from_unit, to_unit)] = rate

    def rate(self, from_unit, to_unit):
        if from_unit == to_unit:
            return 1
        return self._rates[(from_unit, to_unit)]

    def reduce(self, source, unit):
        return source.reduce(self, unit)
