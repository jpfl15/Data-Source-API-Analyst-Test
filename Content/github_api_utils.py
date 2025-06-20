import requests

def safe_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except Exception as e:
        print("Error:", e)
    return {}

def paginated_repo_search(query="python", headers=None, max_pages=3):
    all_items = []
    for page in range(1, max_pages + 1):
        url = f"https://api.github.com/search/repositories?q={query}&per_page=30&page={page}"
        data = safe_request(url, headers)
        all_items.extend(data.get("items", []))
    return all_items

def get_commits(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    return safe_request(url, headers)

def get_contents(owner, repo, path="", headers=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    return safe_request(url, headers)