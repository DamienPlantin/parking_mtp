# main.py
from datetime import datetime
from flask import Blueprint, render_template
from jinja2 import Template
from apscheduler.schedulers.background import BackgroundScheduler
from backend.database.db_mongo import result_database, connect_db, main_db
from backend.database.db_mongo import HOST, PASSWORD, SERVER


MAIN = Blueprint('main', __name__)
SCHED = BackgroundScheduler(daemon=True)
SCHED.start()
main_db()
SCHED.add_job(main_db, 'interval', seconds=179)


@MAIN.route('/')
def parking():
    """This function return parkings in jinja2 in the front
    :returns: list of parkings in parking.html
    :rtype: jinja2
    """
    parkings = result_database(connect_db(HOST, PASSWORD, SERVER))
    now = datetime.now().strftime("%H:%M")
    with open("./frontend/templates/parking.html") as file_:
      template = Template(file_.read())
      result = template.render(parkings=parkings, now=now)
    return result
