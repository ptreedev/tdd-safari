from flask import Flask

from pathlib import Path

from duty import DutyRepository
from duty_controller import DutyController



def create_app(repo=None):
    if repo is None:
        BASE_DIR = Path(__file__).parent
        repo = DutyRepository(filepath=BASE_DIR / "duties.json")

    app = Flask(__name__)
    controller = DutyController(repo)

    @app.route('/')
    def index():
        return "hello there"
    
    @app.route('/duties', methods=["GET"])
    def duties_list():
        return controller.list()

    return app

if __name__ == '__main__':
    app: Flask = create_app()
    app.run(host='0.0.0.0', port=5000)

