from item import Item

def test_item1():
    assert str(Item("Banana", 1.99, 8)) == "Banana: $1.99 | Stock: 8"

def test_item2():
    assert str(Item("Apple", 0.99, 10)) == "Apple: $0.99 | Stock: 10"

def test_item3():
    assert str(Item("Pillow", 11.99, 3)) == "Pillow: $11.99 | Stock: 3"
