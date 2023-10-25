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




