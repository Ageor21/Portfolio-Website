from flask import Flask, render_template

app = Flask(__name__)

projects = [
    { "id": 1,
     "Project": "Vacation Mobile Application",
      "Programming languages": "Java, SQLite" 
      },

      { "id": 2,
     "Project": "Appointment Manager Application",
      "Programming languages": "Java, JavaFX MySQL" 
      },

      { "id": 3,
     "Project": "Interactive World Map",
      "Programming languages": "Typescript, Angular" 
      },

      { "id": 4,
     "Project": "Student Data Table",
      "Programming languages": "C++" 
      },

      { "id": 5,
     "Project": "Time and Weather Application",
      "Programming languages": "Pyton, Tkinter" 
      }
]


@app.route("/")
def hello_world():
    return render_template('home.html', names_projects=projects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)