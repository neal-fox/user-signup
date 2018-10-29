from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup-success", methods=["POST"])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if (not username) or (username.strip() == "") or (" " in username) or (len(username) < 3) or (len(username) > 20):
        username_error = "Invalid! Username must be between 3 and 20 characters and not contain any spaces"
    if (not password) or (password.strip() == "") or (" " in password) or (len(password) < 3) or (len(password) > 20):
        password_error = "Invalid! Password must be between 3 and 20 characters and not contain any spaces"
    if (not verify_password) or (password != verify_password):
        verify_error = "Passwords do not match!"
    if email:
        if (" " in email) or (not "@" in email) or (email.count("@") > 1) or (not "." in email) or (email.count(".") > 1) or (len(email) < 3) or (len(email) > 20):
            email_error = "Invalid! Email must be between 3 and 20 characters long and contain only one '@' and one '.'"
    if (username_error) or (password_error) or (verify_error) or (email_error):
        return redirect("/?username_error={0}&password_error={1}&verify_error={2}&email_error={3}&username={4}&email={5}".format(username_error,password_error,verify_error,email_error,username,email))
    else:
        return render_template('welcome.html',username=username)

@app.route("/")
def index():
    username = request.args.get("username") if request.args.get("username") else ''
    email = request.args.get("email") if request.args.get("email") else ''
    username_error = request.args.get("username_error") if request.args.get("username_error") else ''
    password_error = request.args.get("password_error") if request.args.get("password_error") else ''
    verify_error = request.args.get("verify_error") if request.args.get("verify_error") else ''
    email_error = request.args.get("email_error") if request.args.get("email_error") else ''

    return render_template('signup.html', username=username,email=email,username_error=username_error,password_error=password_error,verify_error=verify_error,email_error=email_error)

app.run()