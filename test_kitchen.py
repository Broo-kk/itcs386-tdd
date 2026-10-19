from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400
