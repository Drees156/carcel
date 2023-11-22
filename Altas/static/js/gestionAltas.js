(function(){

    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Seguro deseas eliminar esta PPL?');
            if(!confirmacion){
              e.preventDefault();
            }
        });
    });
})();

document.addEventListener('DOMContentLoaded', function () {
    var alertMessages = document.querySelectorAll('.alert');

    alertMessages.forEach(function (message) {
        setTimeout(function () {
            message.classList.add('fade');
        }, 5000);
    });

    alertMessages.forEach(function (message) {
        message.addEventListener('transitionend', function () {
            message.remove();
        });
    });
});



