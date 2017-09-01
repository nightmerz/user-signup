from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

#username, password, email;
#Must be 3-20 char, no spaces
#password and ver-pass must match
#email(optional), must have @ and . (1 each)

def check_valid(item):
    message=''

    if len(item)<3 or len(item)>20 or '' in item:
        message = "This must be between 3 and 20 characters and contain no spaces"

    return message

def email_check(email):
    message = check_valid(email)
    # must have @ and .(1 each)
    if email.count('@')>!=1 or email.count('.')>!=1:
         message = "not a valid email"

    return message

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify_password = request.form["verify_password"]
        email = request.form["email"]

        username_error =check_valid (username)
        password_error =check_valid (password)
        verify_password_error = ""
        email_error = ""

        if password != verify_password:
        verify_pasword_error = "Passwrd and verify password do not match"

        if len(email)>0: email_check(email)

        if not username_error and  not password_error and not verify_password_error and not email_errror
            return render_template('welcome.html', user = username)



        return render_template("index.html", username = username,
        email = email,
        username_error = username_error, 
        password_error = passowrd_error,
        verify_password_error = verify_password_error,
        email_error = email_error
)                


    return render_template('index.html')


app.run()
