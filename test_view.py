from item import Item

def test_item1():
    assert Item("Banana", 1.99, 8).str() == "Banana: $1.99 | Stock: 8"

def test_item2():
    assert Item("Apple", 0.99, 10).str() == "Apple: $0.99 | Stock: 10"

def test_item3():
    assert Item("Pillow", 11.99, 3).str() == "Pillow: $11.99 | Stock: 3"
