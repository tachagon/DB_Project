$(document).ready(function(){
    $('nav').affix({
      offset: {
        top: $('nav#derp').offset().top
      }
    });
});