$('select').change(function() {
    user_id = $(this).val()
    url = "/balances/query/" + user_id
    $.ajax({
        type: "GET",
        url: url,
        success: function (response) {
            $('#balance-table').html(response);
        }
    });
})
