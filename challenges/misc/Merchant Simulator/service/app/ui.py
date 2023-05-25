from __future__ import annotations

import os
import time

from typing import TYPE_CHECKING, Callable, List

if TYPE_CHECKING:
  from main import Game

class Interface:
  """
  Provides an interface for the program to output information to the user.
  """

  def __init__(self, game: Game):
    self.game = game
    self.context: List[Callable[[], str]] = []
    self.context_displayed = False

  def output_context(self, with_pause: bool = True):
    """Outputs the current context to the user"""
    self.context_displayed = True
    for func in self.context:
      self.output(func(), with_pause=with_pause)

  def add_context(
      self,
      context: Callable[[], str],
      clear: bool = False,
      with_pause: bool = True,
      silent: bool = False
  ):
    """Adds context to the interface"""
    self.context.append(context)
    if clear:
      self.clear()
      if not silent:
        self.output_context(with_pause=with_pause)
    else:
      if not silent:
        self.output(context(), with_pause=with_pause)

  def remove_context(self, with_pause: bool = True, silent: bool = False):
    """Removes the last context from the interface"""
    self.context.pop()
    self.clear()
    if not silent:
      self.output_context(with_pause=with_pause)

  def output(self, message: str, with_pause: bool = True):
    """Outputs a message to the user beautifully"""
    for line in message.splitlines():
      print(line)
      if with_pause:
        time.sleep(0.01)

  def clear(self, keep_context: bool = False):
    """Clears the terminal"""
    print("\033c", end="")
    if keep_context:
      # If we want to keep the context, we need to re-output it
      self.output_context(with_pause=(not self.context_displayed)) # disgusting, I know.
    else:
      self.context_displayed = False

  def choose_option(
    self,
    message: str,
    options: list,
    with_context: bool = True
  ) -> int:
    """Prints a message and returns the user's choice from a list of options."""
    self.clear(with_context)
    self.output(message)
    for i, option in enumerate(options):
      self.output(f"{i + 1}. {option}")
    choice = input("> ")
    while not choice.isdigit() or not (1 <= int(choice) <= len(options)):
      self.output("Invalid choice.")
      choice = input("> ")
    return int(choice) - 1
  
  def choose_amount(
      self,
      message: str,
      max_amt: int,
      with_context: bool = True
  ) -> int:
    """Prints a message and returns the user's choice of amount."""
    self.clear(with_context)
    choice = self.get_input(message)
    while not (choice.isdigit() or choice.upper() == "A"):
      choice = self.get_input("Invalid choice.")
    if choice.upper() == "A":
      return max_amt
    return int(choice)
  
  def output_info(self, message: str, delay: int = 1):
    """Outputs a message to the user for a few seconds"""
    self.clear()
    self.output(message)
    time.sleep(delay)

  def get_input(self, message: str) -> str:
    """Gets input from the user"""
    self.output(message)
    return input("> ")
