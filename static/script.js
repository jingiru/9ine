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
                window.location.href = data.redirect_url;  // 🔄 특정 페이지로 이동
            } else {
                document.getElementById("auth-error").innerText = "❌ 인증 코드가 올바르지 않습니다.";
                document.getElementById("auth-error").style.display = "block"; // 오류 메시지 표시
            }
        })
        .catch(error => console.error("Error:", error));
    }
}


document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector(".member-video-list")) {
        // 비디오 정보를 객체 배열로 관리
        const videoData = [
            {
                url: "https://www.youtube.com/embed/pU7b1pv-fqs",
                title: "Intro리버 우아하게"
            },
            {
                url: "https://www.youtube.com/embed/XnjY9kA_Yoo",
                title: "프리키디키 슈퍼노바"
            },
            {
                url: "https://www.youtube.com/embed/TPmkIFq9x6I",
                title: "첫 만남은 계획대로 되지 않아"
            },
            {
                url: "https://www.youtube.com/embed/325hDdR4vUY",
                title: "드라마"
            },
            {
                url: "https://www.youtube.com/embed/Dl2UI8x3PuY",
                title: "미야오"
            },
            {
                url: "https://www.youtube.com/embed/eXIssT7Lous",
                title: "매니악"
            },
            {
                url: "https://www.youtube.com/embed/RQ0tNcwB6k0",
                title: "ABCD"
            },
            {
                url: "https://www.youtube.com/embed/5tA1Q1KRlIg",
                title: "이글루"
            },
            {
                url: "https://www.youtube.com/embed/qvsHDbc72r0",
                title: "이다슬"
            },
            {
                url: "https://www.youtube.com/embed/HhaBv8x6BDA",
                title: "위플래시"
            },
            {
                url: "https://www.youtube.com/embed/SjaLYG7ejdI",
                title: "아마겟돈"
            },
            {
                url: "https://www.youtube.com/embed/nMIzlwWmtsQ",
                title: "How Sweet & Supernatural"
            },
            {
                url: "https://www.youtube.com/embed/y4anHeXiNyg",
                title: "Bloodline Banji"
            },
            {
                url: "https://www.youtube.com/embed/mKbjVVPlr60",
                title: "Supersonic Sheesh"
            },
            {
                url: "https://www.youtube.com/embed/gaVYGA4EGsw",
                title: "Silver tooth 백전무패"
            },
            {
                url: "https://www.youtube.com/embed/E7-TbeuoF1s",
                title: "아파트"
            },
            {
                url: "https://www.youtube.com/embed/Qy1eroUGIC8",
                title: "실버투스 백전무패 후방샷"
            },
            {
                url: "https://www.youtube.com/embed/W9GvgJXEQ_M",
                title: "빅버스트 세로 버전"
            },
            {
                url: "https://www.youtube.com/embed/t3mxiaJoSac",
                title: "하우스윗 세로 버전"
            },
            {
                url: "https://www.youtube.com/embed/yXMAqrvJHvc",
                title: "마블 룰렛 추첨 실황"
            }
        ];

        const videoContainer = document.querySelector(".member-video-list");
        
        videoData.forEach(video => {
            const videoDiv = document.createElement("div");
            videoDiv.classList.add("member-video-container");
            videoDiv.innerHTML = `
                <div class="video-title">${video.title}</div>
                <iframe src="${video.url}" allowfullscreen></iframe>
            `;
            videoContainer.appendChild(videoDiv);
        });

        // 가로 스크롤을 부드럽게 하기 위한 이벤트 리스너
        videoContainer.addEventListener("wheel", (evt) => {
            evt.preventDefault();
            videoContainer.scrollLeft += evt.deltaY;
        });
    }
});
