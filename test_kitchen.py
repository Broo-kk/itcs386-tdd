from kitchen import Converter, Quantity, Sum, grams, ounces


def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_addition_retains_both_operands():
    total = grams(200).plus(grams(300))

    assert isinstance(total, Sum)
    assert total.left == grams(200)
    assert total.right == grams(300)


def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)


def test_mixed_addition():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1))
    assert converter.reduce(total, "g") == grams(228)


def test_reduce_ounces_to_grams_multiplies_by_the_rate():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    assert converter.reduce(ounces(2), "g") == grams(56)
