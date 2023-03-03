
document.addEventListener('mousemove', (e) => {
        
    const mouseX = e.clientX;
    const mouseY = e.clientY;
    const eyes = document.querySelectorAll('.eye');
    const anchor = document.getElementById('anchor');
    const rekt = anchor.getBoundingClientRect();
    let anchorX = rekt.left + rekt.width / 2;
    let anchorY = rekt.top + rekt.height / 2;
    const angleDeg = angle(mouseX, mouseY, anchorX, anchorY);
    eyes.forEach(eye => {
        eye.style.transform = `rotate(${(angleDeg-90)}deg)`;
        anchor.style.filter= `hue-rotate(${angleDeg}deg)`;
    })
})



function angle(cx, cy, ex, ey) {
    const dy = ey - cy;
    const dx = ex - cx;
    const rad = Math.atan2(dy, dx);
    const def = rad * 180 / Math.PI;
    return def;
}