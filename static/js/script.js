//Function to toggle menu on homepage
$(document).ready(function() {
    $(".filter").click(function() {
        var filterValue = $(this).attr("data-filter");
        if (filterValue === "all") {
            $(".menu-item").show();
        } else {
            $(".menu-item").hide();
            $("." + filterValue).show();
        }
    });
});

//Function to delete booking
$(document).ready(function () {
    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); 
        var bookingId = button.data('booking-id'); 
        var deleteButton = $('#confirmDeleteButton');
        var deleteUrl = button.data('delete-url'); 
        deleteButton.attr('href', deleteUrl); 
    });
});
