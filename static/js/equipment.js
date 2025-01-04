const equipModal = new bootstrap.Modal(document.getElementById("equipModal"));
const equipable = document.getElementsByClassName('equipable');
const equipConfirm = document.getElementById("equipConfirm");
const equipForm = document.getElementById('equipForm');
const equipModalLabel = document.getElementById('equipModalLabel');
const equipped = document.getElementsByClassName('equipped');
const equipFormBody = document.getElementById('equipFormBody');


for (let equipment of equipable) {
    equipment.addEventListener("click", (e) => {
      let equipmentId = e.currentTarget.getAttribute('data-equipment-id');
      equipForm.setAttribute('action', `equip/${equipmentId}`);
      equipFormBody.classList.remove('d-none');
      equipModalLabel.innerText = 'Equip Item?';
      equipConfirm.innerText = 'Equip!';
      equipModal.show();
    });
};

for (let equipment of equipped) {
    equipment.addEventListener("click", (e) => {
        let equipmentId = e.currentTarget.dataset.equipmentId;
        equipForm.setAttribute('action', `unequip/${equipmentId}`);
        equipModalLabel.innerText = 'Unequip Item?';
        equipFormBody.classList.add('d-none');
        equipConfirm.innerText = 'Unequip!';
        equipModal.show();
    });
};