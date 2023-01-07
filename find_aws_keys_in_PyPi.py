import requests

def search_pypi(query):
  # Search PyPi for the given query
  response = requests.get(f'https://pypi.org/search/?q={query}')
  response.raise_for_status()

  # Extract the search results from the response
  search_results = response.json()['results']

  # Iterate through the search results and print the project names
  for result in search_results:
    print(result['name'])

# Test the function with a query for AWS keys
search_pypi('AWS key')
