$('#closeNav').click(function(e) {
    e.preventDefault();
    $('#sidenav').css("width", "0");
})

$('#openNav').click(function(e) {
    e.preventDefault();
    $('#sidenav').css("width", "200px");
})