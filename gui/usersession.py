import sqlite3
import eel


# Todo go over code


def current_user():
    try:
        db = sqlite3.connect('userdatabase.db')
        c = db.cursor()
        c.execute("SELECT UserName FROM my_session WHERE id =?", (1,))
        get_user_name = c.fetchone()
        c.execute("SELECT UserEmail FROM my_session WHERE id =?", (1,))
        get_user_email = c.fetchone()
        user_name_online = []
        user_email_online = []
        for name in get_user_name:
            user_name_online.append(name)
        for email in get_user_email:
            user_email_online.append(email)
        db.close()
        return user_name_online[0], user_email_online[0]
    except Exception as error:
        user_name_online = "error"
        user_email_online = "error"
        print(error)
        return user_name_online, user_email_online


# checks to ensure that the id = 1
def id_checker():

    u_nam, u_em = current_user()

    db = sqlite3.connect('userdatabase.db')
    c = db.cursor()
    c.execute("SELECT id FROM my_session WHERE UserEmail =?", (u_em,))
    id_check = c.fetchone()
    if id_check == 1:

        msg = 'success'
        return msg

    else:

        msg = 'fail'
        return msg


# Will use "offline" value as error checker
def flush_session():

    user_name = "offline"
    user_email = "offline"

    db = sqlite3.connect('userdatabase.db')
    c = db.cursor()

    c.execute("UPDATE my_session SET UserName ==? WHERE id =?", (user_name, 1,))
    c.execute("UPDATE my_session SET UserEmail ==? WHERE id =?", (user_email, 1,))
    c.execute("UPDATE my_session SET id ==? WHERE id =?", (0, 1))

    db.commit()
    db.close()


# Todo Get current user, get their database info, return that information.

@eel.expose
def user_profile_info():

    p_name, p_email = current_user()

    db = sqlite3.connect('userdatabase.db')
    c = db.cursor()

    c.execute("SELECT * FROM userdatabase WHERE fname ==? and email =?", (p_name, p_email))

    userinfo = c.fetchone()
    user_fname = userinfo[1]
    user_lname = userinfo[2]
    user_age = userinfo[3]
    user_gender = userinfo[4]
    user_height = userinfo[5]
    user_weight = userinfo[6]
    user_bmi = userinfo[7]
    usr_bmi = "{:.2f}".format(user_bmi)
    user_email = userinfo[8]
    user_pass = userinfo[9]
    user_rpass = userinfo[10]

    eel.user_info(user_fname, user_lname, user_age, user_gender, user_height, user_weight, usr_bmi, user_email,
                  user_pass, user_rpass)

    # Todo function to be called from the html side. take in these values. and display them .


@eel.expose
def update_user(fname, lname, age, gender, height, weight, email, password, rpassword):

    # Gets current user email before doing update for pass by reference.
    current_u = current_user()

    db = sqlite3.connect('userdatabase.db')
    c = db.cursor()

    c.execute("UPDATE userdatabase SET fname ==? WHERE email =?", (fname, current_u[1]))
    c.execute("UPDATE userdatabase SET lname ==? WHERE email =?", (lname, current_u[1]))
    c.execute("UPDATE userdatabase SET age ==? WHERE email =?", (age, current_u[1]))
    c.execute("UPDATE userdatabase SET gender ==? WHERE email =?", (gender, current_u[1]))
    c.execute("UPDATE userdatabase SET height ==? WHERE email =?", (height, current_u[1]))
    c.execute("UPDATE userdatabase SET weight ==? WHERE email =?", (weight, current_u[1]))
    c.execute("UPDATE userdatabase SET email ==? WHERE email =?", (email, current_u[1]))
    c.execute("UPDATE userdatabase SET password ==? WHERE email =?", (password, current_u[1]))
    c.execute("UPDATE userdatabase SET rpassword ==? WHERE email =?", (rpassword, current_u[1]))

    db.commit()
    db.close()


# Todo write function to return user to log in page if user tries to go back after logging out. Each page should check this function
# Todo if user = current user run code else return to log in.

# html side will handle href. this is a security measure.
# html side will return a welcome else return user to login page. similar code to code on member.html

# python side return success or failure message
# checks to see if database my_session id =1 or 0 and field is = offline.
# In order to gain access to this database the user would have to attempt a sql injection adding an entry to this particular database.

@eel.expose
def log_check():

    user_name = "offline"
    user_email = "offline"
    msg = id_checker()

    name, email = current_user()

    if name != user_name and email != user_email and msg != 'fail':
        greet = 'bye'
        return greet
    elif msg == 'success':
        greet = 'welcome'
        return greet


# Todo if id is = 0 return to member page. else greeting id checker.


#html side

# eel.expose(login_check)
# function login_check(message)
# {
#
# if (message == "success")
# {
#
#     eel.greeting()
#
# }
#
# else if (message == "fail"){
#
# location.href = "/member.html";
#
# }
#
# };

# Secure check
#
# def secure_check():

# user session database. = offline or 0 then redirect to main page. else pass.






