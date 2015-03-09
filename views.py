from flask import request, render_template, flash, redirect
from app import app
from forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if request.method == "POST":
        if form.validate() == True:
            flash("Attempting to login as {0}, remember={1}".format(
                form.openid.data, str(form.remember_me.data)
            ))
            return redirect("/index")
    return render_template("login.html", title="Sign in", form=form)
