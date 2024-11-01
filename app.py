from flask import Flask, request, jsonify
import openai
import requests
import os

app = Flask(__name__)

# Set your API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
bing_api_key = os.getenv("BING_API_KEY")

def web_search(query):
    headers = {"Ocp-Apim-Subscription-Key": bing_api_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get("https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results

@app.route('/api/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        query = request.args.get('query')
    elif request.method == 'POST':
        data = request.get_json()
        query = data.get('query')
    else:
        return jsonify({'error': 'Invalid request method'}), 405

    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    try:
        # Perform web search
        search_results = web_search(query)
        snippets = [item['snippet'] for item in search_results.get('webPages', {}).get('value', [])]

        # Prepare messages for GPT-4o
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Answer the following question based on the information provided: {query}"}
        ]
        for i, snippet in enumerate(snippets, 1):
            messages.append({"role": "system", "content": f"Source {i}: {snippet}"})

        # Generate response using GPT-4o
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=150000
        )
        answer = response.choices[0].message['content'].strip()
        return
