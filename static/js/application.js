// ฟังก์ชันหาความกว้างและความสูงของหน้าเว็บ
function gWH(){
    var e = window, a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    }
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] }
}

$(document).scroll(function(e){
    var scrollTop = $(document).scrollTop();
    var hei = $(document).height();
    var headerHei = $('header').height();
    console.log(gWH().width);
    if(gWH().width > 1500){
        if(scrollTop > (headerHei)){
            $('#navbar-menu').removeClass('navbar-static-top').addClass('navbar-fixed-top');
        } else {
            $('#navbar-menu').removeClass('navbar-fixed-top').addClass('navbar-static-top');
        }
    }
});

function defaultSelect(btn_id, sel_id){
    var btn_id = '#' + btn_id;
    var sel_id = '#' + sel_id + ' option';
    $(btn_id).on("click", function () {
        $(sel_id).prop('selected', function() {
            return this.defaultSelected;
        });
    });
}
