document.addEventListener("DOMContentLoaded", function () {
    console.log("댄스 동아리 홈페이지가 로드되었습니다!");
});


document.addEventListener("DOMContentLoaded", function () {
    console.log("댄스 동아리 홈페이지가 로드되었습니다!");
});

function goHome() {
    window.location.href = "/home";  // Flask 라우트로 이동
}


// 🔐 회원 인증 코드 입력 및 검증
function requestAccess() {
    let code = prompt("회원 인증 코드를 입력하세요:");

    if (code) {
        fetch("/verify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ auth_code: code }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect_url;  // 🔗 유튜브 페이지로 이동
            } else {
                document.getElementById("auth-error").innerText = "❌ 인증 코드가 올바르지 않습니다.";
                document.getElementById("auth-error").style.display = "block"; // 오류 메시지 표시
            }
        })
        .catch(error => console.error("Error:", error));
    }
}
