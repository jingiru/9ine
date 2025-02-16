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


# 게시글 저장 (임시 리스트, DB 대체 가능)
posts = []

@app.route('/board')
def board():
    return render_template('board.html', posts=posts)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        post_id = len(posts) + 1  # 게시글 ID
        posts.append({'id': post_id, 'title': title, 'author': author, 'content': content})
        return redirect(url_for('board'))
    return render_template('write.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "게시글을 찾을 수 없습니다.", 404



@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)








