from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from main import Game

import time

class MicrotrasactionService:
  
  def __init__(self, game: Game):
    self.game = game
    self.connected = False
    self.bought_items = {
      "customisation": False,
      "premium_items": False,
      "premium_bank": False,
      "premium_interest_rate": False,
      "travellers_map": False
    }

  def connect(self):
    time.sleep(3)
    raise ConnectionError("Connection timed out")
  
  def has_purchased(self, item):
    return self.bought_items[item]
  
  def purchase_item(self, item: str):
    self.game.interface.output_info("Purchasing item...", delay=3)
    if self.connected:
      if item == "loot box":
        return self.open_loot_box()
      self.bought_items[item] = True
      return True
    else:
      return False

  def open_loot_box(self) -> bool:
    """Opens a lootbox
    This is most definitely not a scam
    """
    self.game.interface.output_info("Opening loot box...")
    self.game.interface.output_info("You got...", delay=1.5)
    self.game.interface.output_info("Nothing! Too bad!") # Get scammed
    return True


class MicrotransactionStore:
  def __init__(self, game: Game):
    self.game = game

  def store_loop(self):
    while True:
      choice = self.game.interface.choose_option(
        "Welcome to the microtransaction store!\nWhat would you like to buy?",
        [
          "Name customisation (One time) - $4.99",
          "Premium items - $12.99",
          "Premium bank account - $14.99",
          "Premium interest rate - $9.99",
          "Traveller's map - $19.99",
          "Loot boxes - $0.99",
          "Exit"
        ],
        with_context=False
      )
      if choice == 0:
        if self.game.mts.has_purchased("customisation"):
          self.game.interface.output_info("You have already purchased this item!")
        result = self.game.mts.purchase_item("customisation")
      elif choice == 1:
        if self.game.mts.has_purchased("premium_items"):
          self.game.interface.output_info("You have already purchased this item!")
        result = self.game.mts.purchase_item("premium_items")
      elif choice == 2:
        if self.game.mts.has_purchased("premium_bank"):
          self.game.interface.output_info("You have already purchased this item!")
        self.game.mts.purchase_item("premium_bank")
        result = self.game.mts.purchase_item("premium_interest_rate")
      elif choice == 3:
        if self.game.mts.has_purchased("premium_interest_rate"):
          self.game.interface.output_info("You have already purchased this item!")
        result = self.game.mts.purchase_item("premium_interest_rate")
      elif choice == 4:
        if self.game.mts.has_purchased("travellers_map"):
          self.game.interface.output_info("You have already purchased this item!")
        result = self.game.mts.purchase_item("travellers_map")
      elif choice == 5:
        result = self.game.mts.purchase_item("loot box")
      elif choice == 6:
        return
      if result:
        self.game.interface.output_info("Purchase successful! Thank you for your support!")
      else:
        self.game.interface.output_info("Purchase failed! Please try again later")

      