$(document).ready(function(){
    $("#year").change(update_map);            //  JS里面直接调用函数需要加括号，Jqury事件调用只需函数名 hello()
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
})

function hello(){
alert("hello")
}


function update_map(){
    var map = echarts.init(document.getElementById('map'), 'white', {renderer: 'canvas'});
    $.ajax({
        type: "POST",
        data: {
        year: $("#year").val()
        },
        url: "http://127.0.0.1:5000/Map",
        dataType: 'json',
        success: function (result) {
            map.setOption(result);
        }
    });
    var bar = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
    $.ajax({
        type: "POST",
        data: {
        year: $("#year").val()
        },
        url: "http://127.0.0.1:5000/Bar",
        dataType: 'json',
        success: function (result) {
            bar.setOption(result);
        }
    });
    map.on('click',function(params){
        var chart = echarts.init(document.getElementById('line'), 'white', {renderer: 'canvas'});
        $.ajax({
            type: "POST",
            data:{
            region: JSON.stringify(Array(params.name))
            },
            url: "http://127.0.0.1:5000/Chart",
            dataType: 'json',
            success: function (result) {
                chart.setOption(result);
            }
        });
    });
}