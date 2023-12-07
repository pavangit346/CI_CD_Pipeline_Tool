import requests
import json
import subprocess

def get_commits(repo_url):
    """Gets the latest commits for a given repository URL."""
    response = requests.get(repo_url)
    if response.status_code == 200:
        commits = json.loads(response.content)
        return commits
    else:
        raise Exception("Could not get commits from GitHub API.")


def main():
    """The main function."""
    # Get the repository URL from the user.
    repo_url = "https://api.github.com/repos/CharismaticOwl/ci-cd--herovired-1/commits"

    # Get the latest commits.
    commits = get_commits(repo_url)

    sha_remote = str(commits[0]["sha"])

    sha_local = str(subprocess.call(['sh', '/root/getcurrenthash.sh']))[0:-2]

    print(sha_remote, sha_local)

    if sha_local != sha_remote:
        subprocess.call(['sh', '/root/web.sh'])
    else:
        print("Already up to date.")

if __name__ == "__main__":
    main()
