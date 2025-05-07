document.addEventListener('DOMContentLoaded', () => {
    const menuIcono = document.querySelector('.menu-icono');
    const menuDesplegable = document.querySelector('.menu-desplegable');
    
    menuIcono.addEventListener('click', () => {
        menuDesplegable.classList.toggle('visible');
        menuIcono.classList.toggle('abrir');
    });
});
