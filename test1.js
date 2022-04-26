        $(
            function () {
                $("#country").change(function(){
                    echarts.init(document.getElementById('line')).dispose();          // 清除缓存
                    var chart = echarts.init(document.getElementById('line'), 'white', {renderer: 'canvas'});
                    var selected = new Array();
                    selected = [];
                    $("#country option:selected").each(function(){
                        selected.push($(this).val())
                    });
                    $.ajax({
                        type: "POST",
                        data:{
                        region: JSON.stringify(selected)
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