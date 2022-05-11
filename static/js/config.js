$(document).ready(function(){
    temp_id = $('#config_zone').attr('name')
    url = '/update/' + temp_id
    $('#load_zone').load(url)

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
