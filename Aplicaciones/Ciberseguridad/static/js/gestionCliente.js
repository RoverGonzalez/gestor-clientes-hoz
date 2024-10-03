document.addEventListener('DOMContentLoaded', function() {
    
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmar = confirm('¿Seguro desea eliminar el Cliente?')
            if (!confirmar) {
                e.preventDefault()
            }
        })
    })
})