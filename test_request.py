import requests

url = "http://127.0.0.1:5000/get_form"

# Пример запроса
data = {
    "lead_email": "test@example.com",
    "order_date": "2023-12-01",
    "phone_number": "+7 123 456 78 90"
}

response = requests.post(url, data=data)
print(response.json())
