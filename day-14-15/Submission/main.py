from flask import Flask, jsonify  

app = Flask(__name__)

aws_services = [
    {
        "id": 1,
        "service": "Lambda"
    },
    {
        "id": 2,
        "service": "Simple Storage Service(S3)"
    }
]

# base url
@app.route('/', methods=[''])
def hello():
    pass


# /aws_services/get_all
@app.route('/', methods=[''])
def get_all():
    pass


# /aws_services/<int:service_id>
@app.route('/', methods=[''])
def get_service():
    pass


# /aws_services/add_service
@app.route('/', methods=[''])
def add_service():
    pass


# /aws_services/delete_service/<int:service_id>
@app.route('/', methods=[''])
def delete_service():
    pass


# /aws_services/update_service/<int:service_id>
@app.route('/', methods=[''])
def update_service():
    pass

if __name__ == '__main__':
    app.run(debug=True)