# Backend Data Aggregator for ETL Pipeline

import requests
import pandas as pd

class DataAggregator:
    def __init__(self, platforms):
        self.platforms = platforms

    def fetch_data(self, platform):
        # Placeholder function to fetch data from a platform
        response = requests.get(platform['url'])
        return response.json()

    def aggregate_data(self):
        all_data = []
        for platform in self.platforms:
            platform_data = self.fetch_data(platform)
            all_data.extend(platform_data)
        return pd.DataFrame(all_data)

if __name__ == '__main__':
    platforms = [
        {'name': 'Platform1', 'url': 'http://example.com/api/data1'},
        {'name': 'Platform2', 'url': 'http://example.com/api/data2'},
        {'name': 'Platform3', 'url': 'http://example.com/api/data3'}
    ]
    aggregator = DataAggregator(platforms)
    aggregated_data = aggregator.aggregate_data()
    print(aggregated_data)