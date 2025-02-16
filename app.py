from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

VALID_AUTH_CODE = "9ineVIP"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    auth_code = data.get('auth_code')

    if auth_code == VALID_AUTH_CODE:
        return jsonify(success=True, redirect_url=url_for('performance_videos_mbship'))  # 🔄 페이지 이동
    else:
        return jsonify(success=False)  # ❌ 인증 실패 시 JSON 응답


@app.route('/performance-videos')
def performance_videos():
    return render_template('performance_videos.html')

@app.route('/performance-videos-mbship')
def performance_videos_mbship():
    return render_template('performance_videos_mbship.html')  # 🔒 회원 전용 페이지


@app.route('/practice-videos')
def practice_videos():
    return render_template('practice_videos.html')

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)








