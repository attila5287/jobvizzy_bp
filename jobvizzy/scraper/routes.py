from flask import (
    render_template, url_for, flash,
    redirect, request, abort, Blueprint
)
from flask_login import current_user, login_required
from jobvizzy import db
from jobvizzy.models import Post, User, City, Pair, jobtitle
from jobvizzy.scraper.forms import JobForm, CityForm, JobCityPairForm

from jobvizzy.scraper.functions import scrapListFrameDict
# from jobvizzy.scraper.functions import 

scraper = Blueprint('scraper', __name__)


@scraper.route("/tabulator", methods=['GET', 'POST'])
def tabulator():
    pass


    return render_template(
        'tabulator.html',
        title='Results(b)',
        legend='tabulator',
    )

@scraper.route("/croupier", methods=['GET', 'POST'])
def croupier():
    pass

    jobs_from_db, cities_from_db = jobtitle.query.all(), City.query.all()

    jobTitles_unique, cities_unique = list(
        set([jobTitl3.jobtitle for jobTitl3 in jobs_from_db])), list(set([city.city for city in cities_from_db]))

    inventory = scrapListFrameDict(
        job_list=jobTitles_unique,
        city_list=cities_unique,
    )


    return render_template(
        'croupier.html',
        title='Results(a)',
        legend='Croupier',
        inventory=inventory,
    )




@scraper.route("/scraper", methods=['GET', 'POST'])
def scrap3r():
    """Form page to add job title and city"""
    pass

    jobs_from_db = jobtitle.query.all()

    jobTitles_unique = list(
        set([jobTitl3.jobtitle for jobTitl3 in jobs_from_db]))

    cities_from_db = City.query.all()

    cities_unique = list(set([city.city for city in cities_from_db]))

    try:
        _ = [(jobTitl3, city)
             for (jobTitl3, city) in zip(jobTitles_unique, cities_unique)]
        flash('Job Title and City loaded from DB!', 'success')
    except:
        jobTitles_unique, cities_unique = [], []
        flash('Job Title and City created with DEF ARGS!', 'warning')

    return render_template(
        'scraper.html',
        title='Confirm',
        legend='Scraper',
        jobTitles_unique=jobTitles_unique,
        cities_unique=cities_unique,
    )



# Form page to add job title and city
@scraper.route("/profiler", methods=['GET', 'POST'])
def profiler():
    pass
    form, jobTitles, cities = JobCityPairForm(), jobtitle.query.all(), City.query.all()

    try:
        _ = [(jobTitl3, city) for (jobTitl3, city) in zip(jobTitles, cities)]
        flash('Job Title and City try !', 'success')
    except:
        jobTitles, cities = [], []
        flash('Job Title and City except!', 'warning')

    if request.method == 'POST' and form.validate_on_submit():
        pass
        jobT1tle, city = jobtitle(
            jobtitle=request.form["jobTitle"],
        ), City(
            city=request.form["city"],
        )

        db.session.add(jobT1tle)
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


@scraper.route("/pair/delete/prev", methods=['GET', 'POST'])
def delete_prev():
    pass
    jobTitles =  jobtitle.query.filter_by(deleteprev='True').all()
    cities = City.query.filter_by(deleteprev='True').all()
    try:
        pass
        print(len(jobTitles))
        for jobTitl3, city in zip(jobTitles, cities):
            pass
            db.session.delete(jobTitl3)
            db.session.delete(city)
            db.session.commit()
            flash('jobTitle|city deleted id:' + str(jobTitl3.id) + '|' + str(city.id), 'success')
            
    except NameError as e:
        pass
        print(e)
        flash('no job no city to delete!', 'danger')
    
    try:
        pass
    except expression as identifier:
        pass

    return redirect(url_for('scraper.profiler'))

# backup route, works with single Pair table
@scraper.route("/pair/delete/pr3v", methods=['GET', 'POST'])
def delete_pr3v():
    pass
    pair_list = Pair.query.filter_by(deleteprev='True').all()
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


# @app.route("/03/")
# def lister():
#     pass
#     fulljobVizdata = JobVizzY.scrapListFrameDict(userInputJob, userInputCity)
# # Insert job listings into mongoDb1
#     mongo.db.collection.drop()
#     mongo.db.collection.insert_many(fulljobVizdata)
#     inventory = list(mongo.db.collection.find())
#     return render_template("02Lister.html", inventory=inventory)

