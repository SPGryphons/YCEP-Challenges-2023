from flask import Flask
import logging

from blueprints.routes import web, api

app = Flask(__name__)
app.config.from_object('config.Config')

logger = logging.getLogger(__name__)

app.register_blueprint(web, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

@app.errorhandler(404)
def not_found(e):
    return '404 Not found', 404

@app.errorhandler(Exception)
def handle_error(error):
  message = error.description if hasattr(error, 'description') else [str(x) for x in error.args]
  response = {
    'error': {
      'type': error.__class__.__name__,
      'message': message
    }
  }

  logger.error(error)

  return response, error.code if hasattr(error, 'code') else 500

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=1337, debug=True, use_evalex=False)

