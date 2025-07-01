# ntfy-me

A minimal Python utility to send notifications to [`ntfy.sh`](https://ntfy.sh) from your scripts or applications.

## Features

- Send push notifications to your `ntfy.sh` topic
- Adjustable priority (`high` or `normal`)
- Configurable scheme (HTTP/HTTPS)
- Uses environment variable for topic (no hardcoding!)

## Usage

```bash
export NTFY_TOPIC=my-topic-name
```

```python
import ntfy


# curl "https://ntfy.sh/${NTFY_TOPIC}" -d ping -h 'p: 4'
nyfy.me()

# curl "http://ntfy.sh/World" -d Hello -h 'p: 5'
nyfy.me(message='Hello', high_priority=True, scheme='http', topic=World)
```

Enjoy!
