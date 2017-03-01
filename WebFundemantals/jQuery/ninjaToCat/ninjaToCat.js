$(document).ready(function() {


    $('img').click(function() {
        var catpic = $(this).attr('data-alt-src');
        $(this).attr('src', catpic);
    });
});
