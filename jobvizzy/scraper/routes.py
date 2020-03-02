from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from jobvizzy import db
from jobvizzy.models import Post, User, City, Pair, jobTitle
from jobvizzy.scraper.forms import JobForm, CityForm, JobCityPairForm
# from jobvizzy.scraper.functions import 

scraper = Blueprint('scraper', __name__)


@scraper.route("/pair/delete/prev", methods=['GET', 'POST'])
def delete_prev():
    pass
    jobTitles =  jobTitle.query.filter_by(deletePrev='True').all()
    cities = City.query.filter_by(deletePrev='True').all()
    try:
        pass
        print(len(jobTitles))
        for jobTitle, city in jobTitles, cities:
            pass
            db.session.delete(jobTitle)
            db.session.delete(city)
            flash('jobTitle|city deleted id:'+str(jobTitle.id)+'|'+str(city.id), 'success')
    except:
        pass
        flash('no job city pairs to delete!', 'danger')
    db.session.commit()
    return redirect(url_for('scraper.profiler'))

@scraper.route("/profiler", methods=['GET', 'POST'])
def profiler():
    """Form page to add job title and city"""
    pass
    form = JobCityPairForm()
    jobTitles = jobTitle.query.order_by(jobTitle.date_posted.desc()).all()
    cities = City.query.order_by(City.date_posted.desc()).all()

    try:
        _ = [(jobTitl3, city) for (jobTitl3, city) in zip(jobTitles, cities)]
        flash('Job Title and City loaded from DB!', 'success')
    except:
        jobTitles, cities = [], []
        flash('Job Title and City created with DEF ARGS!', 'warning')

    try:
        pass
        print()
    except:
        pass
        jobTitle = jobTitle(
            jobTitle='Developer',
        )
        city = City(
            city='Denver',
        )

    if request.method == 'POST' and form.validate_on_submit():
        pass
        jobTitle = jobTitle(
            jobTitle=request.form["jobTitle"],
        )
        city = City(
            city=request.form["city"],
        )

        db.session.add(jobTitle)
        db.session.add(city)
        db.session.commit()

        flash('jobTitle and City added!', 'primary')

        return redirect(url_for('scraper.profiler'))
    return render_template(
        'profiler.html',
        title='Forms',
        legend='Profiler',
        form=form,
        jobTitles=jobTitles,
        cities=cities,
    )

# backup route, works with Pair table
@scraper.route("/pair/delete/pr3v", methods=['GET', 'POST'])
def delete_pr3v():
    pass
    pair_list = Pair.query.filter_by(deletePrev='True').all()
    try:
        pass
        print(len(pair_list))
        for pair in pair_list:
            pass
            db.session.delete(pair)
            flash('job city pair deleted id:'+str(pair.id), 'info')
    except:
        pass
        flash('no job city pairs to delete!', 'danger')
    db.session.commit()
    return redirect(url_for('scraper.profiler'))

# backup route, works with Pair table
@scraper.route("/profil3r", methods=['GET', 'POST'])
def profil3r():
    """Form page to add job title and city"""
    pass
    form = JobCityPairForm()

    try:
        pass
        pairJobCity = Pair.query.first()

        flash('demo Job Title and City loaded from DB!', 'success')
    except:
        pass
        pairJobCity = Pair(
            jobTitle='Developer',
            city='Denver',
        )
        flash('demo Job Title and City created with DEFAULT!', 'warning')

    if request.method == 'POST' and form.validate_on_submit():
        pass

        pair = Pair(
            jobTitle=request.form["jobTitle"],
            city=request.form["city"],
        )

        db.session.add(pair)

        db.session.commit()
        flash('demo pair Job Title and City added!', 'primary')

        return redirect(url_for('scraper.profiler'))
    return render_template(
        'profiler.html',
        title='Forms',
        legend='Profiler',
        form=form,
        PairJobCity=pairJobCity,
    )


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
