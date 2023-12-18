from flask import Flask, jsonify  

app = Flask(__name__)

my_info = {
    "name": "Your Name",
    "course_and_section": "Your course and section",
    "favorite_programming language": "Your programming language",
    "aws_service": "Give one AWS service you know"
}

@app.route('/', methods=['GET'])
def get_info():
    pass

if __name__ == '__main__':
    app.run(debug=True)