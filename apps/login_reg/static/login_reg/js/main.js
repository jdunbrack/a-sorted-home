$('#reg-form').hide();

function getCookie(c_name)
{
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

if ($('#logged_in').attr('value') == "true") {
    $('#my-acct-link').show();
    $('#logout-link').show();
    $('#login-link').hide();
} else if ($('#logged_in').attr('value') == "false") {
    $('#my-acct-link').hide();
    $('#logout-link').hide();
    $('#login-link').show();
}


$('.modal-toggler').click(function() {
    $('#reg-form').slideToggle('slow');
    $('#login-form').slideToggle('slow');
});

$('#reg-email').keyup(function() {
    let data = $('#register').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-email",
        data: data,
        success: function (response) {
            $('#email-warn').html(response)
        }
    });
});

$('#reg-pw-entry').keyup(function(e) {

    let data = $('#register').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-pw",
        data: data,
        success: function (response) {
            $('#pw-warn').html(response);
        }
    });

});

$('#reg-pw-confirm').keyup(function(e) {

    let data = $('#register').serialize();
    $.ajax({
        type: "post",
        url: "/login/check-pw",
        data: data,
        success: function (response) {
            $('#pw_warn').html(response);
        }
    });

});

$('#login-btn').click(function(e) {
    
    e.preventDefault()
    let data = $('#login').serialize()
    $.ajax({
        type: 'post',
        url: '/login/register',
        data: data,
        success: function(response) {
            if (response == "Invalid") {
                $('#login-warn').text("This username and password combination does not exist.");
            }
            else {
                $('#loginModal').modal('hide');
                $('#my-acct-link').show();
                $('#logout-link').show();
                $('#login-link').hide();
                $('#logged_in').attr('value', 'true');
                window.location.href = "/users/dash";
            }
        }
    })

})

$('#register-btn').click(function(e) {
    
    e.preventDefault()
    let data = $('#register').serialize()
    $.ajax({
        type: 'post',
        url: '/login/register',
        data: data,
        success: function(response) {
            if (response == "Invalid") {
                $('#login-warn').text("This username and password combination does not exist.");
            }
            else {
                $('#loginModal').modal('hide');
                $('#my-acct-link').show();
                $('#logout-link').show();
                $('#login-link').hide();
                $('#logged_in').attr('value', 'true');
            }
        }
    })

})

$('#logout-link a').click(function(e) {
    e.preventDefault();
    $.ajax({
        type: 'get',
        url: '/login/logout'
    })
    $('#logged_in').attr('value', 'false');
    $('#my-acct-link').hide();
    $('#logout-link').hide();
    $('#login-link').show();
})