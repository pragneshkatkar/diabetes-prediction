$('#add-doctor-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/add-doctor/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            name: $('#name').val(),
            degree: $('#degree').val(),
            contact_number: $('#contact_number').val(),
            email: $('#email').val(),
            is_active: $('#is_active').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/admin/doctors-contact/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})