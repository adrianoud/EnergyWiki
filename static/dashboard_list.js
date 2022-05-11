$(document).ready(function(){
    $('.edit').click(function(){
        alert($(this).attr("name"))
    })

    $('.detail').click(function(){
        id = $(this).attr("name");
        detail(id);
    })
})


function detail(id){
    document.dashboard_list.action = 'config/' + id;
    document.dashboard_list.submit();
}
