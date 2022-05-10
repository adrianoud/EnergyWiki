$(document).ready(function(){
//    var x = document.querySelector('#edit1')
    $('.edit').click(function(){
        alert($(this).attr("id"))
    })
    $('.detail').click(function(){
        window.location.href = link
    })

    var showBtn = document.querySelector('#add_dashboard')
    var closeBtn = document.querySelector('.close')
    var dialog = document.querySelector('dialog')

    showBtn.addEventListener('click', () => {
    dialog.showModal()
    })

    closeBtn.addEventListener('click', () => {
    dialog.close($("#name").val())
    })

    returnValueBtn.addEventListener('click', () => {
    console.log(dialog.returnValue)
})
})






function hello(){
alert("hello000")
}