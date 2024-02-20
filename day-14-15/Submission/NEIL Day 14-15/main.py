from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize sample data
aws_services = [
    {"id": 1, "service": "Lambda"},
    {"id": 2, "service": "Simple Storage Service(S3)"}
]

# Route to get all AWS services
@app.route('/aws_services/get_all', methods=['GET'])
def get_all_services():
    return jsonify({"aws_services": aws_services})

# Route to get a specific AWS service by ID
@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((s for s in aws_services if s['id'] == service_id), None)
    if service:
        return jsonify(service)
    else:
        return jsonify({"error": "Service not found"}), 404

# Route to add a new AWS service
@app.route('/aws_services/add_service', methods=['POST'])
def add_service():
    if len(aws_services) >= 5:
        return jsonify({"error": "Maximum number of services reached"}), 400
    data = request.json
    new_service = {"id": len(aws_services) + 1, "service": data["service"]}
    aws_services.append(new_service)
    return jsonify(new_service), 201

# Route to delete a specific AWS service by ID
@app.route('/aws_services/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    global aws_services
    aws_services = [s for s in aws_services if s['id'] != service_id]
    return jsonify({"message": "Service deleted"}), 200

# Route to update a specific AWS service by ID
@app.route('/aws_services/update_service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    data = request.json
    service = next((s for s in aws_services if s['id'] == service_id), None)
    if service:
        service['service'] = data['service']
        return jsonify(service), 200
    else:
        return jsonify({"error": "Service not found"}), 404

# Root route
@app.route('/')
def root():
    return jsonify({"message": "Welcome to the AWS Services API"})

if __name__ == '__main__':
    app.run(debug=True)
