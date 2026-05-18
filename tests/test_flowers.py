from src.flowers import Tulip


def test_tulip_description():
    tulip = Tulip(
        variety="Angelique",
        color="Pink",
        stem_length_cm=35,
        price=4.0,
    )

    assert tulip.description() == "Pink Angelique tulip (35 cm)"