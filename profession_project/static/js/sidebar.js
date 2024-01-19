let sidebarOpen = true; // Изначально панель открыта

function toggleSidebar() {
    const sidebar = document.querySelector('.main-sidebar');
    const content = document.querySelector('.content');
    const toggleButton = document.querySelector('.toggle-sidebar');

    if (sidebarOpen) {
        sidebar.style.width = '0';
        toggleButton.innerHTML = '☰'; // Изменение значка на ☰
    } else {
        sidebar.style.width = '500px';
        toggleButton.innerHTML = '✖'; // Изменение значка на ✖
    }

    sidebarOpen = !sidebarOpen;

    // Добавляем/удаляем класс для изменения цвета кнопки
    toggleButton.classList.toggle('opened', sidebarOpen);
}
