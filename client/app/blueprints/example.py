
from flask import Blueprint, render_template

example_bp = Blueprint("example", __name__)

@example_bp.route("/example")
def example():
    return render_template("example.html")