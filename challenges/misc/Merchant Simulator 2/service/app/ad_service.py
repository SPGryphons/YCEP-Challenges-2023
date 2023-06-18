from __future__ import annotations

import random
import time

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from main import Game

class AdService:
  ads = [
    "duckcraft",
    "muffin_soda",
    "mushroom_munchies"
  ]

  def __init__(self, game: Game):
    self.game = game

  def display_ad(self):
    ad = random.choice(self.ads)
    with open("ads/" + ad + ".txt") as f:
      self.game.interface.output_info(f.read(), delay=5)