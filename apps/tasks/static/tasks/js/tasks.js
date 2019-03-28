// remember on ui-droppable-hover to increase height and/or width slightly.
// jquery .addClass will animate.

$('.task-row').draggable({
    cursor: 'move',
    opacity: .7,
    revert: 'invalid',
    scroll: true,
    scrollSensitivity: 50,
})

$('.task-tile').droppable({
    tolerance: "pointer"
});

$('.task-tile').on("drop", function(event, ui) {
    // ui = object, contains ['draggable'], the element being dropped

})