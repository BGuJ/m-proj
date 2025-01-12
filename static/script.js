function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    const menuTexts = document.querySelectorAll('.menu-text');
    if (sidebar.style.width === '60px') {
        sidebar.style.width = '200px';
        menuTexts.forEach(text => {
            text.style.display = 'inline';
        });
    } else {
        sidebar.style.width = '60px';
        menuTexts.forEach(text => {
            text.style.display = 'none';
        });
    }
}
