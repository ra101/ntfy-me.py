import os
import requests


def me(message='ping', high_priority=False, scheme='https', topic=None):
    """
    Sends a notification to ntfy.sh using the provided environment variable topic.

    Args:
        message (str): The message to send.
        high_priority (bool): If True, use higher priority.
        scheme (str): URL scheme (default is 'https').
        topic_env (str): Environment variable name for the topic.
    """
    topic = os.getenv('NTFY_TOPIC', topic)
    if not topic:
        raise AttributeError(f"Topic is not set.")

    url = f"{scheme}://ntfy.sh/{topic}"
    priority = 5 if high_priority else 4
    headers = {'Title': 'Notification', 'Priority': str(priority)}

    try:
        response = requests.post(url, data=message, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Notification failed: {e}")