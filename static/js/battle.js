const damageRoll = document.getElementById('damageRoll');
const rollBox = document.getElementById('rollBox');
const maxDamage = damageRoll.getAttribute('max_damage');
const strikeTitle = document.getElementById('strikeTitle');
const strikeForm = document.getElementById('strikeForm');
const damagePost = document.getElementById('damagePost');
const strikeFormButton = document.getElementById('strikeFormButton');
const turn = document.getElementById('turnIndicator').getAttribute('turn');
let damage;
let randomInterval;

function damageRollInterval() {
    randomInterval = setInterval(() => {
        damage = Math.floor(Math.random()*maxDamage);
        rollBox.innerText = damage;
        rollBox.setAttribute('current_damage', damage);
    }, 50);
    
}

function damageRollHandler() {
    damageRollInterval();
    damageRoll.addEventListener('click', () => {
        clearInterval(randomInterval);
        damagePost.setAttribute('value', damage);
        strikeTitle.innerHTML = `Do ${damage} damage`;
        strikeForm.classList.remove('d-none');
        strikeForm.classList.add('d-flex');
    }, {once: true});
}

function stopEnemyRoll() {
    clearInterval(randomInterval);
    damagePost.setAttribute('value', damage);
    strikeTitle.innerHTML = `You take ${damage} damage`;
    strikeForm.classList.remove('d-none');
    strikeForm.classList.add('d-flex');
    strikeFormButton.innerText = 'My Turn'
}

if (turn == 'you') {
    damageRoll.addEventListener('click', damageRollHandler, {once: true});
} else if (turn == 'enemy') {
    damageRollInterval();
    setInterval(stopEnemyRoll, 1500)
}
