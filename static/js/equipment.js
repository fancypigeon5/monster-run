const equipModal = new bootstrap.Modal(document.getElementById("equipModal"));
const equipable = document.getElementsByClassName('equipable');
const equipConfirm = document.getElementById("equipConfirm");
const equipForm = document.getElementById('equipForm')

for (let equipment of equipable) {
    equipment.addEventListener("click", (e) => {
      let equipmentId = e.currentTarget.getAttribute("equipment_id");
      equipForm.setAttribute('action', `equip/${equipmentId}`)
      equipModal.show();
    });
}