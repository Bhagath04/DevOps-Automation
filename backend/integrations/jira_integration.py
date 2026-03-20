import requests
import json

class JiraAPI:
    def __init__(self, base_url, username, api_token):
        self.base_url = base_url
        self.auth = (username, api_token)

    def create_issue(self, project_key, summary, description, issue_type):
        url = f'{self.base_url}/rest/api/2/issue/'
        headers = {'Content-Type': 'application/json'}
        payload = {
            'fields': {
                'project': {'key': project_key},
                'summary': summary,
                'description': description,
                'issuetype': {'name': issue_type},
            }
        }
        response = requests.post(url, auth=self.auth, headers=headers, data=json.dumps(payload))
        return response.json()

    def get_issue(self, issue_key):
        url = f'{self.base_url}/rest/api/2/issue/{issue_key}'
        response = requests.get(url, auth=self.auth)
        return response.json()

    def update_issue(self, issue_key, fields):
        url = f'{self.base_url}/rest/api/2/issue/{issue_key}'
        headers = {'Content-Type': 'application/json'}
        payload = {'fields': fields}
        response = requests.put(url, auth=self.auth, headers=headers, data=json.dumps(payload))
        return response.json()

    def delete_issue(self, issue_key):
        url = f'{self.base_url}/rest/api/2/issue/{issue_key}'
        response = requests.delete(url, auth=self.auth)
        return response.status_code

# Example usage:
# jira = JiraAPI('https://your-jira-instance.atlassian.net', 'your-email@example.com', 'your-api-token')
# jira.create_issue('PROJECT_KEY', 'Issue Summary', 'Issue Description', 'Task')
