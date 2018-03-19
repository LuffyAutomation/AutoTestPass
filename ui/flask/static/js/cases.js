var SELECT_CASE = "[Select Case]";
var SELECT_CASE_SET = "[Select Case Set]";

$("#button_add_new_case_set").click(function(){
//    if($("#input_new_page").val().trim() != ""){
//        $('#button_select_page').text($("#input_new_page").val().trim());
//    }
});
$("#button_add_new_case").click(function(){

});
$("#button_select_case_set").click(function(){
    alert(12121);
    $.ajax({
        url: "/getCaseSet",
        type: "POST",
        data: "",
        error: function (msg) {

        }
        success: function (msg) {
            alert(msg);
        }
    });
});
$("#button_select_case").click(function(){

});