# Day 14-15: Create a Simple REST API using Flask

## Instructions
Create a simple REST API about AWS Services and will have the following routes:
1. /
2. /aws_services/get_all
3. /aws_services/{service_id}
4. /aws_services/add_service
5. /aws_services/delete_service/{service_id}
6. /aws_services/update_service/{service_id}

Sample Output Data:
```json
{
    "aws_services": [
        {
            "id": 1,
            "service": "Lambda"
        },
        {
            "id": 2,
            "service": "Simple Storage Service(S3)"
        }
    ]
}
```

Note: Initialize an array with max of 5 services and request the following routes

1. Create a Python Virtual Enviroment called .venv
```bash
python -m venv .venv
```
2. Activate the venv
```bash
source .venv/Scripts/activate
```
3. Install Flask
```bash
pip install Flask
```
4. If done, deactivate 
```bash
deactivate
```

## To be placed in Submission Folder:
1. main.py
2. requirements.txt
3. Screenshot of the outputs
