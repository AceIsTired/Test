from item import Item

def test_item(name, price, stock):
    assert Item(name, price, stock) == f"{name}: ${price} | Stock:{stock}"
