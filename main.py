from flask import Flask, request, render_template, redirect
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']
# Scanning username for length between 3 and 20 (inclusive) and spaces
    username_error = ""
    if " " in username:
        username_error = "No spaces allowed Try again."

    if len(username) < 3 or len(username) > 20:
        username_error = "I think well how do you I tell you this....It might be too long or too short for my liking.....That's what she said!"
# Scanning password for length between 3 and 20 (inclusive) and spaces
    pass_error = ""
    if " " in password:
        pass_error = "Hey NO spaces geez...You just think you're special because you're a person and add spaces anywhere..WELL NO. Try Again!"

    if len(password) < 3 or len(password) > 20:
        pass_error = "I think well how do you I tell you this....It might be too long or too short for my liking.....That's what she said! Try A New PAssword Please!"
    if password != verifypassword:
        pass_error = "You just typed it in and you forgot...oh boy we are doomed. Please re-verify your password."
# Scanning email for length and appropriate characters (no space but @ and .)
    if not username_error and not pass_error and not email:
        return render_template("welcome.html", username=username)
    email_error = ""
    if " " in email:
        email_error = "Hey NO spaces geez...You just think you're special because you're a person and add spaces anywhere..WELL NO. Try Again!"
    if "@" not in email:
        email_error = "Riddle me this...I am what every email has and you forgot me what am I?.................Give up? You forgot your @. Try Again Please."
    errorcount = email.count('@')
    if errorcount > 1:
        email_error = "Email Error Try Again"
    if "." not in email:
        email_error = "Email Error Try Again"
    #if len(email) > 0 and (len(email) < 3 or len(email) > 20):
        #email_error = "It either too long or too short....Try again."

# Checks for no errors, redirecting to a Welcome page instead.  Else goes back to form.
    # if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
    #     return render_template("welcome.html", username=username)
    # else: Checks for no errors, redirecting to a Welcome page instead.  Else goes back to form.
    if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
        return render_template("welcome.html", username=username)

    return render_template("usersignup.html",
        username=username,
        username_error=username_error,
        pass_error=pass_error,
        email=email, email_error=email_error)

@app.route("/")
def index():
    return render_template("usersignup.html",
        username="",
        username_error="",
        pass_error="",
        email="", email_error="")

app.run()
