from dataclasses import dataclass

@dataclass
class Item:
  """Represents an item in the game world"""

  name: str
  base_price: int

ITEMS = (
  Item("tools", 25),
  Item("silk", 100),
)

PREMIUM_ITEMS = (
  Item("books", 250),
  Item("weapons", 500),
  Item("jewelry", 1000)
)