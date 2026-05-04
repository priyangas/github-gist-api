import requests

GITHUB_API = "https://api.github.com/users/{}/gists"

def fetch_gists(username: str):
    try:
        response = requests.get(GITHUB_API.format(username), timeout=5)
    except requests.exceptions.RequestException:
        raise Exception("External API failure")

    if response.status_code == 404:
        raise ValueError("User not found")

    if response.status_code != 200:
        raise Exception("GitHub API error")

    gists = response.json()

    return [
        {
            "id": gist["id"],
            "url": gist["html_url"],
            "files": list(gist["files"].keys())
        }
        for gist in gists
    ]