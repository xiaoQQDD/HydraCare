"""REST api blueprint"""
import json
from datetime import datetime, timedelta
from flask import Blueprint, render_template, request, session
from . import db
from . import auth
bp = Blueprint('rest', __name__, url_prefix='')






@bp.get("/data/search/<prov>")
def data001(prov):
    """return search dataset"""
    datas = []
    res = [d for d in datas]
    return json.dumps({"code": 0, "data": res})


@bp.route("/settings", methods=('GET', 'POST'))
@auth.login_required
def settings():
    if request.method == 'GET':
        return render_template('settings.html')
    user = db.find_by_name(session['username'])
    goal = int(request.form['goal'])
    start = int(request.form['start'])
    end = int(request.form['end'])
    gap = int(request.form['gap'])
    user['setting'] = {'goal':goal, 'start':start, 'end':end, 'gap':gap}
    db.update_user(user)
    return render_template('settings.html', success_msg="Goal updated.")

@bp.route("/record", methods=('GET', 'POST'))
def record():
    if request.method == 'GET':
        return render_template('record.html')
    user = db.find_by_name(session['username'])
    record = int(request.form['record'])
    if 'records' not in user:
        user['records'] = []
    user['records'].append({'record':record, 'time':datetime.now().strftime('%Y-%m-%d')})
    db.update_user(user)
    return render_template('record.html', success_msg="Record added.")

@bp.route("/statistics", methods=('GET', 'POST'))
def statistics():
    if request.method == 'GET':
        return render_template('statistics.html')

def getData(num):
    today = datetime.now()
    three_days_ago = today - timedelta(days=num)

    date_str = three_days_ago.strftime("%Y-%m-%d")
    date_key = three_days_ago.strftime("%m.%d")

    user = db.find_by_name(session['username'])

    data = 0

    if 'records' in user:
        for record in user['records']:
            if record['time'] == date_str:
                data = data + record['record']

    return {"date": date_key, "data": data}

@bp.get("/statistics/data")
def statistics_data():
    res = []
    if 'username' in session:
        for i in range(7):
            res.append(getData(i))
    return json.dumps({"code": 0, "data": res})



@bp.get("/getsetting")
@auth.login_required
def getsettings():
    user = db.find_by_name(session['username'])
    if'setting' not in user:
        return {'goal':1000,'start':10, 'end':19, 'gap':30}
    else:
        return user['setting']
