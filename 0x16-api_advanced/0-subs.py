import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to avoid being blocked
    headers = {'User-Agent': 'my-reddit-subscriber-counter/0.1'}
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit does not exist or there's another issue, return 0
            return 0
    except requests.RequestException:
        # In case of any request exception, return 0
        return 0

