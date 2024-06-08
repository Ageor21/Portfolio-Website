from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

projects = [
    { "id": 1,
     "Project": "Vacation Mobile Application",
      "Programming languages": "Java, SQLite",
      "Link": "https://github.com/Ageor21/Vacation-App"
      },

      { "id": 2,
     "Project": "Appointment Manager Application",
      "Programming languages": "Java, JavaFX MySQL",
      "Link": "https://github.com/Ageor21/Appointment-Manager-"
      },

      { "id": 3,
     "Project": "Interactive World Map",
      "Programming languages": "Typescript, Angular",
      "Link": "https://github.com/Ageor21/Interactive-World-Map"
      },

      { "id": 4,
     "Project": "Student Data Table",
      "Programming languages": "C++",
      "Link": "https://github.com/Ageor21/Student-Data-Table-"
      },

      { "id": 5,
     "Project": "Time and Weather Application",
      "Programming languages": "Pyton, Tkinter",
      "Link": "https://github.com/Ageor21/TIme_Weather_API"
      }
]


@app.route("/")
def portfolio():
    return render_template('home.html', names_projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
    
@app.route("/<usr>")
def user(usr):
    count = 0
    if request.method == "GET":
        count += 1
        return f"<h1>{usr} YOU HAVE SUCCESSFULLY LOGGED IN!!! Login in attempt: {count}</hr>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)