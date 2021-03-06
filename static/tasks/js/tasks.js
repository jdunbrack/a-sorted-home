// remember on ui-droppable-hover to increase height and/or width slightly.
// jquery .addClass will animate.
/*
$('#add-task').click(function(e) {
    e.preventDefault();
    let data = $('#new-task').serialize();
    $.ajax({
        type: "post",
        url: "/tasks/create",
        data: data,
        success: function (response) {
            $('.main-tile').append(response)
            $('.task-row').draggable({
                cursor: 'move',
                opacity: .7,
                revert: 'invalid',
                scroll: true,
                scrollSensitivity: 50,
            });
        }
    });
});
*/
$('.task-row').draggable({
    cursor: 'move',
    opacity: .7,
    revert: 'invalid',
    scroll: true,
    scrollSensitivity: 50,
});

$('.task-tile').droppable({
    tolerance: "pointer"
});

$('.task-tile').on("drop", function(event, ui) {
    // ui = object, contains ['draggable'], the element being dropped
    // add ajax to change owner of task based on tile dropped

});
