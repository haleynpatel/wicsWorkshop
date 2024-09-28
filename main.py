from flask import Flask, render_template, jsonify, request, redirect, url_for
import os
from prometheus_client import Counter, generate_latest, CollectorRegistry

app = Flask(__name__)

# Prometheus metrics setup
registry = CollectorRegistry()
CLICK_COUNT = Counter('button_clicks_total', 'Total number of button clicks', registry=registry)
REQUEST_COUNT = Counter('page_requests_total', 'Total number of page requests', registry=registry)

# Route for the main page with a button
@app.route('/', methods=['GET', 'POST'])
def index():
    REQUEST_COUNT.inc()  # Increment page requests counter
    if request.method == 'POST':
        CLICK_COUNT.inc()  # Increment button clicks counter when the button is clicked
        return redirect(url_for('index'))  # Redirect back to the main page after the button is clicked
    return render_template('index.html')  # Render the HTML page with the button

# Route for the /metrics endpoint for Prometheus to scrape
@app.route('/metrics')
def metrics():
    return generate_latest(registry), 200, {'Content-Type': 'text/plain; charset=utf-8'}

# Flask app entry point
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

