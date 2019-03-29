// remember on ui-droppable-hover to increase height and/or width slightly.
// jquery .addClass will animate.

$('#add-task').click(function(e) {
    e.preventDefault();
    let data = $('#new-task').serialize();
    $.ajax({
        type: "post",
        url: "/tasks/create",
        data: data,
        success: function (response) {
            $('.main-tile .task-list').append(response)
            $('#close-modal').trigger('click');
        }
    });
});

$('.task-list').sortable({
    cursor: 'move',
    items: '> li',
    opacity: 0.5,
    revert: true,
    tolerance: 'intersect',
    zIndex: 1002,
    connectWith: '.task-list',
    placeholder: "task-placeholder",
    forcePlaceholderSize: true,
    activate: function () {
        $('.task-list').addClass('border');
    },
    deactivate: function () {
        $('.task-list').removeClass('border');
    }
});

