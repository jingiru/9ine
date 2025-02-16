from flask import Flask, render_template, request, jsonify, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

SMTP_SERVER = "smtp.gmail.com"  # 본인의 SMTP 서버 사용 (hanmail은 smtp.daum.net)
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"  # 본인의 이메일
EMAIL_PASSWORD = "your_email_password"  # 앱 비밀번호 사용 (일반 비밀번호 X)
EMAIL_RECEIVER = "skyjjw79@hanmail.net"  # 공연 섭외 요청 받을 이메일




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


@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        event = data.get("event")
        date = data.get("date")
        message = data.get("message")

        email_subject = f"🎤 [공연 섭외 요청] {event} ({date})"
        email_body = f"""
        공연 섭외 요청이 접수되었습니다.
        
        📌 요청자: {name}
        📧 이메일: {email}
        📞 연락처: {phone}
        🎭 공연 행사명: {event}
        📅 공연 날짜: {date}

        💬 추가 요청 사항:
        {message}
        """

        msg = MIMEText(email_body)
        msg['Subject'] = email_subject
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        return jsonify(success=True)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)








