$('#feedback-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/feedback/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            feedback: $('#feedback').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/dashboard/feedback/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})