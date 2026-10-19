import pytest

from shipping import shipping_fee


# Rule 1: zero and negative weights must be rejected.
@pytest.mark.parametrize("weight", [0, -0.1])
def test_nonpositive_weight_is_rejected(weight):
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(weight)


# Rule 2: any positive parcel weighing up to and including 1 kg costs 40 baht.
@pytest.mark.parametrize("weight", [0.1, 0.99, 1])
def test_parcels_up_to_one_kg_cost_40_baht(weight):
    assert shipping_fee(weight) == 40


# Rule 3: parcels over 1 kg and up to and including 5 kg cost 60 baht.
@pytest.mark.parametrize("weight", [1.01, 3, 5])
def test_parcels_over_one_and_up_to_five_kg_cost_60_baht(weight):
    assert shipping_fee(weight) == 60


# Rule 4: each started kilogram above 5 kg adds 10 baht.
@pytest.mark.parametrize(
    "weight, expected_fee",
    [(5.01, 70), (5.2, 70), (6, 70), (6.01, 80)],
)
def test_parcels_over_five_kg_pay_for_each_started_kilogram(weight, expected_fee):
    assert shipping_fee(weight) == expected_fee
