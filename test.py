import os
import requests
from github import Github
import pytz



# Initialize the GitHub API client
g = Github(GITHUB_TOKEN)

# Check rate limit status
rate_limit = g.get_rate_limit()
core_rate_limit = rate_limit.core

# Convert reset time to PST
reset_time_utc = core_rate_limit.reset
pst_timezone = pytz.timezone('America/Los_Angeles')
reset_time_pst = reset_time_utc.astimezone(pst_timezone)

print(f"Rate limit: {core_rate_limit.limit}")
print(f"Remaining: {core_rate_limit.remaining}")
print(f"Reset time (UTC): {reset_time_utc}")
print(f"Reset time (PST): {reset_time_pst}")


def fetch_org_members(org_name, token):
    url = f"https://api.github.com/orgs/{org_name}/members"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return []

def fetch_user_email(username, token):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("email")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

def main():
    members = fetch_org_members(ORG_NAME, GITHUB_TOKEN)
    for member in members:
        username = member["login"]
        email = fetch_user_email(username, GITHUB_TOKEN)
        if email:
            print(f"Username: {username}, Email: {email}")
        else:
            print(f"Username: {username}, Email: Not Public")

if __name__ == "__main__":
    main()
