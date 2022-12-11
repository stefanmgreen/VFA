import pandas as pd
import numpy as np
import joblib
from gui.voices import aitalk


# Portion of code converts feature elements inputted by the user into
# input values test.
# mod_test = np.array([0, 1, 9, 1, 5, 0])


# Todo to be used in predict function .
# progress = mod.predict([mod_test])
#
# print("testinggg.... Model should output Yes here:" + progress)


# Todo Gui side of program calls predict fucntion of ML Model. Suggesting more or less advanced workout.

# Todo Create function to convert features from front end. and return them as a, b, c, d, e. variables

# Todo create function class to encompass the set of functions.


def convert_ex_lvl(e_lvl):
    # todo create list for feature conversion
    # Advanced   0
    # Beginner   1
    # Moderate   2
    # Pro   3

    a = 0
    if "Advanced" in e_lvl:
        a = 0
    elif "Beginner" in e_lvl:
        a = 1
    elif "Moderate" in e_lvl:
        a = 2
    elif "Pro" in e_lvl:
        a = 3

    # print(a)
    return a


# Todo write code to convert body portion features
def convert_b_port(bod_p):

    # Lower Body - 0
    # Upper Body - 1
    # Whole Body - 2
    # ML Encoder sorted features in alphabetical order before encoding.

    b = 0
    if "Lower Body" in bod_p:
        b = 0
    elif "Upper Body" in bod_p:
        b = 1
    elif "Whole Body" in bod_p:
        b = 2
    # print(b)
    return b


# Todo add other workouts
def convert_ex_name(ex_nam):
    # todo create list for feature conversion

    # Loads csv list of exercises and corresponding encoded values
    # I would have to change the file directory if I am trying to test this page individually
    exercises_lst = pd.read_csv("gui/List_of_exercises.csv")

    # Modified code searches the csv list for specific field Exercises with the parameter provided by the function prior
    # User input.
    # isolates the column and rows based on matching name.
    e_name = exercises_lst[exercises_lst["Exercises"] == ex_nam]

    # exercise name and value list stored in np array
    e_list = e_name.values[0]

    # returns encoded value for progress processing.
    e_value = int(e_list[1])
    c = e_value
    # print(c)
    return c

    # Old code
    #     a = 0
    # elif "Body Weight Squats" in ex_nam:
    #     a = 1
    # elif "Jumping Jacks" in ex_nam:
    #     a = 2
    # elif "Weighted Squats" in ex_nam:
    #     a = 3
    # return a


# Feature 'c' Weight Used, Whether free weight as 0 lbs or the recommended 30 lbs or otherwise
# This feature will also look at the ranges 1-29 lbs and 31 lbs and over.


# WHY DOES IT RETURN A 0 OR 1 INSTEAD OF THE ENCODED NUMBER. ?
def convert_w_used(w_used):
    # todo create list for feature conversion

    # weight samples used 0 , 10 , 20 , 30 lbs    -   [ 0, 1, 2, 3 ]
    d = 0

    if int(w_used) <= 0:
        d = 0
    if int(w_used) in range(1, 11):
        d = 1
    if int(w_used) in range(11, 30):
        d = 2
    elif int(w_used) >= 30:
        d = 3
    # print(d)
    return d


# Feature 'd' Sets Completed out of 7

def convert_s_comp(sets_c):
    # todo create list for feature conversion

    # 1 set = 0
    # 2 sets = 1
    # 3 sets = 2
    # 4 sets = 3
    # 5 sets = 4
    # 6 sets = 5
    # 7 sets = 6
    e = 0

    if int(sets_c) <= 1:
        e = 0
    elif int(sets_c) == 2:
        e = 1
    elif int(sets_c) == 3:
        e = 2
    elif int(sets_c) == 4:
        e = 3
    elif int(sets_c) == 5:
        e = 4
    elif int(sets_c) == 6:
        e = 5
    elif int(sets_c) >= 7:
        e = 6
    # print(e)
    return e


# Feature 'e' Difficulty with respect to the time completed

def convert_dif(diff):
    # todo create list for feature conversion

    # "Easy" = 0
    # "Hard" = 1
    # "Moderate" = 2
    f = 0

    if "Easy" in diff:
        f = 0
    elif "Hard" in diff:
        f = 1
    elif "Moderate" in diff:
        f = 2
    # print(f)
    return f


def convert_progress_msg(progress_msg):

    if progress_msg == "No":
        z = 0
    elif progress_msg == "Yes":
        z = 1

    # print(z)
    return z


# converts features to feature parameters "a b c d e" & predicts using model then returns answer Yes or No from target.

def predict_exe(ex_lvl, b_port, ex_name, w_used, s_comp, dif):
    a = convert_ex_lvl(ex_lvl)
    b = convert_b_port(b_port)
    c = convert_ex_name(ex_name)
    d = convert_w_used(w_used)
    e = convert_s_comp(s_comp)
    f = convert_dif(dif)

    feat = np.array([a, b, c, d, e, f])

    # Todo to be used in predict function .
    # Loads ML model created in training_ai
    filename = 'gui/vfa_wk_model.pk1'
    mod = joblib.load(filename)

    filename2 = 'gui/suggestion_model.pk1'
    mod2 = joblib.load(filename2)

    # Yes or No decision concerning user progress based on their performance.
    new_progress = mod.predict([feat])

    # converts progress decision message into integer for second model.
    z = convert_progress_msg(new_progress)

    feat2 = np.array([a, b, z])
    # print(feat2)

    # returns object "NAME" of new target level corresponding encoded number. 0 - 11 for referencing list
    suggest_href = mod2.predict([feat2])

    # print(suggest_href)

    # Loads list of new level suggestions with corresponding page href.
    suggestion_lst = pd.read_csv("gui/workout_href.csv")

    # print(suggestion_lst)

    # isolates the column and rows based on matching name.
    s_lst = suggestion_lst[suggestion_lst["New Lvl Target"] == suggest_href[0]]
    # print(s_lst)

    # exercise name and value list stored in np array
    link = s_lst.values[0]
    # print(link)

    # returns encoded value for progress processing.
    href = str(link[2])

    # print(href)

    # suggest function. take in parameters return href.

    # print(new_progress)
    return new_progress, href


# Todo create function to determine IF Yes then suggest harder exercise and possibly schedule. If No then easier.


def progress(exe_lvl, bod_port, exe_name, weight_used, sets_comp, diff):

    # returns a Yes or No after evaluating user data and the suggested link.
    nw_progress, nw_href = predict_exe(exe_lvl, bod_port, exe_name, weight_used, sets_comp, diff)

    if nw_progress == 'Yes':
        aitalk('Great job! How bout we try something a little more challenging?')

    elif nw_progress == 'No':
        aitalk('Awesome workout! How about we work on some reconditioning before we move on? Lets try these.')
        # call suggest function

    # returns the suggested address
    return nw_href








