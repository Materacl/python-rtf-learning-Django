let sidebarOpen = false; // Изначально панель открыта

function toggleSidebar() {
    const sidebar = document.querySelector('.main-sidebar');
    const container = document.querySelector('.container');
    const toggleButton = document.querySelector('.toggle-sidebar');

    if (sidebarOpen) {
        sidebar.style.width = '0';
        container.style.filter = 'none'; // Убираем блюр при закрытии меню
        toggleButton.innerHTML = '☰';
    } else {
        container.style.filter = 'blur(5px)'; // Добавляем блюр перед изменением ширины меню
        sidebar.style.width = '270px';
        toggleButton.innerHTML = '✖';
    }

    sidebarOpen = !sidebarOpen;

    // Добавляем/удаляем класс для изменения цвета кнопки
    toggleButton.classList.toggle('opened', sidebarOpen);
}

