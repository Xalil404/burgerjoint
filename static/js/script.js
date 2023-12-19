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

//Function to delete bookings & Deliveries
$(document).ready(function () {
    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); 
        var bookingId = button.data('booking-id'); 
        var deleteButton = $('#confirmDeleteButton');
        var deleteUrl = button.data('delete-url'); 
        deleteButton.attr('href', deleteUrl); 
    });
});

//Function to validate form fields data input
function validateForm() {
    var name = document.getElementById('id_name').value;
    var phoneNumber = document.getElementById('id_phone_number').value;
    var bookingDate = document.getElementById('id_booking_date').value;

    if (!name.replace(/\s/g, '').match(/^[a-zA-Z]+$/)) {
        alert('Name must contain only alphabetical characters.');
        return false;
    }

    if (!phoneNumber.replace(/\s|-/g, '').match(/^\d+$/)) {
        alert('Phone number must contain only numerical characters.');
        return false;
    }

    var today = new Date();
    var selectedDate = new Date(bookingDate);

    if (selectedDate < today) {
        alert('Booking date cannot be in the past.');
        return false;
    }

    return true;
};
