from flask import Blueprint, render_template, flash, request, redirect, url_for


from appname import cache
from appname.forms import domain_submit


main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


