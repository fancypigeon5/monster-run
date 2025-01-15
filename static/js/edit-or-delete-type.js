const equipmentItems = document.getElementsByClassName('edit-equipment');
const modal = new bootstrap.Modal(document.getElementById('editEquipModal'));
const editButton = document.querySelector('#editEquipModal .btn-primary');
const deleteButton = document.querySelector('#editEquipModal .btn-danger');


for (let item of equipmentItems) {
    item.addEventListener('click', (e) => {
        let equipmentId = e.currentTarget.getAttribute('data-equipment-id');
        editButton.setAttribute('href', `edit_equipment_type/${equipmentId}`);
        deleteButton.setAttribute('href', `delete_equipment_type/${equipmentId}`);
        modal.show();
    });
}