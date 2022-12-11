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


def get_user_wk_progress(b_portion):

    usr_name, usr_email = current_user()

    u_email = "ntesla@gmail.com"  # info from current user
    # info from exe list.  if exe from list is in database. If you find one of these exercises in the database.
    # diff activated onclick  - all upper lower whole body progress.
    diff = "Upper Body"

    work = sqlite3.connect('userworkout.db')
    wk = work.cursor()

    # # Get Table of all workouts completed "U L or W"

    wk.execute("SELECT exename, exelvl, weightused, setscomp, difficulty, date FROM userworkout WHERE bod_pt=? and user_e=? ",
               (b_portion, usr_email))

    metric_x = wk.fetchall()

    # print('Entire Progress Sheet Array', metric_x)
    # frame_met_x
    frame_progress_x = pd.DataFrame(metric_x, columns=['Exercise', 'Exercise Level', 'Weight Used (lbs)', 'Sets Completed',
                                                  'Difficulty', 'Date'])


    # frame_met_x = frame_progress_x.style.set_properties(**{'text-align': 'left'})
    # display(left_aligned_df)

    # Converts Data column to Datetime format that mathlib can process.
    # frame_met_x["Date"] = pd.to_datetime(frame_met_x["Date"])

    # Sorts data based on Date column.
    # sorted_frame_metrics = frame_met_x.sort_values("Date")

    # frame_progress_x["Date"] = pd.to_datetime(frame_progress_x["Date"])
    # frame_met_x["Date"] = pd.to_datetime(frame_met_x["Date"])
    frame_progress_x["Date"] = pd.to_datetime(frame_progress_x["Date"])
    # frame_met_x = frame_progress_x.style.set_properties(**{'text-align': 'left'})
    # frame_progress_x = frame_progress_x.style.set_properties(**{'text-align': 'left'})
    frame_p_x = frame_progress_x.style.set_properties(**{'text-align': 'left'})
    # frame_progress_x["Date"] = pd.to_datetime(frame_progress_x["Date"])

    # This return value will vary based on the number of diff exercises completed.
    # sfm1 = frame_met_x

    # print("Table of all workouts completed U L or W", sfm1)

    # met_html = frame_met_x.to_html()
    # met_html = frame_progress_x.to_html()
    met_html = frame_p_x.to_html()

    # print(met_html)

    # pro_g = table(frame_met_x)

    # print('This is the table', pro_g)

    # Calls function on _progress page that writes and displays table rows.
    # eel.bye()

    progress_page(b_portion, met_html)
    # eel.upper_progress(met_html)

    # list of exercises names for upper level. completed
    wk.execute("SELECT exename FROM userworkout WHERE user_e=? and bod_pt=? ", (usr_email, b_portion))

    x_data_wk = wk.fetchall()

    # print('000', x_data_wk)

    x_data_wk_frame = pd.DataFrame(x_data_wk, columns=['Exercise'])

    # plt.savefig("metric.png")

    # sorted_frame.to_csv("sorted_frame.xlsx")

    # List of all exercises.
    ex_lst = pd.read_csv("gui/List_of_exercises.csv")

    # Dataframe created with list of all exercises.
    frame2 = pd.DataFrame(ex_lst, columns=['Exercises', 'Eq'])

    # X isolated column of just the Exercises.
    exe = frame2.iloc[:, :-1]

    # converting array of all exercises to list for comparison.
    list_ex = exe["Exercises"].tolist()

    # Converting array of Upper Body exercises completed to list for comparison.
    list_wk_frame = x_data_wk_frame["Exercise"].tolist()

    # secondWord = set(list_wk_frame) & set(x_data_wk_frame) # I was wrongfully comparing both of the same lists here.

    # Both lists are compared here for individual matches.
    # Due to the fact that there may be multiple entries of exercises with the same name in the database.
    # Each individual workout by name is selected to create a list.
    second_word = set(list_ex) & set(list_wk_frame)

# for loop goes through comparison list and then for each value found, pulls recorded metrics
# Loop then stores info as object and then sorted df is made for plotting.
# exe = "Push Ups" i in this case would be the individual exercise found.

    def w_used_date():

        for i in second_word:

            wk.execute(
              "SELECT date, weightused FROM userworkout WHERE exename=? ", (i, ))

            metric_weight_used = wk.fetchall()

            # print('Weight used table', metric_weight_used)

            frame_weight_used = pd.DataFrame(metric_weight_used, columns=['Date', 'Weight Used (lbs)'])

            # Converts Data column to Datetime format that mathlib can process.
            # frame_met_x["Date"] = pd.to_datetime(frame_met_x["Date"])
            frame_weight_used["Date"] = pd.to_datetime(frame_weight_used["Date"])

            # Sorts data based on Date column.

            sorted_frame_weight_used = frame_weight_used.sort_values("Date")

            date_x = pd.DataFrame(sorted_frame_weight_used, columns=['Date'])
            # print("This is date_x", date_x)

            # date time format changed.
            date_met_x = date_x["Date"] = pd.to_datetime(date_x["Date"])
            # print(date_met_x)

            #
            weight_y = pd.DataFrame(sorted_frame_weight_used, columns=['Weight Used (lbs)'])
            # print("This is weight_y", weight_y)

            #
            # list_date_met_x = date_met_x["Date"].tolist()
            # print("This is list x", list_date_met_x)

            # converting array of all exercises to list for comparison.
            list_date_x = date_x["Date"].tolist()
            # print("This is list x", list_date_x)

            # Converting array of Upper Body exercises completed to list for comparison.
            list_weight_y = weight_y["Weight Used (lbs)"].tolist()
            # print("This is list y", list_weight_y)

            sorted_frame_weight_used["Date"] = pd.to_datetime(sorted_frame_weight_used["Date"])

            # This return value will vary based on the number of diff exercises completed.
            graph = plt.plot(sorted_frame_weight_used['Date'], sorted_frame_weight_used['Weight Used (lbs)'])
            # graph = plt.plot(list_date_x['Date'], list_weight_y['Weight Used (lbs)'])

            plt.title(i)
            plt.xlabel("Date")
            plt.ylabel("Weight Used (lbs)")

            # Bokeh
            # p = figure(title=i, x_axis_label="Date", y_axis_label="Weight Used (lbs)")
            #
            # p.line(list_date_x, list_weight_y, legend_label="Temp.", line_width=3)
            #
            # show(p)
            #
            # script, div = components(p)
            #
            # print("FOR FRONT END script", script)
            # print("FOR FRONT END div", div)

            # eel.upper_w_d(script, div)

            # fig = graph.get_figure()
            # fig = plt.figure(figsize=(12, 10), dpi=80)
            # mpld3.plugins.connect(fig, mpld3.plugins.LineLabelTooltip(graph))
            # mpld3.plugins.connect(fig, plugins.LinkedBrush(points))
            # Title will be individual name of workout. i

            # x_date = plt.xlabel("Date")
            # y_weight = plt.ylabel("Weight Used (lbs)")

            # points = plt.plot(x_date.x, y_weight.y, 'o', color='b')
            #
            # tooltip = mpld3.plugins.PointHTMLTooltip(points[0], voffset=10, hoffset=10)
            # #
            plt.show()
            # gph = plt.render_data_uri()
            # met_plot = plt.to_html()
            # print("TESTTT", met_plot)

            #
            # mpld3.display()
            # test = mpld3.save_html(graph1, )
            # print("TEST DATA", test)

            # plt.show()
            # plot_show = plt.show()

            # fig = plt.figure(figsize=(8, 5))

            # def fig_base64(fig_data):
            #     img = io.BytesIO()
            #     fig_data.savefig(img, format='png', bbox_inches='tight')
            #     img.seek(0)
            #
            #     return base64.b64encode(img.getvalue())

            # encoded = fig_base64(plt)
            # my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
            # plt.show()
            # mpld3.show(fig)

            # html_str = mpld3.fig_to_html(fig)
            # # html_file = open("index.html", "w")
            # html_file.write(html_str)
            # html_file.close()

            # my_html = mpld3.fig_to_html(fig)
            # mpld3.display(fig)
            # print("TEST DATA my_html", my_html)
            #
            # print("This is FIG", fig)
            #
            # eel.upper_w_d(my_html)


            # plot1 = plot_show.to_html()

            # print("HERE IS HTML FOR GRAPH", plot1)
            # Todo return table of completed "Body Port" workouts and first plot

            # plot_wu_d = plt.show()

            # eel.upper_progress(SecondWord, sfm1, plot1 plot_wu_d)
            # return plot1

    # w_used_date()

    def s_comp_date():

        for i in second_word:
            wk.execute("SELECT date, setscomp FROM userworkout WHERE exename=? ", (i, ))

            metric_sets_comp = wk.fetchall()

            # print('Sets Comp. table', metric_sets_comp)

            frame_sets_comp = pd.DataFrame(metric_sets_comp, columns=['Date', 'Sets Completed'])

            sorted_frame_sets_comp = frame_sets_comp.sort_values("Date")
            sorted_frame_sets_comp["Date"] = pd.to_datetime(sorted_frame_sets_comp["Date"])

            sfm3 = sorted_frame_sets_comp
            # print("table 2", sfm3)
            graph2 = plt.plot(sorted_frame_sets_comp['Date'], sorted_frame_sets_comp['Sets Completed'])
            # Title will be individual name of workout. i
            plt.title(i)
            plt.xlabel("Date")
            plt.ylabel("Sets Completed")

            # Todo return second plot
            # Returns a plot for each exercise completed
            plt.show()
            # plot2 = plt.show()
            # return plot2
    # s_comp_date()
    # return met_html


# Todo Clean up code. ensure that each page Upper Lower Whole and Overall has access to function
# Todo have function output resluts to GUI.
# Todo Scheduler / My Interest.

# # When Upper progress page opens this function is called.
# @eel.expose
# def progress_upper():
#     msg_u = "Upper Body"
#
#     aitalk("Upper Body Progress")
#     get_user_wk_progress(msg_u)
#
#
# # When Lower progress page opens this function is called.
# @eel.expose
# def progress_lower():
#     msg_u = "Lower Body"
#
#     aitalk("Lower Body Progress")
#     get_user_wk_progress(msg_u)
#
#
# # When Whole progress page opens this function is called.
# @eel.expose
# def progress_whole():
#     msg_u = "Whole Body"
#
#     aitalk("Whole Body Progress")
#     get_user_wk_progress(msg_u)

# Function calls function on individual progress page to display the table being passed through.
def progress_page(b_port_stat, html):

    if b_port_stat == "Upper Body":
        eel.upper_progress(html)
    elif b_port_stat == "Lower Body":
        eel.lower_progress(html)
    elif b_port_stat == "Whole Body":
        eel.whole_progress(html)




