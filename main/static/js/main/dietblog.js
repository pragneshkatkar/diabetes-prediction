$('#add-diet-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/diet/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            heading: $('#heading').val(),
            description: $('#description').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/diets/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})

$('#edit-diet-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'PUT',
        url: '/api/diet/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            diet_id: $('#diet_id').val(),
            heading: $('#heading').val(),
            description: $('#description').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/diets/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})

function deleteDiet(post_id){
    $.ajax({
        type: 'DELETE',
        url: '/api/diet/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            diet_id: post_id,
        },
        success: (data) => {
            window.location.href = '/diets/';
        },
        error: (err) => {
            console.log(err);
        }
    });
}