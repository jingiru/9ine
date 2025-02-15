from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice-videos')
def practice_videos():
    return render_template('practice_videos.html')

@app.route('/performance-videos')
def performance_videos():
    return render_template('performance_videos.html')

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

