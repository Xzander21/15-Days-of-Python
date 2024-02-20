from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/info', methods=['GET'])
def get_info():
    response = {
        "name": "Your Name",
        "course_and_section": "Your course and section",
        "favorite_programming_language": "Your programming language",
        "aws_service": "Give one AWS service you know"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)