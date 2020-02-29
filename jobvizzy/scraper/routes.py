from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from jobvizzy import db
from jobvizzy.models import Post, User
from jobvizzy.scraper.forms import JobCityForm

scraper = Blueprint('scraper', __name__)


@scraper.route("/profiler", methods=['GET', 'POST'])
def profiler():
    """Form page to add job title and city"""
    pass
    form = JobCityForm()
    if request.method == 'POST':
        pass
        job = request.form["job"]
        city = request.form["city"]


        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('profiler.html', title='Forms', form=form, legend='Profiler')


# @scraper.route("/scraper", methods=['GET', 'POST'])
# def scraper():
#     form = JobCityForm()

#     return render_template('profiler.html', title='Forms', form=form, legend='profiler')


# @app.route("/03/")
# def lister():
#     pass
#     fulljobVizdata = JobVizzY.scrapListFrameDict(userInputJob, userInputCity)
# # Insert job listings into mongoDb1
#     mongo.db.collection.drop()
#     mongo.db.collection.insert_many(fulljobVizdata)
#     inventory = list(mongo.db.collection.find())
#     return render_template("02Lister.html", inventory=inventory)


# @app.route('/signup', methods=['GET', 'POST'])
# def signup_page():
#     """User sign-up page."""
#     signup_form = SignupForm(request.form)
#     # POST: Sign user in
#     if request.method == 'POST':
