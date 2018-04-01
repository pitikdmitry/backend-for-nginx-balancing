from werkzeug.contrib.fixers import ProxyFix
from app import create_app

# config_name = os.getenv('FLASK_CONFIG')
app = create_app()
# app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
