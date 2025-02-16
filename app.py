from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

VALID_AUTH_CODE = "9ineVIP"
SECRET_URL = "https://www.youtube.com/playlist?list=PLKK7CKrIcg5VUwbQ4srbldARWuER8QmmE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/practice-videos')
def practice_videos():
    return render_template('practice_videos.html')

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    auth_code = data.get('auth_code')

    if auth_code == VALID_AUTH_CODE:
        return jsonify(success=True, redirect_url=SECRET_URL)  # ✅ 올바른 경우 유튜브 링크 반환
    else:
        return jsonify(success=False)  # ❌ 잘못된 코드일 경우


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

