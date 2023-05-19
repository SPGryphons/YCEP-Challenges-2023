from flask import Flask
import logging

from blueprints.routes import web, api

app = Flask(__name__)

logger = logging.getLogger(__name__)

app.register_blueprint(web, url_prefix="/")
app.register_blueprint(api, url_prefix="/api")

@app.errorhandler(404)
def not_found(e):
  return "404 Not Found", 404

@app.errorhandler(Exception)
def handle_error(e):
  message = e.description if hasattr(e, "description") else [str(a)for a in e.args]
  response = {
    "error": {
      "type": e.__class__.__name__,
      "message": message
    }
  }

  logger.error(response)

  return response, e.code if hasattr(e, "code") else 500

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=1337, use_evalex=False)

