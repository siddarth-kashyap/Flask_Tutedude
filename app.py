from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

app = Flask(__name__)

# Replace with YOUR MongoDB Connection String
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.school_db
collection = db.students

@app.route('/')
def index():
    # We pass None for the error initially
    return render_template('index.html', error=None)

@app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form.get('student_name')
    grade = request.form.get('student_grade')

    try:
        # Try to insert data
        collection.insert_one({"name": name, "grade": grade})
        # If successful, REDIRECT to the success page
        return redirect(url_for('success'))
    except Exception as e:
        # If error, stay on the SAME page and show the error
        return render_template('index.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)