import os
from src.query_builder import QueryBuilder
from src.search_executor import SearchExecutor
from src.html_generator import HTMLGenerator
from src.data_aggregator import DataAggregator

def main():
    try:
        # Initialize modules
        query_builder = QueryBuilder(int(os.getenv('NUMBER_OF_QUERIES')))
        search_executor = SearchExecutor()
        aggregator = DataAggregator('data/data.json')
        html_generator = HTMLGenerator()
        
        # Build the search query
        query_data = query_builder.get_query_data()
        
        # Execute the search and get PDF links
        # links = search_executor.execute_search(query_data)
        
        # Stub for testing:
        links = ['https://www.stata.com/manuals13/semexample26.pdf', 'http://ekladata.com/5jpNRcdcAmpwzanYQ-hOFjPFREU/L2-GROUPS-3-4-5-6-THEME-VERSION.pdf', 'https://egusphere.copernicus.org/preprints/2024/egusphere-2023-2885/egusphere-2023-2885.pdf', 'https://www.analog.com/media/en/technical-documentation/data-sheets/4636f.pdf', 'https://www.sigmaaldrich.com/content/dam/sigma-aldrich/docs/Sigma/General_Information/bromelain_inhibitor.pdf', 'https://proceedings.neurips.cc/paper/2019/file/fc2c7c47b918d0c2d792a719dfb602ef-Paper.pdf', 'https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/4/24696/files/2016/06/psumac2016-51-Bash-In-A-NutShell.pdf', 'https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/kinetis%40tkb/326/1/Porting-Fatfs-file-system-to-KL26-SPI-SD-code.pdf', 'https://courses.cs.washington.edu/courses/cse341/10wi/exams/final.pdf', 'https://files.microstrain.com/tech-notes/orientation-conversion-formulas.pdf']
        print("Found links:", links)
        
        # Aggregate data for grants.json and html
        found_data = aggregator.add_found_data(query_data, links)
        print("Aggregated data:", found_data)
        
        # Generating HTML 
        # html_generator.generate_html(found_data)
    except Exception as e:
        print(f"An error occurred in main: {e}")

if __name__ == "__main__":
    main()
