$(document).ready(function () {

    function csrfCatch() {

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

    }

    csrfCatch();

    function openDailog() {
        $('.modal').modal('show');
    }

    $(document).on('click', '.postEditLink', function () {
        event.preventDefault();
        openDailog();
        $.get(this.href, function (data) {
            $('#dialogBody').html(data)
        });
        return false;
    });

    $(document).on('click', '.newPostCreate', function () {
        event.preventDefault();
        openDailog();
        $.get(this.href, function (data) {
            $('#dialogBody').html(data)
        });
        return false;
    });

    $(document).on('click', '.updateLikes', function (event) {
        event.preventDefault();
        updateLikes();
    });

    function updateLikes() {

        var ids = [];


        $('.likecount').each(function () {
            ids.push($(this).data('post-id'))
        });

        $.getJSON('./../likes', {ids:ids.join(',')}, function (data) {
            for(var i in data) {
                $('.likecount[data-post-id='+i+']').html(data[i]);
            }
        })
    }
    updateLikes();
    window.setInterval(updateLikes, 60000);

    $('.likecount').click(function () {
        var url = $(this).data('likes-url');
        var element = $(this);
        $.post(url, function (data) {
            element.html(data);
        });
    });

    $('#id_order_by').chosen();

});
