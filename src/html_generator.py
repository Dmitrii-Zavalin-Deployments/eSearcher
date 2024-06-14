import os

class HTMLGenerator:
    def generate_html(self, found_data, output_file='information.html'):
        # Check if the output file exists and delete it if it does
        if os.path.exists(output_file):
            os.remove(output_file)

        # Read the reviewed links
        with open('data/reviewed_links.txt', 'r') as file:
            reviewed_links = file.read().splitlines()

        # Start of the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Search Details</title>
            <style>
                table {{
                    width: 100%; /* Adjusted table width */
                    border-collapse: collapse;
                    table-layout: fixed; /* Fixed table layout to manage column widths */
                }}
                table, th, td {{
                    border: 1px solid black;
                    padding: 10px;
                    text-align: left;
                    vertical-align: top; /* Align text to the top of the cell */
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                th:nth-child(1) {{ width: 20%; }} /* Criteria column */
                th:nth-child(2) {{ width: 80%; }} /* Links column */
                .tabcontent {{
                    display: none;
                }}
                .active-tab {{
                    display: block;
                }}
            </style>
        </head>
        <body onload="openTab(event, 'NewLinks')">
            <h1>Search Details</h1>
            <div class="tab">
                <button class="tablinks" onclick="openTab(event, 'NewLinks')">New Links</button>
                <button class="tablinks" onclick="openTab(event, 'ReviewedLinks')">Reviewed Links</button>
            </div>

            <div id="NewLinks" class="tabcontent">
                <h2>New Links</h2>
                <table>
                    <tr>
                        <th>Criteria</th>
                        <th>Queries, Links, Comments</th>
                    </tr>
                    {new_links_rows}
                </table>
            </div>

            <div id="ReviewedLinks" class="tabcontent">
                <h2>Reviewed Links</h2>
                <table>
                    <tr>
                        <th>Criteria</th>
                        <th>Queries, Links, Comments</th>
                    </tr>
                    {reviewed_links_rows}
                </table>
            </div>

            <script>
                function openTab(evt, tabName) {{
                    var i, tabcontent, tablinks;
                    tabcontent = document.getElementsByClassName("tabcontent");
                    for (i = 0; i < tabcontent.length; i++) {{
                        tabcontent[i].className = tabcontent[i].className.replace(" active-tab", "");
                    }}
                    tablinks = document.getElementsByClassName("tablinks");
                    for (i = 0; i < tablinks.length; i++) {{
                        tablinks[i].className = tablinks[i].className.replace(" active", "");
                    }}
                    document.getElementById(tabName).className += " active-tab";
                    if (evt) evt.currentTarget.className += " active";
                }}
                // Call openTab to set the default tab when the page loads
                document.addEventListener('DOMContentLoaded', (event) => {{
                    openTab(null, 'NewLinks');
                }});
            </script>
        </body>
        </html>
        """

        # Function to create rows HTML
        def create_rows_html(data):
            rows_html = ""
            for criteria, links in data.items():
                links_html = "<br>".join([f'<a href="{link}" target="_blank">{link}</a>' for link in links])
                rows_html += f"""
                    <tr>
                        <td>{criteria}</td>
                        <td>{links_html}</td>
                    </tr>
                """
            return rows_html

        # Categorize grants into new and reviewed
        new_links_data = {}
        reviewed_links_data = {}
        for criteria, links in found_data.items():
            new_links = [link for link in links if link not in reviewed_links]
            reviewed_links = [link for link in links if link in reviewed_links]
            if new_links:
                new_links_data[criteria] = new_links
            if reviewed_links:
                reviewed_links_data[criteria] = reviewed_links

        # Create rows HTML for New and Reviewed Links
        new_links_rows = create_rows_html(new_links_data)
        reviewed_links_rows = create_rows_html(reviewed_links_data)

        # Format the HTML content with the rows
        html_content = html_content.format(new_links_rows=new_links_rows, reviewed_links_rows=reviewed_links_rows)

        # Write the HTML content to the output file
        with open(output_file, 'w') as file:
            file.write(html_content)

        print(f"HTML file generated: {output_file}")


