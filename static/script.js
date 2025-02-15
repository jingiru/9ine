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
    if (code === "9ineVIP") {  // ✅ 올바른 인증 코드
        window.location.href = "https://www.youtube.com/playlist?list=PL1234567890";  // 🔗 이동할 링크
    } else if (code !== null) {  // 🚫 잘못된 코드 입력 시
        alert("인증 코드가 올바르지 않습니다. 다시 시도해주세요.");
    }
}
