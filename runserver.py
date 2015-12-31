from app.app_and_db import app, db
from app.startup.init_app import init_app

init_app(app, db)

@app.before_first_request
def create_database():
  db.create_all()

if __name__ == "__main__":
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])