# Unit 2 Large Assignment #3: Sign Up Form
# Import needed libraries
from flask import Flask, request, redirect, render_template
import cgi
from helpers import check_empty, check_length, check_space

# Set up Flask and debugging
app = Flask(__name__)
app.config['DEBUG'] = True

# TODO: Remove the render_template that occurs with each if
# statement. Create a new if statement that checks to see
# if any of the error messages are not "". If this evaluates
# to True, render the template with the error(s) and clear the
# password fields only.
# Else, render the welcome page.

# Render the home page
@app.route("/")
def index():
    return render_template('signup-form.html', title="Sign Up")

# Setup the signup function
@app.route("/", methods=['POST'])
def signup():

    # Pull in the data for your four variables
    username = request.form['username']
    password = request.form['password']
    verifypw = request.form['verifypw']
    email = request.form['email']

    # Initialize empty strings for the errors
    username_error = ""
    password_error = ""
    verifypw_error = ""
    email_error = ""

    # Validate content present in username field
    if check_empty(username):
        username_error += cgi.escape("Please enter a username. ")

    # Validate username length
    if check_length(username):
        username_error += cgi.escape("Your username must be 3-20 characters. ")

    # Validate no spaces in username
    if check_space(username):
        username_error += cgi.escape("Your username may not contain spaces. ")

    # Validate content present in password field
    if check_empty(password):
        password_error += cgi.escape("Please enter a password. ")

    # Validate password length
    if check_length(password):
        password_error += cgi.escape("Your password must be 3-20 characters. ")

    # Validate no spaces in password
    if check_space(password):
        password_error += cgi.escape("Your password may not contain spaces. ")

    # Validate content present in verifypw field
    if check_empty(verifypw):
        verifypw_error += cgi.escape("Please verify your password. ")

    # Check password and verifypw to see if they match
    # You don't need to perform the same checks as on password
    # Because if password passes, then verifypw should too
    if password != verifypw:
        verifypw_error += cgi.escape("Your passwords do not match! ")

    # Check email for spaces

    if email != "":
        if check_length(email):
            email_error += cgi.escape("Your email may not contain spaces. ")

    # Check length of email
        if check_length(email):
            email_error += cgi.escape("Your email must be 3-20 characters. ")

    # Check for @ symbol
        if "@" not in email:
            email_error += cgi.escape("Your email must contain an @ symbol. ")

    # Check for . symbol
        if "." not in email:
            email_error += cgi.escape("Your email must contain an . symbol. ")

    if username_error != "" or password_error != "" or verifypw_error != "" or email_error != "":
        username = username
        password = ""
        verifypw = ""
        email = email
        return render_template('signup-form.html', title="Sign Up",
            username=username,
            password=password,
            verifypw=verifypw,
            email=email,
            username_error=username_error,
            password_error=password_error,
            verifypw_error=verifypw_error,
            email_error=email_error)

    else:
        return render_template('welcome.html', title="Welcome!",
            username=username)


#Run the app
app.run()
