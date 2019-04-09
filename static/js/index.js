
$(document).ready(function () {
    $("#success-alert").hide();
    $("#danger-alert").hide();
});

function click_on() {
    $.ajax({
        type: 'GET',
        url: '/light/on',
        contentType: "application/json charset=utf-8",
        traditional: true,
        dataType: "json",
        success: function () {
            console.log("SUCCESS on button click !! ")
            $("#success-alert").fadeTo(2000, 500).slideUp(300, function () {
                $("#success-alert").slideUp(300);
            });
        },
        error: function () {
            console.log("THIS IS THE ERROR");
        }
    });
}

function click_off() {
    $.ajax({
        type: 'GET',
        url: '/light/off',
        contentType: "application/json charset=utf-8",
        traditional: true,
        dataType: "json",
        success: function () {
            console.log("SUCCESS off button click !! ")
            $("#danger-alert").fadeTo(2000, 500).slideUp(300, function () {
                $("#danger-alert").slideUp(300);
            });
        },
        error: function () {
            console.log("THIS IS THE ERROR");
        }
    });
}



