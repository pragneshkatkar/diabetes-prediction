$('#predict-form').submit(event => {
    event.preventDefault();
    alert('ds')
    $.ajax({
        type: 'POST',
        url: '/api/predict/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            name: $('#name').val(),
            no_of_pregnancies: $('#no_of_pregnancies').val(),
			glucose: $('#glucose').val(),
			blood_pressure: $('#blood_pressure').val(),
			skin_thickness: $('#skin_thickness').val(),
			insulin: $('#insulin').val(),
			bmi: $('#bmi').val(),
			age: $('#age').val()
        },
        success: (data) => {
            // if (data.status === 'Successful') {
            //     window.location.href = '/requirements/';
            // }
            // else {
            //     alert('Username or Password is incorrect');
            // }
        },
        error: (err) => {
            console.log(err);
        }
    });
})