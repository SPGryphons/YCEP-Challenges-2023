import sqlite3 as sql
import logging

from util import generate, createJWT

logger = logging.getLogger(__name__)

class Database:
  def __init__(self):
    self.conn = sql.connect(":memory:", check_same_thread=False)
    cursor = self.conn.cursor()
    with open("init.sql") as f:
      cursor.executescript(f.read())
    self.conn.commit()

    cursor.execute(
      "INSERT INTO users (username, password) VALUES (?, ?)",
      ("admin", generate(16))
    )

    self.conn.commit()
    cursor.close()
    logger.info("Database initialized")

  def login(self, username, password):
    cursor = self.conn.cursor()
    cursor.execute(
      f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    )
    user = cursor.fetchone()

    if user:
      token = createJWT(username)
      return token
    else:
      return False
    
db = Database()
