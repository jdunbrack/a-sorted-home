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

$('#pw-1').keyup(function(e) {

    let data = $('#info-update').serialize();
    $.ajax({
        type: "post",
        url: "/users/check-pw",
        data: data,
        success: function (response) {
            $('#pw1-warn').html(response);
        }
    });

});

$('#pw-2').keyup(function(e) {

    let data = $('#pw-update').serialize();
    $.ajax({
        type: "post",
        url: "/users/check-pw",
        data: data,
        success: function (response) {
            $('#pw2-warn').html(response);
        }
    });

});

$('#new-pw').keyup(function(e) {

    let data = $('#pw-update').serialize();
    $.ajax({
        type: "post",
        url: "/users/validate-pw",
        data: data,
        success: function (response) {
            $('#new-pw-warn').html(response);
        }
    });

});

$('#new-pw-confirm').keyup(function(e) {

    let data = $('#pw-update').serialize();
    $.ajax({
        type: "post",
        url: "/users/validate-pw",
        data: data,
        success: function (response) {
            $('#new-pw-warn').html(response);
        }
    });

});