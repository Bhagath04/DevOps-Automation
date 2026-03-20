import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/jira', methods=['POST'])
def jira_webhook():
    data = request.json
    # Process Jira webhook data
    print('Received Jira webhook:', data)
    return jsonify({'status': 'success'}), 200

@app.route('/webhook/servicenow', methods=['POST'])
def servicenow_webhook():
    data = request.json
    # Process ServiceNow webhook data
    print('Received ServiceNow webhook:', data)
    return jsonify({'status': 'success'}), 200

@app.route('/webhook/github', methods=['POST'])
def github_webhook():
    data = request.json
    # Process GitHub webhook data
    print('Received GitHub webhook:', data)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)