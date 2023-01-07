import requests

# Set the GitHub API endpoint
api_endpoint = 'https://api.github.com'

# Set the GitHub API token
api_token = 'your-api-token'

# Set the headers for the API request
headers = {
  'Authorization': f'token {api_token}',
  'Accept': 'application/vnd.github+json'
}

def search_github(query):
  # Search GitHub for the given query
  response = requests.get(f'{api_endpoint}/search/code?q={query}', headers=headers)
  response.raise_for_status()

  # Extract the search results from the response
  search_results = response.json()['items']

  # Iterate through the search results and print the repository names and file paths
  for result in search_results:
    repo_name = result['repository']['name']
    file_path = result['path']
    print(f'API key found in {repo_name} at {file_path}')

# Test the function with a query for API keys
search_github('api_key')

# Test the function with a query for access/secret keys
search_github('access_key')
search_github('secret_key')
