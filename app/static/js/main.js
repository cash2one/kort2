$(document).ready(function() {
    $('.main').fadeIn(1000);
});

var recaptchaCallback = function(){
  $("form").submit();
}