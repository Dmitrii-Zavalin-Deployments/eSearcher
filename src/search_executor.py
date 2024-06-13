import os
import requests

class SearchExecutor:
    def execute_search(self, query_data):
        API_KEY = os.getenv('API_KEY')
        SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')
        QUERY = query_data['query']

        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={QUERY}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            results = response.json()

            found_links = []
            for item in results.get('items', []):
                found_links.append(item['link'])

            return found_links
        except requests.exceptions.RequestException as e:
            print(f"An error occurred in SearchExecutor: {e}")
            return []
