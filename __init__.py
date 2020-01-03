from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_wtf import FlaskForm
from summaryAndTemp import getNeededInfo

app = Flask(__name__)

# Homepage
@app.route('/')
def hello():
    # Home template
    return render_template('home.html')

# Form Submission
@app.route('/getCity', methods=["GET", "POST"])
def formSubmit():
    # Check if form is submitted
    if request.method == "POST":
        # set location to user input
        location = request.form['cityform']
        
        # error handling in case user input is not a location
        try:

            # calls on back end
            info = getNeededInfo(location)

            # sets dict values to variables
            outlooks = info['Outlook']
            precipitation = int(info['Precip'])
            tempe = int(info['Temp'])
            timez = info['TimeZone']

        except Exception:
            # handles error- displays a message prompting user to enter a valid location
            displayTop = "That is not a location"
            displayBottom = "Enter a new one up top!"
            return render_template('error.html', errorMsg = displayTop, err2= displayBottom)

        # renders template with necessary info
        return render_template('answer.html', sum = outlooks, temperature = tempe, precipitation = precipitation, tz = timez, city=location)

    else:
        # renders home template if http request is GET
        render_template('home.html')

# runs program
if __name__ == '__main__':
    app.run() 