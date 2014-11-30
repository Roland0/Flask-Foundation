from flask import Blueprint, render_template, flash, request, redirect, url_for
from appname import cache
from appname.forms import domain_submit
from appname.controllers.acq_dns import is_live

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=1000)
def home():
    form = domain_submit()
    if form.validate_on_submit():
        domain = form.domain.data
        try:
            live = is_live(domain)
        except:
            live = False
        return render_template('domain_info.html', domain=domain, live=live)
    return render_template('index.html', form=form)


