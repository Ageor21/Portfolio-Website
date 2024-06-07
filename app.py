from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)