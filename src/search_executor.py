import os
import requests
from datetime import datetime, timedelta

class SearchExecutor:
    def execute_search(self, query_data):
        API_KEY = os.getenv('API_KEY')
        SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')
        QUERY = query_data['query']

        # Calculate the number of words in the query
        word_count = len(QUERY.split())

        # Check if the query is within the 32-word limit
        if word_count <= 32:
            # Calculate the date 7 months ago from today
            seven_months_ago = (datetime.now() - timedelta(days=7*30)).strftime('%Y%m%d')
            today = datetime.now().strftime('%Y%m%d')

            # Update the URL to include the date range for the past 7 months
            url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={QUERY}&sort=date:r:{seven_months_ago}:{today}"

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
        else:
            # Return a message if the query exceeds the word limit
            return [f"Query exceeds 32 words ({word_count} words). Please shorten the query."]



