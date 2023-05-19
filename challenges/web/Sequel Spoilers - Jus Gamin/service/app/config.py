from util import generate

class Config(object):
  SECRET_KEY = generate(50)