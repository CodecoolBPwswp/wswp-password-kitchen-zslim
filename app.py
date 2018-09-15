import hash_manager
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", body_class="default")


@app.route("/hash-new-password", methods=["POST"])
def hashing():
    password_to_hash = request.form["password"]
    new_hash = hash_manager.hash_password(password_to_hash)
    return render_template("index.html", password_to_hash=password_to_hash,
                           new_hash=new_hash)


@app.route("/verify", methods=["POST"])
def verifying():
    password = request.form["password_to_verify"]
    entered_hash = request.form["hash_to_compare"]
    verified = hash_manager.verify_password(password, entered_hash)
    return render_template("index.html", password_to_verify=password,
                           hash_to_compare=entered_hash, verification_result=verified)


if __name__ == "__main__":
    app.run()
