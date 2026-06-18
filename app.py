from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    visits = cache.incr('visits')
    return f"This page has been visited {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)