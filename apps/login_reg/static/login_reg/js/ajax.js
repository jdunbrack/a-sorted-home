$('#reg-fname').keyup(function(e) {

    data = $('#reg').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-name",
        data: data,
        success: function (response) {
            $('#name_warn').html(response)
        }
    });

});

$('#reg-lname').keyup(function(e) {

    data = $('#reg').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-name",
        data: data,
        success: function (response) {
            $('#name_warn').html(response)
        }
    });

});

$('#email').keyup(function(e) {

    data = $('#reg').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-email",
        data: data,
        success: function (response) {
            $('#email_warn').html(response)
        }
    });

});

$('#pw-entry').keyup(function(e) {

    data = $('#reg').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-pw",
        data: data,
        success: function (response) {
            $('#pw_warn').html(response);
        }
    });

});

$('#pw-confirm').keyup(function(e) {

    data = $('#reg').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-pw",
        data: data,
        success: function (response) {
            $('#pw_warn').html(response);
        }
    });

});

$('#bday').focusout(function() {

    data = $('#reg').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-age",
        data: data,
        success: function (response) {
            $('#age_warn').html(response);
        }
    });

});
