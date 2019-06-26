$(document).ready(function () {
    $(".botao").click(function () {
        $(this).addClass('disabled');
        $(this).css('cursor', 'not-allowed');
        $(this).css('background-color', 'lightgray');
        $(this).css('color', 'black');
    });
})

$('#popover').popover({
  trigger: 'click'
})


