const damageRoll = document.getElementById('damageRoll');


function changeinnertext(damage) {
    setTimeout(100);
    rollBox.innerText = damage;
}

damageRoll.addEventListener('click', (e) => {
    let maxDamage = e.currentTarget.getAttribute('max_damage');
    for (let i = 0; i < 10; i++) {
        const rollBox = document.getElementById('rollBox');
        damage = Math.floor(Math.random()*maxDamage);
        rollBox.innerText = damage;
        setInterval(100);
    }
})