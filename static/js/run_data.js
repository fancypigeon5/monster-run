const runModal = new bootstrap.Modal(document.getElementById("runModal"));
const enterRun = document.getElementById('enterRun');
const unlockButton = document.getElementById('unlockRunButton');
const recoverButton = document.getElementById('recoverRunButton');
const unlockRunForm = document.getElementById('unlockRunForm');
const recoverRunForm = document.getElementById('recoverRunForm');
const runFormChoice = document.getElementById('runFormChoice');



enterRun.addEventListener('click', () => {
    runFormChoice.classList.remove('d-none');
    unlockRunForm.classList.add('d-none');
    recoverRunForm.classList.add('d-none');
    unlockButton.addEventListener('click', () => {
        runFormChoice.classList.add('d-none');
        unlockRunForm.classList.remove('d-none');
    })
    recoverButton.addEventListener('click', () => {
        runFormChoice.classList.add('d-none');
        recoverRunForm.classList.remove('d-none');
    })
    runModal.show();
})