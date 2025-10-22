import time
import socket
import redis
from flask import Flask

app = Flask(__name__)

# Connect to Redis container (service name from docker-compose)
redis_client = redis.Redis(host='redis', port=6379, db=0)

def get_visit_count(max_retries=5, delay=0.5):
    """Increment and return the number of visits, retrying if Redis is not ready."""
    retries = max_retries
    while retries > 0:
        try:
            return redis_client.incr('visit_count')
        except redis.exceptions.ConnectionError:
            retries -= 1
            time.sleep(delay)
    raise ConnectionError("Could not connect to Redis after multiple retries.")

@app.route('/')
def home():
    try:
        count = get_visit_count()
        hostname = socket.gethostname()
        return f"""
        <html>
            <head><title>Flask + Redis Counter</title></head>
            <body style="font-family: sans-serif; text-align: center; margin-top: 100px;">
                <h1>Hello from <span style="color:#0078D7;">Soulayman</span>!</h1>
                <h2>You've visited this page <span style="color:green;">{count}</span> times.</h2>
                <p><b>Container Host:</b> {hostname}</p>
                <p><b>Status:</b> Connected to Redis ✅</p>
            </body>
        </html>
        """
    except Exception as e:
        return f"<h2>❌ Error connecting to Redis: {str(e)}</h2>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

