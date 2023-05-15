"""
 __  __               _                 _     ____  _                 _       _             
|  \/  | ___ _ __ ___| |__   __ _ _ __ | |_  / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
| |\/| |/ _ \ '__/ __| '_ \ / _` | '_ \| __| \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |  | |  __/ | | (__| | | | (_| | | | | |_   ___) | | | | | | | |_| | | (_| | || (_) | |   
|_|  |_|\___|_|  \___|_| |_|\__,_|_| |_|\__| |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                                                                                            
 ____       _                  ____                     _                 
|  _ \  ___| |_   ___  _____  |  _ \ _ __ ___ _ __ ___ (_)_   _ _ __ ___  
| | | |/ _ \ | | | \ \/ / _ \ | |_) | '__/ _ \ '_ ` _ \| | | | | '_ ` _ \ 
| |_| |  __/ | |_| |>  <  __/ |  __/| | |  __/ | | | | | | |_| | | | | | |
|____/ \___|_|\__,_/_/\_\___| |_|   |_|  \___|_| |_| |_|_|\__,_|_| |_| |_|
                                                                          
 _   _ _ _   _                 _         _____    _ _ _   _                ____             __  
| | | | | |_(_)_ __ ___   __ _| |_ ___  | ____|__| (_) |_(_) ___  _ __    / / _|_ __ ___  __\ \ 
| | | | | __| | '_ ` _ \ / _` | __/ _ \ |  _| / _` | | __| |/ _ \| '_ \  | | |_| '__/ _ \/ _ \ |
| |_| | | |_| | | | | | | (_| | ||  __/ | |__| (_| | | |_| | (_) | | | | | |  _| | |  __/  __/ |
 \___/|_|\__|_|_| |_| |_|\__,_|\__\___| |_____\__,_|_|\__|_|\___/|_| |_| | |_| |_|  \___|\___| |
                                                                          \_\               /_/
Inspired by Mega Micro Computers
"""


# Imports
import os
import random
from typing import Dict, Tuple

from ad_service import AdService
from bank import Bank
from items import ITEMS, PREMIUM_ITEMS
from player import Player
from towns import TOWNS, Town
from ui import Interface
from microtransaction_service import MicrotrasactionService, MicrotransactionStore

# Constants
STARTING_GOLD = 100
TARGET_GOLD = 1000000
DEFAULT_NAME = "Player"

# Main game class
class Game:
  """The main game class"""
  
  def __init__(self):
    self.bank: Bank = Bank(self)
    self.interface: Interface = Interface(self)
    self.towns: Tuple[Town, ...] = TOWNS
    self.current_town = self.towns[0]
    self.items = ITEMS
    self.week: int = 1
    self.is_running: bool = False
    self.prices: Dict[str, int] = {}

    self.mts = MicrotrasactionService(self)
    self.store = MicrotransactionStore(self)

    self.ad_service = AdService(self)

  def pass_weeks(self, weeks: int):
    """Passes the specified number of weeks
    And maybe show an ad"""
    self.week += weeks

    n = random.randint(1, 10)
    if 1 <= n <= 2:
      self.ad_service.display_ad()
    elif 7 <= n <= 10:
      choice = self.interface.choose_option(
        "Would you like to watch an ad for a free loot box?",
        ["Yes", "No"],
        with_context=False
      )
      if choice == 0:
        self.ad_service.display_ad()
        self.mts.open_loot_box()

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
    if self.mts.has_purchased("premium_items"):
      self.items = ITEMS + PREMIUM_ITEMS
    self.price_weights = self.generate_random_price_weights()
    for item in self.items:
      self.prices[item.name] = int(
        item.base_price + item.base_price * (self.price_weights[item.name] / 100)
      )
    for name, weight in self.price_weights.items():
      if weight > 25:
        self.interface.output_info(f"{name.capitalize()} is more expensive than usual!")
      elif weight < -25:
        self.interface.output_info(f"{name.capitalize()} is much cheaper than usual!")

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

    self.interface.output_info("Loading game...", delay=5)

    self.interface.output_info("Connecting to Microtransaction Services...", delay=0)
    try:
      self.mts.connect()
    except ConnectionError:
      self.interface.output_info("Failed to connect to Microtransaction Services! Unable to load player data!")

    choice = self.interface.choose_option(
      "Please read and accept the terms and conditions to continue:",
      [
        "Read Terms and Conditions", "Don't care, accept anyway"
      ]
    )
    if choice == 0:
      with open("terms.txt") as f:
        choice = self.interface.choose_option(
          f"Terms and Conditions:\n{f.read()}\nDo you accept?",
          ["I accept the terms, and have painstakingly signed it in blood"]
        )
    
    self.interface.clear()

    if self.mts.has_purchased("customisation"):
      name = self.interface.get_input("What is your name?")
    else:
      self.interface.output_info("Setting player name to default name: 'Player'")
      self.interface.output_info("TIP: Purchase the Customisation DLC for only $4.99 to change your name! (For one game only)")
      name = DEFAULT_NAME

    self.player = Player(name, STARTING_GOLD)

    self.interface.clear()

    self.is_running = True
    self.main_loop()
  
  def end_game(self, debt=False, retire=False):
    self.is_running = False
    self.interface.clear()
    if retire:
      self.interface.output("Congratulations! You have somehow retired!")
      self.interface.output(f"Your net worth was {self.net_worth}!")
      with open("flag.txt") as f:
        self.interface.output(f.read())
    elif debt:
      self.interface.output("You have been forced to retire due to debt!")
      self.interface.output(f"Your net worth was {self.net_worth}!")
    else:
      self.interface.output("Your free trial has ended, please purchase the full version to continue playing!")



  def bank_loop(self):
    while True:
      premium_bank = self.mts.has_purchased("premium_bank")
      premium_interest_rate = self.mts.has_purchased("premium_interest_rate")
      if not premium_bank and not premium_interest_rate:
        self.interface.output_info("TIP: Purchase the Premium Bank DLC for only $14.99 to unlock bank accounts and a lower interest rate on loans!")
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
        if not premium_bank:
          self.interface.output_info("You need to purchase the Premium Bank DLC to use this feature!")
          continue
        amount = self.interface.choose_amount("How much would you like to deposit? ('a' for all)", self.player.gold)
        try:
          self.player.pay(amount)
        except ValueError:
          self.interface.output_info("You don't have enough gold!")
          continue
        self.bank.deposit(amount)
        self.interface.output_info(f"You have deposited {amount} gold!")

      elif choice == 1:
        if not premium_bank:
          self.interface.output_info("You need to purchase the Premium Bank DLC to use this feature!")
          continue
        amount = self.interface.choose_amount("How much would you like to withdraw? ('a' for all)", self.bank.player_gold)
        try:
          self.bank.withdraw(amount)
        except ValueError:
          self.interface.output_info("You don't have enough gold!")
          continue
        self.player.receive(amount)
        self.interface.output_info(f"You have withdrawn {amount} gold!")

      elif choice == 2:
        if not premium_interest_rate:
          self.interface.output_info("TIP: Purchase the Premium Interest DLC for only $9.99 to get a lower interest rate on loans!")
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
        if not premium_interest_rate:
          self.interface.output_info("TIP: Purchase the Premium Interest DLC for only $9.99 to get a lower interest rate on loans!")
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
    self.interface.add_context(self.get_prices, silent=True)
    while True:
      if not self.mts.has_purchased("premium_items"):
        self.interface.output_info("TIP: Purchase the Premium Items DLC for only $12.99 to unlock more items in the shop!")
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
          [item.name.capitalize() for item in self.items]
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
          [item.name.capitalize() for item in self.items]
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
    if not self.mts.has_purchased("travellers_map"):
      self.interface.output_info("You require the Traveller's Map DLC to travel between towns!")
      return

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

      if not self.mts.has_purchased("travellers_map"):
        self.interface.output_info("TIP: Purchase the Traveller's Map DLC for only $19.99 to travel to different towns!")

      choices = [
        "Shop",
        "Travel",
        "Rest for a week",
        "Microtrascation Store"
      ]
      if self.current_town.is_main_city:
        choices.append("Go to the bank")
      if self.net_worth >= TARGET_GOLD:
        choices.append("Retire")

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
      elif choice == 3:
        self.store.store_loop()
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