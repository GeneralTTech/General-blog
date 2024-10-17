function toggleDropdown(menuId) {
    const dropDownMenu = document.querySelector(`#${menuId}`);
    if (dropDownMenu.classList.contains('hidden')) {
        dropDownMenu.classList.remove('hidden');
    } else {
        dropDownMenu.classList.add('hidden');
    }
}




