from typing_extensions import Optional
from requests import post as request
from os import getenv
from cli.runcmd import runcmd

GITHUB_API_URL = "https://api.github.com"
TOKEN = getenv("github_okuldaogrenilen_token")

# öncelikle bir github deposu oluşturulacak.

# oluşturulan bu github deposunu, yeni oluşturulan klasör içerisine init edecem.

class repository:
    def __init__(self):
        pass

    @staticmethod
    def create(repo_name: str, private: bool = False):
        url = f"{GITHUB_API_URL}/user/repos"
        
        headers = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "name": repo_name,
            "private": private
        }

        response = request(url, json=data, headers=headers)

        if response.status_code == 201:
            # init repository
            runcmd(f"git init {repo_name}", "initializing repository...")

            # set remote
            runcmd(f"git remote add origin https://github.com/OkuldaOgrenilen/{repo_name}.git", "setting remote address...")

            # set branch
            runcmd(f"git branch -M main", "setting branch...")
        else:
            print("     [bold red]Github repository oluşturulurken bir sorun meydana geldi!![/bold red]")

if __name__ == "__main__":
    repository.create("kariyer-planlama")