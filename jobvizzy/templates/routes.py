from jam.timesheet.forms import Timesheet
from Flask import Blueprint

timesheet = Blueprint('timesheet', __name__)



# forms for timesheet-enter clockin-out time for weekly total hours
@app.route('/timesheet', methods=['POST', 'GET'])
def timesheet():
    pass
    We3klyTimesheet = WeeklyHours()
    D4ys = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    if request.method == 'POST':
        pass
        # still need request.form for iteration through form data
        result = request.form
        We3klyTimesheetRes = WeeklyHours(obj=request.form)
        
        return render_template(
            "created_timesheet.html",
            Days=D4ys,
            WeeklyResult=result,
            WeeklyTimesheetRes=We3klyTimesheetRes
        )
    return render_template(
        'create_timesheet.html',
        Days=D4ys,
        form=We3klyTimesheet
    )
