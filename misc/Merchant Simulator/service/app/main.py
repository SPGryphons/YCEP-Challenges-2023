"""
  __  __               _                 _      _____ _                 _       _             
 |  \/  |             | |               | |    / ____(_)               | |     | |            
 | \  / | ___ _ __ ___| |__   __ _ _ __ | |_  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
 | |\/| |/ _ \ '__/ __| '_ \ / _` | '_ \| __|  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
 | |  | |  __/ | | (__| | | | (_| | | | | |_   ____) | | | | | | | |_| | | (_| | || (_) | |   
 |_|  |_|\___|_|  \___|_| |_|\__,_|_| |_|\__| |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|
"""

# Imports
import os
import codecs
import random
from typing import Dict, Tuple

from bank import Bank
from items import ITEMS
from player import Player
from towns import TOWNS, Town
from ui import Interface

# Constants
STARTING_GOLD = 100
TARGET_GOLD = 1000000

# Main game class
class Game:
  """The main game class"""
  
  def __init__(self):
    self.bank: Bank = Bank(self)
    self.interface: Interface = Interface(self)
    self.towns: Tuple[Town, ...] = TOWNS
    self.current_town = self.towns[0]
    self.items = ITEMS
    self.debug_mode: bool = False # TODO: Remove before game release
    self.week: int = 1
    self.is_running: bool = False
    self.prices: Dict[str, int] = {}

  def pass_weeks(self, weeks: int):
    """Passes the specified number of weeks"""
    self.week += weeks
    self.bank.collect_interest(weeks)
    self.check_debt_status()
    self.generate_shop_prices()

  def generate_random_price_weights(self) -> Dict[str, int]:
    """Generates random price weights for the current town"""
    weights = {
      item.name: random.randint(-25, 25) or 1 # Make sure the value is not 0
      for item in self.items
    }
    if random.randint(1, 5) == 1:
      # 1 in 5 chance of a major price change
      weights[random.choice(list(weights.keys()))] *= 3

    return weights

  def generate_shop_prices(self):
    """Generates the prices for the shop"""
    self.price_weights = self.generate_random_price_weights()
    for item in self.items:
      self.prices[item.name] = int(
        item.base_price + item.base_price * (self.price_weights[item.name] / 100)
      )
    for name, weight in self.price_weights.items():
      if weight > 25:
        self.interface.output_info(f"{name.capitalize()} is more expensive than usual!")
      elif weight < -25:
        self.interface.output_info(f"{name.capitalize()} is more cheaper than usual!")

  def check_debt_status(self):
    """Check if the debt is due, if it is, end the game
    If it isn't due, give a warning
    """
    if self.bank.in_debt_since is not None:
      in_debt_for = self.week - self.bank.in_debt_since
      if in_debt_for >= 50:
        self.end_game(debt=True)
      else:
        self.interface.output_info(f"You have been in debt for {in_debt_for} weeks. If you don't pay it off in {50 - in_debt_for} weeks, you will be forced to retire!")



  def travel_time(self, town: Town) -> int:
    """Returns the travel time to the specified town"""
    return self.current_town.distance_from(town) // 50



  @property
  def net_worth(self):
    """Returns the player's net worth"""
    return self.player.gold + self.bank.player_gold + sum(item.base_price * self.player.inventory[item.name] for item in self.items) - self.bank.player_debt



  def get_status(self) -> str:
    """Returns the UI for the current status"""
    return (
      f"Welcome, {self.player.name}! You are currently in {self.current_town.name}.\n"
      f"Gold: {self.player.gold}\n"
      f"Bank: {self.bank.player_gold}\n"
      f"Week: {self.week}\n"
      f"Debt: {self.bank.player_debt}\n"
      f"Inventory:\n"
      f"  Tools: {self.player.inventory['tools']}\n"
      f"  Silk: {self.player.inventory['silk']}\n"
      f"  Books: {self.player.inventory['books']}\n"
      f"  Weapons: {self.player.inventory['weapons']}\n"
      f"  Jewelry: {self.player.inventory['jewellery']}"
    )

  def get_prices(self) -> str:
    """Returns the UI for the current prices"""
    return "Current Prices:\n" + "\n".join(f"  {item.name.capitalize()}: {self.prices[item.name]}" for item in self.items)



  def start_game(self):
    """Starts the game"""
    self.interface.clear()

    self.interface.output(__doc__)
    input("Press enter to start...")

    self.interface.clear()

    name = self.interface.get_input("What is your name?")
    self.player = Player(name, STARTING_GOLD)

    if codecs.encode(name, "rot_13") == "zhssva":
      self.debug_mode = True

    self.interface.clear()

    self.is_running = True
    self.main_loop()
  
  def end_game(self, debt=False, retire=False):
    self.is_running = False
    self.interface.clear()
    if retire:
      self.interface.output("Congratulations! You have retired!")
      self.interface.output(f"Your net worth was {self.net_worth}!")
      with open("flag.txt") as f:
        self.interface.output(f.read())
    elif debt:
      self.interface.output("You have been forced to retire due to debt!")
      self.interface.output(f"Your net worth was {self.net_worth}!")
    else:
      self.interface.output("You have ran out of time, you lose!")



  def bank_loop(self):
    while True:
      choice = self.interface.choose_option(
        "Welcome to the bank!\nWhat would you like to do?",
        [
          "Deposit gold",
          "Withdraw gold",
          "Take out a loan",
          "Pay off loan",
          "Go back"
        ]
      )
      if choice == 0:
        amount = self.interface.choose_amount("How much would you like to deposit? ('a' for all)", self.player.gold)
        try:
          self.player.pay(amount)
        except ValueError:
          self.interface.output_info("You don't have enough gold!")
          continue
        self.bank.deposit(amount)
        self.interface.output_info(f"You have deposited {amount} gold!")

      elif choice == 1:
        amount = self.interface.choose_amount("How much would you like to withdraw?", self.bank.player_gold)
        try:
          self.bank.withdraw(amount)
        except ValueError:
          self.interface.output_info("You don't have enough gold!")
          continue
        self.player.receive(amount)
        self.interface.output_info(f"You have withdrawn {amount} gold!")

      elif choice == 2:
        if self.bank.player_debt > 0:
          self.interface.output_info("You already have a loan!")
          continue
        amount = self.interface.choose_amount("How much would you like to borrow? ('a' for all)", self.bank.max_loan)
        if amount > self.bank.max_loan:
          self.interface.output_info("You can't borrow that much!")
          continue
        self.bank.take_loan(amount)
        self.player.receive(amount)
        self.interface.output_info(f"You have taken out a loan of {amount} gold!")

      elif choice == 3:
        if self.bank.player_debt == 0:
          self.interface.output_info("You don't have a loan!")
          continue
        amount = self.interface.choose_amount("How much would you like to pay off? ('a' for all)", min(self.player.gold, self.bank.player_debt))
        if amount > self.player.gold:
          self.interface.output_info("You don't have enough gold!")
          continue
        self.player.pay(amount)
        self.bank.pay_loan(amount)
        self.interface.output_info(f"You have paid off {amount} gold!")

      elif choice == 4:
        break

  def shop_loop(self):
    self.interface.add_context(self.get_prices)
    while True:
      choice = self.interface.choose_option(
        "Welcome to the shop!\nWhat would you like to do?",
        [
          "Buy items",
          "Sell items",
          "Go back"
        ]
      )
      if choice == 0:
        item = self.interface.choose_option(
          "What would you like to buy?",
          [
            "Tools",
            "Silk",
            "Books",
            "Weapons",
            "Jewelry"
          ]
        )
        amount = self.interface.choose_amount("How many would you like to buy? ('a' for all)", self.player.gold // self.prices[self.items[item].name])
        try:
          self.player.pay(self.prices[self.items[item].name] * amount)
        except ValueError:
          self.interface.output_info("You don't have enough gold!")
          continue
        self.player.inventory[self.items[item].name] += amount
        self.interface.output_info(f"You have bought {amount} {self.items[item].name}!")
      elif choice == 1:
        item = self.interface.choose_option(
          "What would you like to sell?",
          [
            "Tools",
            "Silk",
            "Books",
            "Weapons",
            "Jewelry"
          ]
        )
        amount = self.interface.choose_amount("How many would you like to sell? ('a' for all)", self.player.inventory[self.items[item].name])
        if amount > self.player.inventory[self.items[item].name]:
          self.interface.output_info("You don't have that many!")
          continue
        self.player.receive(self.prices[self.items[item].name] * amount)
        self.player.inventory[self.items[item].name] -= amount
        self.interface.output_info(f"You have sold {amount} {self.items[item].name}!")
      elif choice == 2:
        self.interface.remove_context(silent=True)
        break

  def travel_menu(self):
    travel_times = {
      town.name: self.travel_time(town) for town in self.towns
    }

    choices = [
      f"{town.name} ({travel_times[town.name]} days)" for town in self.towns if town != self.current_town
    ]
    choices.append("Go back")

    choice = self.interface.choose_option(
      "Where would you like to travel?",
      choices
    )
    if choice == len(choices) - 1:
      return
    
    self.interface.output_info(f"You are traveling to {self.towns[choice].name}!")

    travel_time = travel_times[self.towns[choice].name]
    self.current_town = self.towns[choice]

    self.interface.output_info("Travelling...", delay=travel_time)

    self.interface.output_info(f"You have arrived in {self.current_town.name}!")

    self.pass_weeks(travel_time)

  def main_loop(self):
    self.generate_shop_prices()
    self.interface.add_context(self.get_status, silent=True)

    while self.is_running:
      if self.week >= 500:
        self.end_game()
        break

      choices = [
        "Shop",
        "Travel",
        "Rest for a week"
      ]
      if self.current_town.is_main_city:
        choices.append("Go to the bank")
      if self.net_worth >= TARGET_GOLD:
        choices.append("Retire")
      if self.debug_mode:
        choices.append("Get gold") # TODO: Remove before game release

      choice = self.interface.choose_option(
        "What would you like to do?",
        choices
      )

      if choice == 0:
        self.shop_loop()
      elif choice == 1:
        self.travel_menu()
      elif choice == 2:
        self.interface.output_info("You rest for a week.", delay=1)
        self.pass_weeks(1)
      elif choices[choice] == "Go to the bank":
        self.bank_loop()
      elif choices[choice] == "Retire":
        self.end_game(retire=True)
        break
      elif choices[choice] == "Get gold":
        amount = self.interface.choose_amount("How much gold would you like? ('a' for all)", 1000000)
        self.player.receive(amount)
        self.interface.output_info(f"You have received {amount} gold!")


if __name__ == "__main__":
  os.chdir(os.path.dirname(os.path.abspath(__file__)))
  game = Game()
  game.start_game()