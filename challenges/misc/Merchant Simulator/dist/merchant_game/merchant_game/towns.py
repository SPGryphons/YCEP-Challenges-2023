from __future__ import annotations

from dataclasses import dataclass
import math
import random

@dataclass
class Town:
  """Represents town in the game world"""

  name: str
  x: int
  y: int
  is_main_city: bool = False

  @property
  def coordinates(self) -> tuple:
    """Returns the coordinates of the town as a tuple"""
    return (self.x, self.y)
  
  def distance_from(self, town: Town) -> int:
    """Returns the distance from this town to another town"""
    return int(math.sqrt((self.x - town.x) ** 2 + (self.y - town.y) ** 2))
  

# Towns are in a 3x3 grid, with the main city in the center
# The towns are randomly generated within the grid


TOWNS = (
  Town("Ravenwood", random.randrange(0, 100), random.randrange(0, 100), is_main_city=True),
  Town("Stonehaven", random.randrange(0, 100), random.randrange(100, 200)), # North
  Town("Blackwater", random.randrange(100, 200), random.randrange(100, 200)), # Northeast
  Town("Ironhold", random.randrange(100, 200), random.randrange(0, 100)), # East
  Town("Castleford", random.randrange(100, 200), random.randrange(-100, 0)), # Southeast
  Town("Fairview", random.randrange(0, 100), random.randrange(-100, 0)), # South
  Town("Willowdale", random.randrange(-100, 0), random.randrange(-100, 0)), # Southwest
  Town("Windermere", random.randrange(-100, 0), random.randrange(0, 100)), # West
  Town("Hazelwood", random.randrange(-100, 0), random.randrange(100, 200)), # Northwest
)