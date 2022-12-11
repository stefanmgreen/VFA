import speech_recognition as spr
import pyttsx3
import pywhatkit
import datetime
import time
import webbrowser
import wikipedia
import pyjokes
import eel
from gui.usersession import flush_session
from gui.usersession import current_user
from gui.bmi import current_bmi, current_weight
from gui.workout_metrics import get_user_wk_progress
from gui.weight_bmi_metrics import get_weight_bmi_date

eel.init("gui")

listener = spr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def hello():

    engine.say('Hi I am Zion')
    # engine.say('I am here to help you with your fitness journey..? Are you ready?')
    engine.runAndWait()
    # engine.stop()
    # busy()


# Ask bool??
def record(ask=False):

    with spr.Microphone() as source:
        if ask:
            aitalk(ask)
        voice = listener.listen(source)
        command = ''
        try:
            command = listener.recognize_google(voice)
            command = command.lower()
        except spr.RequestError:
            aitalk('Zion is down')
        except spr.UnknownValueError:
            aitalk('Hmm. I am not sure if I heard you correctly. Please try again')
            pass
        #     eel.return_window()
            # engine.endLoop()
            # engine.stop()
        return command


def aitalk(text):
    engine.say(text)
    engine.runAndWait()
    # engine.stop()


# Test function to see if engine is isBusy
def busy():
    stat = engine.isBusy()
    # print(stat)


def response(command):

    if 'what is your name' in command:
        aitalk('My name is Zion. I am your Virtual Fitness Assistant')
    elif 'what can you do' in command:
        aitalk('I can help you create your ideal personal fitness plan, by helping you set up your schedule and '
               'suggesting a variety of fun exercises and much more. Would you like to create a profile and get '
               'started?')
    elif 'have one' in command:
        aitalk('Awesome, lets get you log in!')
    elif 'play' in command:
        song = command.replace('play', '')
        aitalk('playing' + song)
        pywhatkit.playonyt(song)
        # print(song)
        exit()
    elif 'play music by' in command:
        song = command.replace('play music by', '')
        aitalk('playing' + song)
        pywhatkit.playonyt(song)
        # print(song)
        exit()
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        # print(info)
        aitalk(info)

    elif 'what is ' in command:
        question = command.replace('what is', '')
        info = wikipedia.summary(question, 1)
        # print(info)
        aitalk(info)
    elif 'how ' in command:
        fact = command.replace('how', '')
        info = wikipedia.summary(fact, 1)
        # print(info)
        aitalk(info)
    elif 'joke' in command:
        funny = command.replace('joke', '')
        joke = pyjokes.get_joke()
        # print(joke)
        aitalk(joke)
        engine.endLoop()
        # exit()
    elif 'exit' in command:
        aitalk('Goodbye')
        exit()
    elif 'bye' in command:
        aitalk('Goodbye')
        # exit()

    elif 'sign up' in command:

        aitalk('Okay. Lets get you signed up')   # Lets create a profile for your own personal Dashboard
        eel.start("/member.html")
        # eel.start("signup.html")

    elif 'log me in' in command:
        aitalk('Okay. Lets get you logged in!')
        eel.start("/member.html")

    elif 'log in' in command:
        aitalk('Okay. Lets get you logged in!')
        eel.start("/member.html")
        busy()

    elif 'login' in command:
        aitalk('Okay. Lets get you logged in!')
        eel.start("/member.html")

    elif 'my bmi' in command:
        usr_bmi = current_bmi()
        us_bmi = "{:.2f}".format(usr_bmi)
        aitalk('Your body mass index is' + str(us_bmi))
        # print(str(user_bmi)

    elif 'my current weight' in command:
        usr_weight = current_weight()
        aitalk('Your current body weight is' + str(usr_weight) + 'pounds.')

    elif 'time' in command:
        t_time = datetime.datetime.now().strftime('%I:%M %p')
        aitalk('The current time is' + t_time)
    elif 'search' in command:
        search = record('What would you like me to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        aitalk('Here is what I found for' + search)
    elif 'find' in command:
        location = record('What would you like me to locate for you?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        aitalk('Here is what I found for the location of' + location)
        # print(user_weight)


# Todo Create other function for access to these responses within log in through wake button and wake phrase
#     if 'my workouts' in command:
#         aitalk('Okay. Here are your workouts!')
#
#         eel.my_work()  # Todo flow control worked with vocal command but need to correct program not returning to UI
#
#         # eel.start("/myworkouts.html")   NOT eel start but href.... function ..

    elif 'my dashboard' in command:
        aitalk('Okay. Here is your dashboard!')
        eel.my_dash()

    elif 'workouts' in command:
        # aitalk('Okay!')
        eel.my_work()


        # Todo function here needs to return VA to UI. without giving error.
        # busy()
        # stat = engine.isBusy()
        # print(stat)

    elif 'dashboard' in command:
        aitalk('Okay. Here is your dashboard!')
        # eel.my_dash()

    # elif '' in command:
    #     aitalk('How can I help?')
    #     busy()
        # listen()
    #
    # else:
    #     aitalk('How can I help?')
    #     busy()
    #     # listen()


eel.return_window()


# Todo Combine signup responses within a class method... if href = then welcome maybe
@eel.expose
def voice_test():
    aitalk("Voice Test 123")


@eel.expose
def t_complete():
    aitalk("Time! How was your workout? Remember to log your performance below.")


# When Upper progress page opens this function is called.
@eel.expose
def progress_upper():
    msg_u = "Upper Body"

    get_user_wk_progress(msg_u)
    aitalk("Upper Body Progress")


# When Lower progress page opens this function is called.
@eel.expose
def progress_lower():
    msg_u = "Lower Body"

    get_user_wk_progress(msg_u)
    aitalk("Lower Body Progress")


# When Whole progress page opens this function is called.
@eel.expose
def progress_whole():
    msg_u = "Whole Body"

    get_user_wk_progress(msg_u)
    aitalk("Whole Body Progress")


# When overall progress page opens this function is called then table create function.
@eel.expose
def progress_overall():

    get_weight_bmi_date()
    aitalk("Overall Progress")


@eel.expose
def profile_updated():
    u_name, u_email = current_user()
    aitalk("Okay" + u_name + "...I updated it")


@eel.expose
def greeting():
    u_name, u_email = current_user()
    aitalk("Welcome back master" + u_name + "...Lets Get Started")


@eel.expose
def user_profile_welcome():

    aitalk('Here is your profile.')


@eel.expose
def welcome():

    aitalk('Here is your Dashboard.')

    # Todo work smooth transition between ai and users
    # listen()


@eel.expose
def work_display():

    aitalk('Here are your workouts.')


@eel.expose
def my_progress():

    aitalk('Here is your progress.')


@eel.expose
def my_schedule():

    aitalk('Here is your schedule')


def event():

    moment = {
        "title": 'Click for Google',
        "url": 'http://google.com/',
        "start": '2021-11-28'
    }


@eel.expose
def my_calendar():

    moment = "{title: 'Testing', url: 'http://apple.com/', start: '2022-01-05'}"

    aitalk('Here is your calendar')
    eel.add_event(moment)


# Beginner Upper Lower and Whole Body Greeting
@eel.expose
def beginner_ulw():

    aitalk('Beginner Upper, Lower and Whole Body Workouts')


# Beginner separate ULW page greetings
@eel.expose
def beginner_upper():

    aitalk('Beginner Upper Body Workouts')


@eel.expose
def beginner_lower():

    aitalk('Beginner Lower Body Workouts')


@eel.expose
def beginner_whole():

    aitalk('Beginner Whole Body Workouts')


# Moderate Upper Lower and Whole Body Greeting
@eel.expose
def moderate_ulw():
    aitalk('Moderate Upper, Lower and Whole Body Workouts')


# Moderate separate ULW page greetings
@eel.expose
def moderate_upper():

    aitalk('Moderate Upper, Body Workouts')


@eel.expose
def moderate_lower():

    aitalk('Moderate Lower, Body Workouts')


@eel.expose
def moderate_whole():

    aitalk('Moderate Whole, Body Workouts')


# Advanced Upper Lower and Whole Body Greeting
@eel.expose
def advanced_ulw():
    aitalk('Advanced Upper, Lower and Whole Body Workouts')


# Advanced separate ULW page greetings
@eel.expose
def advanced_upper():

    aitalk('Advanced Upper, Body Workouts')


@eel.expose
def advanced_lower():

    aitalk('Advanced Lower, Body Workouts')


@eel.expose
def advanced_whole():

    aitalk('Advanced Whole, Body Workouts')


# Pro Athlete Upper Lower and Whole Body Greeting
@eel.expose
def pro_ulw():
    aitalk('Pro Athlete Upper, Lower and Whole Body Workouts')


# Pro Athlete separate ULW page greetings
@eel.expose
def pro_upper():

    aitalk('Pro Athlete Upper Body Workouts')


@eel.expose
def pro_lower():

    aitalk('Pro Athlete Lower Body Workouts')


@eel.expose
def pro_whole():

    aitalk('Pro Athlete Whole Body Workouts')


# Individual Workout Pages.
# Todo html for the 60 different individual workouts including greetings.

@eel.expose
def wk_one():

    aitalk('Workout 1. Start timer when ready.')


@eel.expose
def wk_two():
    aitalk('Workout 2. Start timer when ready.')


@eel.expose
def wk_three():
    aitalk('Workout 3. Start timer when ready.')


@eel.expose
def wk_four():
    aitalk('Workout 4. Start timer when ready.')


@eel.expose
def wk_five():
    aitalk('Workout 5. Start timer when ready.')


@eel.expose
def beginner():

    aitalk('Beginner Jumping Jacks. Start timer when ready ')


@eel.expose
def moderate():

    aitalk('Moderate Body Weight Squats. Start timer when ready ')


@eel.expose
def advanced():

    aitalk('Advanced Body Weight Lunges. Start timer when ready ')


@eel.expose
def pro():

    aitalk('Pro Weight Squats. Start timer when ready ')


@eel.expose
def goodbye():
    u_name, u_email = current_user()
    aitalk('Goodbye' + u_name + '...remember to stay consistent.')
    flush_session()


@eel.expose
def invalid_id():
    aitalk('Incorrect Email or Password')


@eel.expose
def main_page():
    aitalk('Log in')


@eel.expose
def log_in_error():
    aitalk('Please use user email and password to log in')


# Program will run an wait for user input via mic. Just not sure how to correctly parse flow control.
@eel.expose
def assist():

    aitalk('How can I help?')
    listen()


def listen():

    time.sleep(1)
    print('Listening...')
    while 1:
        command = record()
        response(command)
        print(command)






