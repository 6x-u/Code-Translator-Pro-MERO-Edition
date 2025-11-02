import requests
import base64

class GitHubExplorer:
    def __init__(self):
        self.base_url = "https://api.github.com"
    
    def search_repositories(self, query, language=None, limit=10):
        try:
            params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': limit}
            if language:
                params['q'] += f" language:{language}"
            
            response = requests.get(f"{self.base_url}/search/repositories", params=params)
            if response.status_code == 200:
                return response.json().get('items', [])
            return []
        except:
            return []
    
    def get_repository_contents(self, owner, repo, path=""):
        try:
            url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            return []
        except:
            return []
    
    def get_file_content(self, owner, repo, path):
        try:
            url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
            response = requests.get(url)
            if response.status_code == 200:
                content = response.json().get('content', '')
                return base64.b64decode(content).decode('utf-8')
            return None
        except:
            return None
