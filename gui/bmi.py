import sqlite3
from gui.usersession import current_user


def calc_bmi(user_h, user_w):

    # Here converting height received in cm to inches.
    height = float(user_h)/2.54
    weight = float(user_w)

    bmi = (weight/(height * height))*703

    return float(bmi)


def current_bmi():
    u_name, u_email = current_user()
    db = sqlite3.connect('userdatabase.db')
    c = db.cursor()

    c.execute(
        "SELECT height FROM userdatabase WHERE email =?", (u_email,))

    h = c.fetchone()
    user_height = h[0]
    # print(user_height)
    c.execute(
        "SELECT weight FROM userdatabase WHERE email =?", (u_email,))
    w = c.fetchone()
    user_weight = w[0]
    # print(user_weight)

    c_bmi = calc_bmi(user_height, user_weight)

    c.execute(
        "UPDATE userdatabase SET bmi ==? WHERE email =?", (c_bmi, u_email))

    db.commit()
    db.close()
    # print(c_bmi)

    return c_bmi


def current_weight():

    u_name, u_email = current_user()
    db = sqlite3.connect('userdatabase.db')
    c = db.cursor()

    c.execute(
        "SELECT weight FROM userdatabase WHERE email =?", (u_email,))
    w = c.fetchone()
    c_weight = w[0]

    return c_weight


# Todo function to Update bmi based on new weight. Progress function would use these parameters to monitor progress over time.

# function creates weight / bmi database.
def create_w_bmi_metrics():

    w_bmi = sqlite3.connect('w_bmi_metrics.db')
    wb = w_bmi.cursor()

    wb.execute('''CREATE TABLE IF NOT EXISTS w_bmi_metrics(
        id integer PRIMARY KEY,
        user_n text NOT NULL,
        user_e text NOT NULL,
        weight text NOT NULL,
        bmi text NOT NULL,
        date date);

        ''')

    w_bmi.commit()
    w_bmi.close()


# function stores current user, current user weight and bmi and date of last workout.
# function used to keep track of user weight and bmi over time.
# I will use this to plot graphs for my progress.

def w_bmi_metrics(user_n, user_e, weight, bmi, date):

    try:

        w_bmi = sqlite3.connect('w_bmi_metrics.db')

        wb = w_bmi.cursor()

        if user_n != "" and user_e != "" and weight != "" and bmi != "" and date != "":

            wb.execute("INSERT INTO w_bmi_metrics (user_n, user_e, weight, bmi, date) VALUES (?,?,?,?,?);",

                       (user_n, user_e, weight, bmi, date))

            w_bmi.commit()

            w_bmi.close()

            reply = "success"

            return reply

        else:

            reply = "failure"
            return reply

    except Exception as Error:

        print(Error)
        reply = "failure"
        return reply
