import sqlite3
import eel
from gui.voices import aitalk
from gui.progress import progress
from gui.usersession import current_user
from gui.bmi import current_bmi, current_weight, w_bmi_metrics


def userwk():

    work = sqlite3.connect('userworkout.db')
    wk = work.cursor()

    wk.execute('''CREATE TABLE IF NOT EXISTS userworkout(
        id integer PRIMARY KEY,
        user_n text NOT NULL,
        user_e text NOT NULL,
        exelvl text NOT NULL,
        bod_pt text NOT NULL,
        exename text NOT NULL,
        weightused integer,
        setscomp integer,
        difficulty text NOT NULL,
        date date);
        
        ''')

    work.commit()
    work.close()


# Todo Create function calls to insert and update database

# Difficulty feature would be used to determine the recommended number of reps.
# Classifier will measure the persons aptitude to complete the workout successfully.

# Todo Create Recommendation Class

def myworkout(user_n, user_e, exelvl, bod_pt, exename, weightused, setscomp, difficulty, date):

    try:

        work = sqlite3.connect('userworkout.db')
        wk = work.cursor()

        if user_n != "" and user_e != "" and exelvl != "" and bod_pt !="" and exename != "" and weightused != "" and setscomp != "" and difficulty != "" and date !="":

            wk.execute(
                "INSERT INTO userworkout (user_n, user_e, exelvl, bod_pt, exename, weightused, setscomp, difficulty, date) VALUES (?,?,?,?,?,?,?,?,?);",

                (user_n, user_e, exelvl, bod_pt, exename, weightused, setscomp, difficulty, date))

            work.commit()
            work.close()
            reply = "success"
            return reply

        else:

            reply = "failure"
            return reply

    except Exception as Error:
        print(Error)
        reply = "failure"
        return reply


# Todo Test io from the html user side.

# Todo Test io from the html user side.

@eel.expose
def metrics(exelvl, bod_pt, exename, weightused, setscomp, difficulty, date):

    # Todo receive email log in session data here. User
    user_n, user_e = current_user()

    msg1 = myworkout(user_n, user_e, exelvl, bod_pt, exename, weightused, setscomp, difficulty, date)

    # current user bmi stored for metric use.
    c_weight = current_weight()

    # current user weight stored for metric use.
    c_bmi = current_bmi()

    # stores most current bmi after each workout.
    msg2 = w_bmi_metrics(user_n, user_e, c_weight, c_bmi, date)

    aitalk('Workout Complete! Remember to stay hydrated!')

    new_href = progress(exelvl, bod_pt, exename, weightused, setscomp, difficulty)

    eel.new_href(new_href)


