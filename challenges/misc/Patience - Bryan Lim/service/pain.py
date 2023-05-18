import time
import os
import threading

FLAG = "YCEP2023{P4C13NC3_1S_4_V1RTU3}"

message = f"\033[0;36mCongratulations! You either waited for 20 minutes for this flag, or accidentally saw this. Either way, here's your flag:\n{FLAG}\nPS: If you used a program to capture all the output, well done!\033[0m"

FAKE_COUNTDOWN_TIME = 900

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def output(text, duration=3, delay=0):
  text = "\033[0;36m" + text + "\033[0m"
  if fake_timer.running:
    fake_timer.output_text(text)
    time.sleep(duration)
    fake_timer.clear()
  else:
    print(text)
    time.sleep(duration)
    clear()
  time.sleep(delay)

def spinning_animation():
  while True:
    for cursor in '|/-\\':
      yield cursor



class FakeTimer:
  def __init__(self):
    self.timer = 0
    self.output = ""
    self.running = False

  def output_text(self, text):
    self.output = text

  def clear(self):
    self.output = ""

  def main_loop(self):
    show_timer = True
    while self.running:
      if self.timer >= FAKE_COUNTDOWN_TIME:
        if show_timer:
          text = "\033[0;31mTime until flag is revealed: 00:00\033[0m"
        else:
          text = ""
        show_timer = not show_timer
      else:
        text = "\033[0;32mTime until flag is revealed: {:02d}:{:02d}\033[0m".format(*divmod(FAKE_COUNTDOWN_TIME - self.timer, 60))
      if self.output:
        text += "\n" + self.output
      clear()
      print(text)
      self.timer += 1
      time.sleep(1)
    
  def start(self):
    self.running = True
    self.main_loop()

fake_timer = FakeTimer()



if __name__ == "__main__":
  clear()

  # My console doesn't like printing with no newline ending
  output("Loading", duration=3)
  output("Loading.", duration=3)
  output("Loading..", duration=3)
  output("Loading...", duration=3)

  clear()

  output("That was definitely not a fake loading screen.")
  output("Anyways, how are you doing?")
  output("This is a game of patience.")
  output("You will be put to the test.")
  output("How has the CTF been so far?")
  output("I hope you have enjoyed it.")
  output("I hope you have learned something.")
  output("Is it difficult?")
  output("Or did you pick this challenge first because it was easy?")
  output("If you thought that this challenge was easy, prepare to be disappointed.")
  output("Now I know, you're just here for the flag.")
  output("So let me help you with that.")

  fake_timer_thread = threading.Thread(target=fake_timer.start, daemon=True)
  fake_timer_thread.start()

  time.sleep(3)

  output("There we go! A timer!", delay=2)
  output("At least you now know when the flag will be revealed! :)", delay=2)
  output("So, I guess we have 15 minutes to spare.", delay=2)
  output("How are you doing?", delay=2)
  output("I hope you're doing well.", delay=2)
  output("I hope you're having fun.", delay=2)
  output("I definitely didn't have fun making this challenge.", delay=2)
  output("This timer was a nightmare to implement.", delay=2)
  output("And it sometimes flickers a little.", delay=2)
  output("I hope you appreciate it.", delay=2)
  output("Anyways, I'm gonna go now.", delay=2)
  output("See you soon!", delay=2)

  for cursor in spinning_animation():
    if FAKE_COUNTDOWN_TIME - fake_timer.timer <= 749:
      break
    output("Loading... " + cursor, duration=1)

  output("Are you still there?", delay=2)
  output("I hope you're still there.", delay=2)
  output("If you're still there, I want you to know something.", delay=2)
  output("I want you to know that I'm proud of you.", delay=2)
  output("Proud of you for having a longer than average attention span.", delay=2)
  output("Why are you still here?", delay=2)
  output("Go do something else.", delay=2)
  output("I'm sure there are other challenges that you can do.", delay=2)
  output("Seriously, there's nothing here.", delay=2)
  output("I'm not even kidding.", delay=2)

  for cursor in spinning_animation():
    if FAKE_COUNTDOWN_TIME - fake_timer.timer <= 513:
      break
    output("Loading... " + cursor, duration=1)

  output("Wow, you're still here?", delay=2)
  output("I'm impressed.", delay=2)
  output("As a reward, wanna know a secret?", delay=2)
  output("The countdown is fake.", delay=2)
  output("I'm sorry.", delay=2)
  output("It's all a lie.", delay=2)
  output("Always has been.", delay=2)
  output("This challenge requires a lot of patience.", delay=2)
  output("I hope you have it.", delay=2)

  for cursor in spinning_animation():
    if FAKE_COUNTDOWN_TIME - fake_timer.timer <= 274:
      break
    output("Loading... " + cursor, duration=1)

  output("Wow.", delay=2)
  output("You're still here.", delay=2)
  output("I'm impressed.", delay=2)
  output("For staying with me for so long, I'll give you a reward.", delay=2)
  output("Exactly 380 seconds after the timer ends, the flag will be revealed.", duration=5, delay=2)
  output("You will have a 5 second window, so be ready.", delay=2)
  output("I wish you the best of luck.", delay=2)

  for cursor in spinning_animation():
    if FAKE_COUNTDOWN_TIME - fake_timer.timer <= 31:
      break
    output("Loading... " + cursor, duration=1)

  time.sleep(1)
  
  output("30 seconds left!!!!", delay=2)
  output("I hope you're ready!", delay=2)
  output("Also if you set a timer to remind you to come back, I'm not impressed.", delay=2)
  output("You're not supposed to do that.", delay=2)
  for i in range(10, 0, -1):
    output(str(i) + " seconds left!!!!", duration=1)
  
  output("Time's up!", duration=5, delay=2)
  output("The flag is...")
  output("The flag is... a lie!", delay=2)
  output("Too bad! :)", delay=2)
  output("I hope you enjoyed this challenge!", delay=5)

  output("If you're here, you're too late! Too bad! :)", duration=355)

  output("The flag is: " + FLAG, duration=5)

  fake_timer.output = "\033[0;36mIf you're here, you're too late! Too bad! :)\033[0m"

  # Output this for 5 more minutes, then exit
  time.sleep(300)

  fake_timer.running = False
  fake_timer_thread.join()

  exit(0)
