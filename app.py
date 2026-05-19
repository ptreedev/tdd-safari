import os

from flask import Flask, request

from pathlib import Path

from duty import DutyRepository
from duty_controller import DutyController



def create_app(repo=None):
    if repo is None:
        BASE_DIR = Path(__file__).parent
        default_path = BASE_DIR / "duties.json"
        filepath = Path(os.environ.get("DUTIES_FILE", default_path))
        repo = DutyRepository(filepath=filepath)

    app = Flask(__name__)
    app.secret_key="dev-secret"
    controller = DutyController(repo)

    @app.route('/')
    def index():
        return """
        hello there
        <a href="/duties"> Duties </a>
        """
    
    @app.route('/duties')
    def duties_list():
        return controller.list()
    
    @app.route('/duties/new')
    def duties_new_form():
        return controller.new_form()
    
    @app.post('/duties')
    def duties_create():
        return controller.create_duty(
              name=request.form["name"],
              description=request.form["description"],
          )

    return app

if __name__ == '__main__':
    app: Flask = create_app()
    app.run(host='0.0.0.0', port=5001)

