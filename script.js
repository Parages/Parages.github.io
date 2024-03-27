// script.js

const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
const particles = [];

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 2 + 1;
        this.speedX = (Math.random() - 0.5) * 0.05; // 非常缓慢的速度
        this.speedY = (Math.random() - 0.5) * 0.05; // 非常缓慢的速度
        this.life = Math.random() * 900; // 长生命周期
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.size > 0.2) this.size -= 0.05;

        this.life -= 1;

        if (this.life <= 0) {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 1;
            this.speedX = (Math.random() - 0.5) * 0.05;
            this.speedY = (Math.random() - 0.5) * 0.05;
            this.life = Math.random() * 1000;
        }
    }

    draw() {
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

function createParticles() {
    for (let i = 0; i < 10; i++) { // 减少粒子数量
        particles.push(new Particle());
    }
}

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (const particle of particles) {
        particle.update();
        particle.draw();
    }

    requestAnimationFrame(animateParticles);
}

function getRandomSpacing(min, max) {
    return Math.random() * (max - min) + min;
}

function updateLetterSpacing() {
    const paragraph = document.getElementById('randomSpacing');
    const randomSpacingValue = getRandomSpacing(40, 230) + 'px'; // 调整范围和单位
    paragraph.style.letterSpacing = randomSpacingValue;

 
   
  // 设置 transition 为 none
  paragraph.style.transition = 'none';
  paragraph.style.letterSpacing = randomSpacingValue;

  // 强制浏览器重新计算样式，使变化立即生效
  void paragraph.offsetWidth;

  // 恢复 transition
  paragraph.style.transition = '';
}

// 设置间隔时间为200毫秒
setInterval(updateLetterSpacing, 1500);  
   

 // 使用 setTimeout 来延迟显示弹窗
 setTimeout(function() {
    // 创建弹窗元素
    var popup = document.createElement('div');
    popup.innerHTML = '<p>建议使用笔电/手机横屏</p>';
    popup.style.position = 'fixed';
    popup.style.top = '50%';
    popup.style.left = '50%';
    popup.style.transform = 'translate(-50%, -50%)';
    popup.style.backgroundColor = 'black'; // 黑底
            popup.style.color = 'white'; // 白字
    popup.style.padding = '20px';
    popup.style.border = '2px solid black';
    popup.style.fontSize = '30px';
    

    // 将弹窗添加到 body 中
    document.body.appendChild(popup);

    // 使用 setTimeout 再延迟三秒后移除弹窗
    setTimeout(function() {
        document.body.removeChild(popup);
    }, 3000);

}, 0); // 使用0毫秒延迟确保在页面加载后立即执行



// 初始化
updateLetterSpacing();

createParticles();
animateParticles();


