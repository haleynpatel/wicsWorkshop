import os
from flask import Flask, render_template, request, redirect, url_for
from prometheus_client import Counter, generate_latest, CollectorRegistry

app = Flask(__name__)

# Create a Prometheus registry
registry = CollectorRegistry()
CLICK_COUNT = Counter('button_clicks_total', 'Total number of button clicks', registry=registry)
REQUEST_COUNT = Counter('page_requests_total', 'Total number of page requests', registry=registry)

@app.route('/', methods=['GET', 'POST'])
def index():
    REQUEST_COUNT.inc()
    if request.method == 'POST':
        CLICK_COUNT.inc()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    # Expose metrics to Prometheus
    return generate_latest(registry), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

