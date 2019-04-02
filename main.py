from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head></head>
    <body>
      <h1>Signup</h1>
      <form action="/" method="post">
        <label for="username">
            Username
            <input type="text" id="username" name="username" />
        </label>
        <br></br>
        <label for="password">
            Password
            <input type="password" id="password" name="password" />
        </label>
        <br></br>
        <label for="verify_password">
            Verify Password
            <input type="password" id="verify_password" name="verify_password" />
        </label>
        <br></br>
        <label for="email">
            Email (optional)
            <input type="text" id="email" name="email" />
        </label>
        <br></br>
        <input type="submit" value="Submit"/>
      </form>
    </body>
</html>
"""

welcome_html = """
<!DOCTYPE html>
<html>
    <head></head>
    <body>
    Welcome, [username]!
    </body>
</html>
"""

@app.route("/welcome")
def welcome():
    return welcome_html

@app.route("/")      #testinghall on repl.it has test code
def index():
    return form

app.run()