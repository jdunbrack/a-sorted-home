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

$('.task-list').on('sortreceive', function (e, ui) {
    let data = "csrfmiddlewaretoken=" + document.getElementsByName('csrfmiddlewaretoken')[0].value + "&task-id=" + ui.item.attr('data-task-id') + "&receiver=" + $(this).parent('.task-tile').attr('data-user-id');
    $.post({
        url: "/tasks/assign",
        data: data
    });
});

$('a[href="/tasks/finish"]').click(function(e) {
    e.preventDefault();
    let data = "csrfmiddlewaretoken=" + document.getElementsByName('csrfmiddlewaretoken')[0].value + "&task-id=" + $(this).parent('.task-row').attr('data-task-id');
    $.post({
        url: "/tasks/finish",
        data: data
    });
    $(this).parent('.task-row').remove();
});

$(document).ready(function () {
    $(".info-popup").tooltip({
        track: true,
        open: function (event, ui) {
            console.log("open listener activated");
            let data = "csrfmiddlewaretoken=" + document.getElementsByName('csrfmiddlewaretoken')[0].value + "&task-id=" + $(this).parents('.task-row').attr('data-task-id');
            $.ajax({
                url: '/tasks/info',
                type: 'post',
                data: data,
                success: function (response) {
                    console.log("ajax returned success")
                    $(this).tooltip('option', 'content', response);
                }
            });
        }
    });

    $(".info-popup").mouseout(function () {
        // re-initializing tooltip
        $(this).attr('title', 'Please wait...');
        $(this).tooltip();
        $('.ui-tooltip').hide();
    });
});