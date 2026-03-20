import requests

class GitHubIntegration:
    def __init__(self, token, repo_owner, repo_name):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'

    def create_issue(self, title, body):
        url = f'{self.api_url}/issues'
        headers = {'Authorization': f'token {self.token}', 'Accept': 'application/vnd.github.v3+json'}
        issue_data = {'title': title, 'body': body}
        response = requests.post(url, json=issue_data, headers=headers)
        return response.json()

    def list_pull_requests(self, state='open'):
        url = f'{self.api_url}/pulls?state={state}'
        headers = {'Authorization': f'token {self.token}', 'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(url, headers=headers)
        return response.json()

# Usage:
# token = 'YOUR_GITHUB_TOKEN'
# git_integration = GitHubIntegration(token, 'repo_owner', 'repo_name')
# issues = git_integration.create_issue('Issue title', 'Issue body')
# prs = git_integration.list_pull_requests()