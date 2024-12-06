from flask import Flask, request, jsonify
from pymongo import MongoClient
import re
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")  # Имя сервиса в Docker Compose
db = client["form_database"]
collection = db["templates"]
def validate_field(value):
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return "phone"
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return "date"
    except ValueError:
        pass
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return "date"
    except ValueError:
        pass
    if re.match(r'^[^@]+@[^@]+\.[^@]+$', value):
        return "email"
    return "text"

def find_template(data):
    templates = collection.find()
    for template in templates:
        template_fields = template["fields"]
        if all(field in data and validate_field(data[field]) == template_fields[field] for field in template_fields):
            return template["name"]
    return None

@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    template_name = find_template(data)

    if template_name:
        return jsonify({"template": template_name})

    field_types = {key: validate_field(value) for key, value in data.items()}
    return jsonify(field_types)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
