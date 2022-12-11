import sqlite3


# Handles the user interests and research topics


def userdash():

    dash = sqlite3.connect('userdashboard.db')
    sh = dash.cursor()
    sh.execute('''CREATE TABLE IF NOT EXISTS userdashboard(
                               id integer PRIMARY KEY,
                               user_n text NOT NULL,
                               user_e text NOT NULL,
                               topicname text NOT NULL,
                               artlink text NOT NULL,
                               vidlink text NOT NULL,
                               date date);

                

                ''')

    dash.commit()
    dash.close()


# Todo Create function calls to insert and update database here
# Function used to save user interest selected on dashboard.
def userinterest(topicname, artlink, vidlink, date):

    try:

        dash = sqlite3.connect('userdashboard.db')
        sh = dash.cursor()

        if topicname != "" and artlink != "" and vidlink != "" and date != "":

            sh.execute(
                "INSERT INTO userdashboard (topicname, artlink, vidlink, date) VALUES (?,?,?,?);",

                (topicname, artlink, vidlink, date))

            dash.commit()
            dash.close()
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
