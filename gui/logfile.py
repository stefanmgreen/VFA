import sqlite3
import eel
from gui.voices import aitalk
from gui.dashboard import userdash
from gui.workout import userwk
from gui.bmi import calc_bmi, create_w_bmi_metrics

eel.init("gui")


# Function creates secondary databases for User Dashboard and User Workout functions. and also user weight/bmi
def data_mind():
    msg2 = userdash()
    msg3 = userwk()
    msg4 = create_w_bmi_metrics()


def data_manager(fname, lname, age, gender, height, weight, bmi, email, password, rpassword):
    try:
        db = sqlite3.connect('userdatabase.db')
        # db = Database(sqlite3.connect('userdatabase.db'))
        c = db.cursor()
        # Handles log in and session establishment as well as necessary user personal info. weight ,bmi etc.
        c.execute('''CREATE TABLE IF NOT EXISTS userdatabase(
                                 id integer PRIMARY KEY,
                                 fname text NOT NULL,
                                 lname text NOT NULL,
                                 age integer,
                                 gender text NOT NULL,
                                 height integer,
                                 weight integer,
                                 bmi integer,
                                 email text NOT NULL,
                                 password text NOT NULL,
                                 rpassword text NOT NULL);
                
                ''')
        # Attaches another databased user session. I will use this to determine the log in session status.
        c.execute(
            "CREATE TABLE IF NOT EXISTS my_session(id INTEGER NOT NULL PRIMARY KEY, UserName text, UserEmail text)")

        c.execute(
            "INSERT OR REPLACE INTO my_session(id) VALUES(?)", (0,))

        c.execute("UPDATE my_session SET UserName ==? WHERE id =?", ("offline", 0,))
        c.execute("UPDATE my_session SET UserEmail ==? WHERE id =?", ("offline", 0,))

        # Todo Process should compare password and rpassword before returning success.
        # Todo if not return prompt please ensure that you chose the same password

        if fname != "" and lname != "" and age != "" and gender != "" and height != "" and weight != "" and bmi != "" and email != "" and password != "" and rpassword != "":
            c.execute(
                "INSERT INTO userdatabase (fname, lname, age, gender, height, weight, bmi, email, password, rpassword) VALUES (?,?,?,?,?,?,?,?,?,?);",
                (fname, lname, age, gender, height, weight, bmi, email, password, rpassword))

            db.commit()
            db.close()
            reply = "success"

            return reply

        else:

            reply = "failure"
            return reply
    except Exception as Error:

        print(Error)
        reply = "failure"
        return reply


# Data_manager function is called on sign up. I did this to reduce processes of creating 3 databases on start up
@eel.expose
def sign_up(fname, lname, age, gender, height, weight, email, password, rpassword):

    # Todo BMI function will receive parameters height and weight, calculate the bmi and return the value for
    #  reference to the data_manager function.
    bmi = calc_bmi(height, weight)

    msg1 = data_manager(fname, lname, age, gender, height, weight, bmi, email, password, rpassword)

    aitalk('Sign Up Successful! You can now log in to your Dashboard')


def login(user, passw):
    try:

        db = sqlite3.connect('userdatabase.db')
        c = db.cursor()

        c.execute(
            "SELECT password FROM userdatabase WHERE email =?", (user,))
        getpass = c.fetchone()

        # Todo create statement for using repeated password in log in process.

        # c.execute("SELECT UserName FROM my_session WHERE id =?", (0, ))
        # get_id = c.fetchone()
        # and get_id == "offline" testtt

        if passw == getpass[0]:
            c.execute("UPDATE my_session SET id ==? WHERE id =?", (1, 0))
            c.execute(
                "SELECT fname FROM userdatabase WHERE email =?", (user,))

            # Current members based on user signed in.
            user_name = c.fetchone()

            user_email = user
            # c.execute(
            #     "UPDATE my_session SET User == WHERE id =?", (member[0], 1,))
            c.execute("UPDATE my_session SET UserName ==? WHERE id =?", (user_name[0], 1,))
            c.execute("UPDATE my_session SET UserEmail ==? WHERE id =?", (user_email, 1,))

            db.commit()
            # print(user_name)
            # print(user_email)
            msg = "success"
            db.close()
            return msg
        else:
            msg = "fail"
            db.close()
            return msg

    except Exception as Error:
        print(Error)
        msg = "fail"
        return msg


@eel.expose
def btn_click(user, passw):
    msg = login(user, passw)
    # message passed as string from back end to front end. Either success or fail, to determine href.
    eel.login_stat(str(msg))


# Function to test the display of information from the back end to the front end input field form.
# @eel.expose
# def log_field_test():
#     email = "nikola@gmail.comhaha"
#     password = "test12345"
#     eel.log_test(email, password)
#     print(email)
#     print(password)

