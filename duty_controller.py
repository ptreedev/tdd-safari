from flask import render_template, redirect, url_for, flash
from duty import DuplicateDescriptionError, DuplicateNameError

class DutyController:
    def __init__(self, repo) -> None:
        self._repo = repo

    def list(self) -> str:
        duties = self._repo.all()
        return render_template("duties/list.html", duties=duties)
    
    def new_form(self) -> str:
        return render_template("duties/new_form.html")
    
    def create_duty(self, name, description):
        try:
            self._repo.add(name, description)
        except(DuplicateNameError, DuplicateDescriptionError) as e:
            flash(str(e), "error")
        return redirect(url_for("duties_list"))