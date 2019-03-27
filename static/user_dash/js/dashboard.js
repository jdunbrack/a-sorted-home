$('#create-form').hide()
$('#join-form').hide()
$('#delete-button').hide()
$('#leave-button').hide()

$('#show-create').click(function(e) {
    e.preventDefault();
    $('#create-form').slideDown();
})

$('#show-join').click(function (e) {
    e.preventDefault();
    $('#join-form').slideDown();
})

$('#delete-link').click(function(e) {
    e.preventDefault();
    $('#delete-button').slideDown();
})

$('#leave-link').click(function(e) {
    e.preventDefault();
    $('#leave-button').slideDown();
})

$('.form-close').click(function(e) {
    e.preventDefault();
    $(this).parent().slideUp();
})
