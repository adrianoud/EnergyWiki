$(document).ready(function(){
    var showBtn = document.querySelector('#add_dashboard')
    var closeBtn = document.querySelector('.close')
    var dialog = document.querySelector('dialog')

    showBtn.addEventListener('click', () => {
    dialog.showModal()
    })

    closeBtn.addEventListener('click', () => {
    dialog.close($("#name").val())
    })
})
