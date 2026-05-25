"""Defining CLI and program structure:
- Running main program loop
- Command based, and terminates based on the terminating condition invoked by a command "exit"
"""

from requests import ConnectionError
import requests
import json

def main():
    RUN_PROGRAM = True
    print("GitHub user activity tracker program start!")
    print("Choose the number for the command you wish to execute:\n",
     "1. Return User's github activity\n", 
     "2. End program")

    commands = ['github-activity','end']
    while RUN_PROGRAM:
        user_input = int(input("Enter your command :=> ")   )
        match user_input:
            case 1:
                username = str(input("Enter the github username just as it appears to be: "))
                if username == '':
                    print("Please do not leave it blank")
                    continue
                github_activity(username)
                continue

            case 2:
                print("Program is ending...")
                RUN_PROGRAM = False


def github_activity(username):
    params = {'per_page': 5, 'page': 1}
    headers={'Accept': 'application/vnd.github+json'}
    # URL = f"https://api.github.com/{username}/events"
    URL = f"https://api.github.com/users/{username}/events/public"
    try:
        user_activity = requests.get(URL, headers=headers, params=params)
        if user_activity.status_code == 200:
            json_obj = user_activity.json()
            for event in json_obj:
                print(f"Event Type: {event['type']}")
                print(f"Repository: {event['repo']['name']}")
                print(f"Created At: {event['created_at']}\n")
        else: 
            print("Failed to load user activity ", user_activity.status_code)
    except Exception as e:
        print("Faced an error: ", e)
    

if __name__ == "__main__":
    main()
