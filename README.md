# 🎶 Haley's Observability Workshop - Flask with Prometheus Metrics and a Disco-Themed Button

This project was a fun and interactive way that I demonstrated **observability** concepts using Flask, Prometheus metrics, and a disco-themed button that users can click to generate metrics. It uses a Flask web application with Prometheus to track metrics such as button clicks and page requests.

Attendees were able to access the deployed application, and spam requests to the button. The surge in requests was captured and presented on a visual dashboard to demonstrate how observability can help detect high-volume events. 

## Features

- **Flask Web App**: A simple Flask app with two main pages.
- **Disco-Themed Button**: A vibrant button that users can click to generate metrics.
- **Prometheus Metrics**: Tracks and exposes metrics such as button clicks and page requests.

## Project Structure

```plaintext
wicsWorkshop/
├── app.py                   # Main Flask app
├── static/                  # Static files such as images, CSS
│   └── images/              # Image directory
├── templates/               # HTML templates
│   ├── index.html           # Main HTML file
├── requirements.txt         # Python dependencies
└── README.md                # Project readme file

![image](static\images\applicationImage.PNG)
