import sqlite3 as sql
import secrets
import logging

logger = logging.getLogger(__name__)

class Database:
  def __init__(self):
    self.conn = sql.connect(":memory:", check_same_thread=False)
    cursor = self.conn.cursor()
    with open("init.sql") as f:
      self.conn.executescript(f.read())
    self.conn.commit()

    # Create jason and secret admin users
    cursor.execute(
      "INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (27182, "5b84436c34030209f4dfa71ac45e0b97", "acmd0379@password")
    )
    cursor.execute(
      "INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (31415, "jason", secrets.token_hex(16))
    )

    # Insert data from trivia.csv into the database
    with open("trivia.csv") as f:
      for line in f.readlines():
        cursor.execute(
          "INSERT INTO trivia (id, question, answer, user_id, link) VALUES (?, ?, ?, ?, ?)", line.strip().split(",")
        )

    self.conn.commit()
    cursor.close()
    logger.info("Database initialized")
    
  def add_user(self, username, password):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
      )
      cursor.close()
      return True
    except Exception as e:
      logger.error(e)
      return False
    
  def get_user(self, username):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT id FROM users WHERE username=?", (username,)
      )
      answer = cursor.fetchone()
      cursor.close()
      if answer:
        return answer[0]
      else:
        return False
    except Exception as e:
      logger.error(e)
      return False
    
  def login(self, username, password):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT id FROM users WHERE username=? AND password=?", (username, password)
      )
      answer = cursor.fetchone()
      cursor.close()
      if answer:
        return answer[0]
      else:
        return False
    except Exception as e:
      logger.error(e)
      return False
    
  def get_trivia_by_user_id(self, user_id):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT id, question, answer, link FROM trivia WHERE user_id=?", (user_id,)
      )
      answer = cursor.fetchall()
      cursor.close()
      return answer
    except Exception as e:
      logger.error(e)
      return False
    
  def get_trivia_by_link(self, link):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT id, question, answer, user_id FROM trivia WHERE link=?", (link,)
      )
      answer = cursor.fetchone()
      cursor.close()
      return answer
    except Exception as e:
      logger.error(e)
      return False

  def add_trivia(self, user_id, question, answer, link):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "INSERT INTO trivia (user_id, question, answer, link) VALUES (?, ?, ?, ?)", (user_id, question, answer, link)
      )
      self.conn.commit()
      cursor.close()
      return True
    except Exception as e:
      logger.error(e)
      return False
    
  def get_all_trivia(self):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT * FROM trivia"
      )
      answer = cursor.fetchall()
      cursor.close()
      return answer
    except Exception as e:
      logger.error(e)
      return False
    
  def get_all_users(self):
    try:
      cursor = self.conn.cursor()
      cursor.execute(
        "SELECT * FROM users"
      )
      answer = cursor.fetchall()
      cursor.close()
      return answer
    except Exception as e:
      logger.error(e)
      return False
    
database = Database()