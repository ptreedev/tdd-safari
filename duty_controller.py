from flask import render_template

from duty import Duty


class DutyController:
    def __init__(self, repo) -> None:
        self._duties = repo.all()

    def list(self) -> str:
        return render_template("duties/list.html", duties=self._duties)
    
    def new_form(self) -> str:
        return render_template("duties/new_form.html")