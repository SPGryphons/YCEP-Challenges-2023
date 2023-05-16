from dataclasses import dataclass

@dataclass
class Item:
  """Represents an item in the game world"""

  name: str
  base_price: int

ITEMS = (
  Item("tools", 25),
  Item("silk", 100),
  Item("books", 250),
  Item("weapons", 500),
  Item("jewellery", 1000)
)