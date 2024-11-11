<script>
    document.getElementById('search-input').addEventListener('input', function() {
        var query = this.value.toLowerCase();
        var rows = document.querySelectorAll('table tbody tr');

        rows.forEach(function(row) {
            var nombre = row.querySelector('td:nth-child(1) .text-base').textContent.toLowerCase();
            var facultad = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
            var especialidad = row.querySelector('td:nth-child(3)').textContent.toLowerCase();
            var categoria = row.querySelector('td:nth-child(4)').textContent.toLowerCase();
            var fechaContratacion = row.querySelector('td:nth-child(5)').textContent.toLowerCase();

            if (nombre.includes(query) || facultad.includes(query) || especialidad.includes(query) || categoria.includes(query) || fechaContratacion.includes(query)) {
                row.style.display = ''; // Mostrar la fila
            } else {
                row.style.display = 'none'; // Ocultar la fila
            }
        });
    });
</script>