import os
from src.query_builder import QueryBuilder
from src.search_executor import SearchExecutor
from src.html_generator import HTMLGenerator
from src.data_aggregator import DataAggregator

def main():
    # Initialize modules
    query_builder = QueryBuilder(int(os.getenv('NUMBER_OF_QUERIES')))
    search_executor = SearchExecutor()
    aggregator = DataAggregator('data/data.json')
    html_generator = HTMLGenerator()
    
    # Build the search query
    query_data = query_builder.get_query_data()
    
    # Execute the search and get PDF links
    links = search_executor.execute_search(query_data)
    
    # Continue with aggregating and generating HTML
    for url in links:
        # Aggregate data for grants.json and html
        found_data = aggregator.add_grant_data(query_data, url)
        # Generating HTML 
        html_generator.generate_html(found_data)

if __name__ == "__main__":
    main()
