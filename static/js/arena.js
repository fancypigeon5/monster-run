const battleModal = new bootstrap.Modal(document.getElementById("battleModal"));
const battleButton = document.getElementById('battleButton');




battleButton.addEventListener('click', () => {
    battleModal.show();
})