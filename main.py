from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def validity(u, p, pv, e):
    u_error_msg = ""
    p_error_msg = ""
    pv_error_msg = ""
    e_error_msg = ""
 
    if " " in u or len(u) < 3 or len(u) > 20:
        u_error_msg = "Invalid username"
    if " " in p or len(p) < 3 or len(p) > 20:
        p_error_msg = "Invalid password"
    if p != pv:
        pv_error_msg += "Passwords must match"
    if e != "":
        ats = 0
        dots = 0
        for i in e:
            if i == "@":
                ats += 1
            if i == ".":
                dots += 1
            else:
                continue
        if ats or dots != 1:
            e_error_msg = "Invalid email"
        if " " in e or len(e) < 3 or len(e) > 20:
            e_error_msg = "Invalid email"
    if u == "":
        u_error_msg = "Field cannot be blank"
    if p == "":
        p_error_msg = "Field cannot be blank"
    if pv == "":
        pv_error_msg = "Field cannot be blank"
    
    if u_error_msg and p_error_msg and pv_error_msg and e_error_msg == "":
        allvalid = 3

    return u_error_msg, p_error_msg, pv_error_msg, e_error_msg, allvalid

@app.route("/", methods=["POST"])
def validate():
    u_input = request.form['username']
    p_input = request.form['password']
    pv_input = request.form['verify_password']
    e_input = request.form['email']

    errors = validity(u_input, p_input, pv_input, e_input)

    u_error_msg = errors[0]
    p_error_msg = errors[1]
    pv_error_msg = errors[2]
    e_error_msg = errors[3]

    complete = errors[4]

    if complete == 3:    #local variable allvalid referenced before assignment
        return redirect("/welcome" + u_input)

    return render_template("index.html", old_username = u_input, old_email = e_input, u_error = u_error_msg, p_error = p_error_msg, pv_error = pv_error_msg, e_error = e_error_msg)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html", username = u_input)

@app.route("/")      #testinghall on repl.it has test code
def index():
    return render_template("index.html")

app.run()