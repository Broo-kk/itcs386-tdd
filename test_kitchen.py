from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)
    assert flour.times(2) == Quantity(400)


def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)


def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")
