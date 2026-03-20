import requests

class ServiceNowIntegration:
    def __init__(self, instance, user, password):
        self.instance = instance
        self.user = user
        self.password = password
        self.base_url = f'https://{self.instance}.service-now.com/api/now/'

    def create_incident(self, short_description, description):
        url = f'{self.base_url}table/incident'
        headers = {'Content-Type': 'application/json'}
        data = {
            'short_description': short_description,
            'description': description,
        }

        response = requests.post(url, headers=headers, json=data, auth=(self.user, self.password))
        return response.json()

    def get_incident(self, incident_id):
        url = f'{self.base_url}table/incident/{incident_id}'
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url, headers=headers, auth=(self.user, self.password))
        return response.json()

    def update_incident(self, incident_id, update_fields):
        url = f'{self.base_url}table/incident/{incident_id}'
        headers = {'Content-Type': 'application/json'}

        response = requests.patch(url, headers=headers, json=update_fields, auth=(self.user, self.password))
        return response.json()  

    def delete_incident(self, incident_id):
        url = f'{self.base_url}table/incident/{incident_id}'
        headers = {'Content-Type': 'application/json'}

        response = requests.delete(url, headers=headers, auth=(self.user, self.password))
        return response.status_code == 204  
