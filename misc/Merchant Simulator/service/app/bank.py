from __future__ import annotations
from dataclasses import dataclass

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
  from main import Game

DEBT_INTEREST_RATE = 0.025
BASE_MIN_LOAN = 5000

@dataclass
class Bank:
  """Represents bank in the game world"""

  game: Game
  player_gold: int = 0
  player_debt: int = 0
  in_debt_since: Union[int, None] = None

  def deposit(self, amount: int):
    """Deposits gold into the bank"""
    self.player_gold += amount

  def withdraw(self, amount: int):
    """Withdraws gold from the bank"""
    if self.player_gold < amount:
      raise ValueError("Not enough gold to withdraw")
    self.player_gold -= amount

  def take_loan(self, amount: int):
    """Takes out a loan from the bank"""
    self.in_debt_since = self.game.week
    self.player_debt += amount

  def pay_loan(self, amount: int):
    """Pays off a loan from the bank"""
    self.player_debt -= amount
    if self.player_debt == 0:
      self.in_debt_since = None

  def collect_interest(self, weeks: int = 1):
    """Collects interest on the player's debt"""
    if self.player_debt != 0:
      for _ in range(weeks):
        self.player_debt = int(self.player_debt * (1 + DEBT_INTEREST_RATE))

  @property
  def max_loan(self) -> int:
    """Returns the maximum amount of gold the player can take out as a loan"""
    return max(BASE_MIN_LOAN, self.game.net_worth * 2 - self.player_debt)