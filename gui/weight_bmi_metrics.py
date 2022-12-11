import sqlite3
import eel
import pygal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpld3 import plugins
# import mpld3
from bokeh.plotting import figure, show
from bokeh.embed import components
from matplotlib.pyplot import figure
import io
import base64
import plotly
from mpld3 import fig_to_html
from gui.usersession import current_user
from IPython.display import HTML
import IPython


def get_weight_bmi_date():

    usr_name, usr_email = current_user()

    u_email = "ntesla@gmail.com"  # info from current user
    # info from exe list.  if exe from list is in database. If you find one of these exercises in the database.
    # diff activated onclick  - all upper lower whole body progress.
    diff = "Upper Body"

    w_bmi = sqlite3.connect('w_bmi_metrics.db')
    wb = w_bmi.cursor()

    # # Get Table of all workouts completed "U L or W"

    wb.execute("SELECT weight, bmi, date FROM w_bmi_metrics WHERE user_e=? ", (usr_email, ))

    metric_w_b = wb.fetchall()

    # print('Entire Progress Sheet Array', metric_x)
    # frame_met_x
    frame_progress_w_b = pd.DataFrame(metric_w_b, columns=['Weight (lbs)', 'BMI', 'Date'])

    # frame_met_w_b = frame_progress_w_b.style.set_properties(**{'text-align': 'left'})
    # display(left_aligned_df)

    # Converts Data column to Datetime format that mathlib can process.
    # frame_met_x["Date"] = pd.to_datetime(frame_met_x["Date"])

    # Sorts data based on Date column.
    # sorted_frame_metrics = frame_met_x.sort_values("Date")

    # frame_met_w_b["Date"] = pd.to_datetime(frame_met_w_b["Date"])
    frame_progress_w_b["Date"] = pd.to_datetime(frame_progress_w_b["Date"])

    frame_met_w_b = frame_progress_w_b.style.set_properties(**{'text-align': 'left'})
    # frame_progress_w_b.style.set_properties(**{'text-align': 'left'})

    # This return value will vary based on the number of diff exercises completed.
    # sfm1 = frame_met_w_b

    # print("Table of all workouts completed U L or W", sfm1)

    met_html = frame_met_w_b.to_html()
    # met_html = frame_progress_w_b.to_html()

    # print(met_html)

    # pro_g = table(frame_met_x)

    # print('This is the table', pro_g)

    # Calls function on _progress page that writes and displays table rows.
    # eel.bye()

    # progress_page(b_portion, met_html)
    eel.overall(met_html)

    # list of exercises names for upper level. completed
    # wk.execute("SELECT exename FROM userworkout WHERE user_e=? and bod_pt=? ", (usr_email, b_portion))
    #
    # x_data_wk = wk.fetchall()
    #
    # # print('000', x_data_wk)
    #
    # x_data_wk_frame = pd.DataFrame(x_data_wk, columns=['Exercise'])
    #
    # # plt.savefig("metric.png")
    #
    # # sorted_frame.to_csv("sorted_frame.xlsx")
    #
    # # List of all exercises.
    # ex_lst = pd.read_csv("gui/List_of_exercises.csv")
    #
    # # Dataframe created with list of all exercises.
    # frame2 = pd.DataFrame(ex_lst, columns=['Exercises', 'Eq'])
    #
    # # X isolated column of just the Exercises.
    # exe = frame2.iloc[:, :-1]
    #
    # # print('4', ex_lst)
    # # print('5', frame2)
    # # print('6', exe)
    #
    # # converting array of all exercises to list for comparison.
    # list_ex = exe["Exercises"].tolist()
    # # print(list_ex)
    # #
    # # print('List of exercises completed, Upper Body ', x_data_wk_frame)
    #
    # # Converting array of Upper Body exercises completed to list for comparison.
    # list_wk_frame = x_data_wk_frame["Exercise"].tolist()
    # # print(list_wk_frame)
    #
    # # i really need to understand this.
    # # secondWord = set(list_wk_frame) & set(x_data_wk_frame) # was wrongfully comparing both of the same lists here.
    #
    # # Both lists are compared here for individual matches.
    # # Due to the fact that there may be multiple entries. Each individual workout by name is selected to create a list.
    # second_word = set(list_ex) & set(list_wk_frame)
    # print(second_word)

# for loop goes through comparison list and then for each value found, pulls recorded metrics
# Loop then stores info as object and then sorted df is made for plotting.
# exe = "Push Ups" i in this case would be the individual exercise found.

# This script will create a database for observing the weight and bmi metrics overtime.


# u_email = "ntesla@gmail.com"
#
# # usr_name, usr_email = current_user()

    # PLOT
    def weight_date_plot():

        # Acquires date and bmi recorded information for user
        wb.execute(
            "SELECT date, weight FROM w_bmi_metrics WHERE user_e=? ", (u_email,))

        # w_metric = w_bmi.fetchall()
        w_metric = wb.fetchall()

        # print('1', w_metric)

        # formatting test

        w_metric_frame = pd.DataFrame(w_metric, columns=['Date', 'Weight'])

        w_metric_frame["Date"] = pd.to_datetime(w_metric_frame["Date"])

        # w_metric_frame["Date"] = w_metric_frame["Date"].dt.strftime('%d-%b-%Y')

        # print('2', w_metric_frame)

        sorted_w_metric_frame = w_metric_frame.sort_values("Date")
        #
        # print('3', sorted_w_metric_frame)

        # plt.rcParams['figure.figsize'] = (20, 12)

        weight_graph = plt.plot(sorted_w_metric_frame['Date'], sorted_w_metric_frame['Weight'])

        # d_format = DateFormatter('%d-%b-%Y')

        plt.title("W/Time")
        plt.xlabel("Date")
        plt.ylabel("Weight (lbs)")
        # plt.plot(figsize=(40, 20))

        # weight_graph.xaxis.set_major_formatter(md.DataFormatter('%d%b%Y'))

        plt.show()

    # weight_date_plot()

    def bmi_date_plot():

        # Acquires date and bmi recorded information for user
        wb.execute(
            "SELECT date, bmi FROM w_bmi_metrics WHERE user_e=? ", (u_email,))

        # bmi_metric = w_bmi.fetchall()
        bmi_metric = wb.fetchall()

        bmi_metric_frame = pd.DataFrame(bmi_metric, columns=['Date', 'BMI'])

        pd.options.display.float_format = '${:,.2f}'.format

        bmi_metric_frame["Date"] = pd.to_datetime(bmi_metric_frame["Date"])

        sorted_bmi_metric_frame = bmi_metric_frame.sort_values("Date")

        # print(sorted_bmi_metric_frame)

        bmi_graph = plt.plot(sorted_bmi_metric_frame['Date'], sorted_bmi_metric_frame['BMI'])
        # graph2 = plt.plot(frame['Date'], frame['Sets Completed'])

        # Title will be individual name of workout. i
        plt.title("BMI/Time")
        plt.xlabel("Date")
        plt.ylabel("BMI")

        plt.show()

    # Tables for weight and bmi recorded over time.
    # weight_bmi_metrics()

    # bmi_date_plot()


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







