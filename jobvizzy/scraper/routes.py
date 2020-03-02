from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from jobvizzy import db
from jobvizzy.models import Post, User, City, Jobtitle, Pair
from jobvizzy.scraper.forms import JobForm, CityForm, JobCityPairForm
# from jobvizzy.scraper.functions import 

scraper = Blueprint('scraper', __name__)


@scraper.route("/pair/delete/prev", methods=['GET', 'POST'])
def delete_prev():
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


@scraper.route("/profiler", methods=['GET', 'POST'])
def profiler():
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
