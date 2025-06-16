import requests
import json
import os

# --- Configuration ---
SOURCEGRAPH_URL = os.environ.get("SOURCEGRAPH_URL", "https://sourcegraph.com")
SOURCEGRAPH_ACCESS_TOKEN = os.environ.get("SOURCEGRAPH_ACCESS_TOKEN", "sgp_9bea5fb6370f0a6e01bc56b7a99c5b335f32a4c0") # Get this from your Sourcegraph user settings

if not SOURCEGRAPH_ACCESS_TOKEN:
    print("Please set the SOURCEGRAPH_ACCESS_TOKEN environment variable.")
    exit(1)

# --- GraphQL Query ---
def search_sourcegraph(query, repo_filter=None, file_filter=None, limit=10):
    """
    Performs a code search on Sourcegraph and returns matching code snippets.

    Args:
        query (str): The search query (e.g., "func createUser").
        repo_filter (str, optional): A regex to filter repositories (e.g., "github.com/my-org/").
        file_filter (str, optional): A regex to filter files (e.g., ".*\.go$").
        limit (int, optional): Maximum number of results to return.
    Returns:
        list: A list of dictionaries, each representing a search result.
    """
    graphql_query = """
    query CodeSearch($query: String!, $first: Int) {
      search(query: $query, first: $first) {
        results {
          __typename
          ... on FileMatch {
            repository {
              name
            }
            file {
              path
            }
            lineMatches {
              preview
              lineNumber
              offsetAndLengths
            }
          }
        }
      }
    }
    """

    variables = {
        "query": f"type:file {query}",
        "first": limit,
    }

    if repo_filter:
        variables["query"] += f" repo:{repo_filter}"
    if file_filter:
        variables["query"] += f" file:{file_filter}"

    headers = {
        "Authorization": f"token {SOURCEGRAPH_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "query": graphql_query,
        "variables": variables,
    }

    try:
        response = requests.post(f"{SOURCEGRAPH_URL}/.api/graphql", headers=headers, data=json.dumps(payload))
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()

        results = []
        if data and "data" in data and "search" in data["data"] and "results" in data["data"]["search"]:
            for item in data["data"]["search"]["results"]:
                if item["__typename"] == "FileMatch":
                    for line_match in item["lineMatches"]:
                        results.append({
                            "repository": item["repository"]["name"],
                            "file": item["file"]["path"],
                            "line": line_match["lineNumber"],
                            "code_snippet": line_match["preview"].strip()
                        })
        return results

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        if response:
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
        return []

# --- Example Usage ---
if __name__ == "__main__":
    # Search for all definitions of 'authenticateUser' in TypeScript files
    search_term = "func authenticateUser"
    repository_scope = "github.com/sourcegraph/" # Example: limit to Sourcegraph's own repos
    file_type = ".*\.ts$" # Example: only TypeScript files

    print(f"Searching for '{search_term}' in '{repository_scope}' (TypeScript files)...")
    code_snippets = search_sourcegraph(search_term, repo_filter=repository_scope, file_filter=file_type, limit=5)

    if code_snippets:
        print("\nFound code snippets:")
        for snippet in code_snippets:
            print(f"---")
            print(f"Repo: {snippet['repository']}")
            print(f"File: {snippet['file']} (Line: {snippet['line']})")
            print(f"Code:\n{snippet['code_snippet']}")
    else:
        print("No matching code snippets found.")

    print("\n--- Searching for database connection examples ---")
    db_connection_snippets = search_sourcegraph("connect to database", limit=3)
    if db_connection_snippets:
        print("\nFound database connection examples:")
        for snippet in db_connection_snippets:
            print(f"---")
            print(f"Repo: {snippet['repository']}")
            print(f"File: {snippet['file']} (Line: {snippet['line']})")
            print(f"Code:\n{snippet['code_snippet']}")
    else:
        print("No database connection examples found.")
