$(document).ready(function(){
    temp_id = $('#config_zone').attr('name')
    url = '/update/' + temp_id
    $('#load_zone').load(url)

    $('#add').click(function(){
        var new_div = '<div class="draggable" style = "position:absolute; top:100px;left:600px"> </div>'
        $("#config_zone").append(new_div);
        alert('add success')
    })

    $('#reset').click(function(){
        $("#config_zone").html('<div class="draggable" id="aaa"> </div>');
        alert('reset success')
    })

    $('#save').click(function(){
        var context = $("<p>").append($("#config_zone").clone()).html();
        id = $(this).attr("name");
        $.ajax({
            type: "POST",
            data:{
            id: id,
            html:context
            },
            url: "save_config_dashboard/" + id,
            dataType: 'text',
            success: function(result) {
                alert(result)
            }
        });
    })
})
