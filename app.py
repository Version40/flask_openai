from flask import Flask, render_template, request, jsonify
import requests

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = "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"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


MODEL = "gpt-3.5-turbo"


@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json

    user_message = ""

    if 'field1' in data and data['field1'].strip():
        user_message += f"{data['field1']}\n"

    if 'field2' in data and data['field2'].strip():
        user_message += f"{data['field2']}"

    if not user_message:
        response_data = {
            'result': "Порожні поля. Введіть дані у поля field1 або field2."
        }
        return jsonify(response_data)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.9,  # Параметр для регулювання креативності відповіді (за замовчуванням 1.0)
        "max_tokens": 1000,  # Максимальна кількість токенів у відповіді
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        result = [choice["message"]["content"] for choice in data["choices"]]
    else:
        result = ["Помилка під час запиту до OpenAI API."]

    response_data = {
        'result': result
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)