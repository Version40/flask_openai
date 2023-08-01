$(document).ready(function() {
    $('#submit-button').on('click', function() {
        const data = {
            field1: $('#field1').val(),
            field2: $('#field2').val(),
        };

        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/process_data',
            data: JSON.stringify(data),
            success: function(response) {
                $('#result').text(response.result);
            },
            error: function(error) {
                console.error('Помилка під час запиту:', error);
            }
        });
    });
});

$(document).ready(function() {
  $("#submit-button").click(function() {
    var field1 = $("#field1").val();
    var field2 = $("#field2").val();

    $("#loading-animation").show();

    $.ajax({
      url: "/process_data",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({ "field1": field1, "field2": field2 }),
      success: function(response) {
        $("#loading-animation").hide();

        $("#result").text(response.result);
      },
      error: function(error) {
        $("#loading-animation").hide();

        console.error('Помилка під час запиту:', error);
      }
    });
  });
});
