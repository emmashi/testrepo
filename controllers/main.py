from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')

def getUserList():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute('SELECT username FROM User')
    results = cur.fetchall()
    return results

@main.route('/')
def main_route():
    user_list = getUserList()
    # user_list = ['sportslover','traveler','spacejunkie']

    options = {
        "user_list": user_list
    }
    return render_template("homepage.html", **options)

# @main.route('/hello')
# def main_hello():
#     db = connect_to_database()
#     cur = db.cursor()
#     cur.execute('SELECT id, name FROM test_tbl')
#     results = cur.fetchall()
#     print(results)
#     print_str = "<table>"
#     for result in results:
#         print_str += "<tr><td>%s</td><td>%s</td><tr>" % (result['id'], result['name'])
#     print_str += "</table>"
#     return print_str
