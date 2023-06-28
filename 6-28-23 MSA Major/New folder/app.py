from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)
app.config['DEBUG'] = True

#set secret key.
app.config['SECRET_KEY'] = 'your secret key'

#Function to get student data from the api
#input: url
#output: JSON student data
def get_student_data(url):
    #make a reuest
    response = requests.get(url)

    #convert to JSON
    response_json = response.json()
    return response_json

#create route for site index. Will display all student data
@app.route('/', methods=['GET'])
def index():

    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data = student_data)

#create a route for the majors search page
@app.route('/majors', methods = ['GET', 'POST'])
def majors():
     #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)
    major_list = []

    #write code that gets the unique majors from the student_data list
    for students in student_data:
        if students['major'] not in major_list:
            major_list.append(students['major'])

    if request.method == 'POST':
        #get the form data
        major = request.form['major'].strip()
        #create list to store results
        result_list = []
        #validate form data
        if not major:
            flash("You must select a major.")
        else:
            #get students with selected major and place in results list
            for student in student_data:
                if student['major'] == major:
                    result_list.append(student)
            return render_template('majors.html', major_list=major_list, result_list=result_list)
        
    return render_template('majors.html', major_list=major_list)

#run the flask appplication
app.run(port=5007)