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

$('#my-profile-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'PUT',
        url: '/api/my-profile/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            username: $('#email').val(),
            first_name: $('#first-name').val(),
            last_name: $('#last-name').val(),
            email: $('#email').val(),
            address: $('#address').val(),
            city: $('#city').val(),
            state: $('#state').val(),
            country: $('#country').val(),
            zipcode: $('#zipcode').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/my-profile/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})