from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # Make a request to the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",  # You may need to adjust the engine
        prompt=user_input,
        max_tokens=150  # You can adjust this based on your needs
    )

    # Extract the generated response from the API result
    ai_response = response['choices'][0]['text'].strip()

    return jsonify({'ai_response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
