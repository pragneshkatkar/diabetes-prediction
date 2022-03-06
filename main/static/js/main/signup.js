$('#signup-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/signup/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            username: $('#email').val(),
            first_name: $('#first-name').val(),
            last_name: $('#last-name').val(),
            email: $('#email').val(),
            password: $('#password').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/login/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})