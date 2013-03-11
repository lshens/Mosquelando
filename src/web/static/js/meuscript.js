/**
 * Created with PyCharm.
 * User: renzo
 * Date: 3/5/13
 * Time: 8:56 PM
 * To change this template use File | Settings | File Templates.
 */

var init=function init(){
    var $botoes=$(".btn-danger");
    $botoes.click(function(){
        $("#fluido").slideUp()
    })
        $(".btn-primary").click(function(){
            $("#fluido").slideDown()
        })

    $("#enviar").click(function(){
        var texto=$("#in").val()
        $("#in").val("")
    })
}
$(document).ready(init)