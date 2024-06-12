import json
import os
import logging

class DataAggregator:
    def __init__(self, grants_file_path):
        self.grants_file_path = grants_file_path
        self.logger = logging.getLogger(__name__)
        self.run_number = int(os.getenv('GITHUB_RUN_NUMBER', 0))
        self.query_folder = self.run_number % int(os.getenv('NUMBER_OF_QUERIES', 1))
        print(f'GitHub Actions Run Number: {self.run_number}')
        print(f'Number of Queries: {os.getenv("NUMBER_OF_QUERIES", 1)}')
        print(f'Query Folder: {self.query_folder}')

    def append_links_to_file(self, links):
        file_path = f'data/{self.query_folder}/none_words.txt'
        with open(file_path, 'a') as file:
            for link in links:
                file.write(link + '\n')

    def read_grants_data(self):
        if os.path.exists(self.grants_file_path) and os.path.getsize(self.grants_file_path) > 0:
            with open(self.grants_file_path, 'r') as file:
                return json.load(file)
        else:
            return {}

    def write_grants_data(self, data):
        with open(self.grants_file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_grant_data(self, query_data, links):
        self.append_links_to_file(links)
        grants_data = self.read_grants_data()
        
        query_key = query_data['query']
        if query_key not in grants_data:
            grants_data[query_key] = []

        grants_data[query_key].extend(links)
        
        self.write_grants_data(grants_data)
        return grants_data
