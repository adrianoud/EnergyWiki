        $(
            function () {
                var chart = echarts.init(document.getElementById('line'), 'white', {renderer: 'canvas'});

                $("select").change(function(){
                    var selected = new Array();
                    $("select option:selected").each(function(){
                    selected.push($(this).val())
                    });
                    $.ajax({
                        type: "POST",
                        data:{
                        region: selected,
                        start_year: $("#start_year").val(),
                        end_year: $("#end_year").val()
                        },
                        url: "http://127.0.0.1:5000/Chart",
                        dataType: 'json',
                        success: function (result) {
                            chart.setOption(result);
                        }
                    });
                });
            }
        )