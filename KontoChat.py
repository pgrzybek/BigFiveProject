from flask import Flask, request, redirect, url_for, render_template_string
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "sekret"

login_manager = LoginManager(app)
login_manager.login_view = "login"

# Ustawienia admina
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = generate_password_hash("admin123")  # zmień hasło!


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(username):
    if username == ADMIN_USERNAME:
        user = User()
        user.id = ADMIN_USERNAME
        return user
    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            user = User()
            user.id = ADMIN_USERNAME
            login_user(user)
            return redirect(url_for("admin"))

        return "Błędne dane!"

    return render_template_string("""
        <h2>Logowanie admina</h2>
        <form method="POST">
            <input name="username" placeholder="login" required><br>
            <input name="password" type="password" placeholder="hasło" required><br>
            <button>Zaloguj</button>
        </form>
    """)


@app.route("/admin")
@login_required
def admin():
    return "<h1>Panel Admina</h1> <a href='/logout'>Wyloguj</a>"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


app.run(debug=True)
