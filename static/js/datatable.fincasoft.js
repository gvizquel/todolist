$(document).ready(function () {
    var table = $('#example').DataTable({

        paging: true,
        lengthChange: false,
        searching: true,
        ordering: true,
        info: true,
        autoWidth: false,
        language: {
            lengthMenu: "Mostrar _MENU_ registros por página",
            zeroRecords: "Lo sentimos, no encontramos nada",
            info: "Mostrando la página _PAGE_ de _PAGES_",
            infoEmpty: "Sin registros disponibles",
            infoFiltered: "(Filtrados de untotal de _MAX_ registros)",
            search: "Buscar: ",
            paginate: {
                first: "Primero",
                last: "Último",
                next: "Siguiente",
                previous: "Previo"
            },
            buttons: {
                copy: "Copiar"
            },
            decimal: "-",
            thousands: "."
        },
        buttons: ['copy', 'csv', 'pdf']
    });

    table.buttons().container()
        .appendTo('#example_wrapper .col-sm-6:eq(0)');

});