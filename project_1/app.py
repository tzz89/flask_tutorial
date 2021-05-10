from flask import Flask, render_template, url_for, flash, redirect
from project_1.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2360f64ee689b3b89b9566f3caa352e1'

posts = [
    {
        'author': "tzz",
        'title': 'test',
        'content': 'first post content',
        'date_posted': 'May 10 2021'
    },
    {
        'author': 'pig',
        'title': ' blog post 2',
        'content': 'second post content',
        'date_posted': 'Ma 11 2021'
    }
]


@app.route("/")
@app.route("/home")  # this is the root page of the website
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash("login unsucessful. Please check username and password", 'danger')

    return render_template("login.html", title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
