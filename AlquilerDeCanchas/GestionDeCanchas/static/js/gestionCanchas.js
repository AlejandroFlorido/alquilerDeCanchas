const btnEliminar = document.querySelectorAll(".btnEliminar");

btnEliminar.forEach(btn => {
    btn.addEventListener('click', e => {
        const confirmacion = confirm('¿Seguro de eliminar la Cancha seleccionada?');
        
    });
});