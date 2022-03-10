$('#predict-form').submit(event => {
    event.preventDefault();
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
            if (data.flash === true) {
                window.location.href = '/dashboard/';
            }
            else {
                alert('Something went wrong');
            }
        },
        error: (err) => {
            console.log(err);
        }
    });
})
