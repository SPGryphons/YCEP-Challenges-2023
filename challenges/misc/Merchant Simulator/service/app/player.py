from dataclasses import dataclass, field

from typing import Dict

DEFAULT_INVENTORY = {
  "tools": 0,
  "silk": 0,
  "books": 0,
  "weapons": 0,
  "jewellery": 0,
}

@dataclass
class Player:
  """Represents the player in the game world"""

  name: str
  gold: int
  inventory: Dict[str, int] = field(default_factory=lambda: DEFAULT_INVENTORY)

  def pay(self, amount: int):
    """Pays gold to another entity"""
    if self.gold < amount:
      raise ValueError("Not enough gold!")
    self.gold -= amount

  def receive(self, amount: int):
    """Receives gold from another entity"""
    self.gold += amount