var SELECT_CASE = "[Select Case]";
var SELECT_CASE_SET = "[Select Case Set]";
function reset_ul_case_set(){
    //$('#ul_elements li').remove();
    $('#ul_case_set').children().remove();
    $('#button_select_case_set').text(SELECT_CASE_SET);
}

$("#button_add_new_case_set").click(function(){
//    if($("#input_new_page").val().trim() != ""){
//        $('#button_select_page').text($("#input_new_page").val().trim());
//    }
});
$("#button_add_new_case").click(function(){

});
$("#button_select_case_set").click(function(){
    var tmp_case_sets = [];
    $.ajax({
        url: "/getCaseSet",
        type: "POST",
        data: "",
        error: function (msg) {

        },
        success: function (msg) {
            var tmp_button_select_case_set = $("#button_select_case_set").html().replace(DROPDOWN_SIGN, "").trim();
            if(msg != "" && tmp_button_select_case_set == SELECT_CASE_SET){
                tmp_case_sets = msg.split(".py");
                $("#ul_case_set").children().remove();
                for(var i=0; i<tmp_case_sets.length; i++)
                {
                    if(tmp_case_sets[i] != ""){
                        newRow = _addLi_assemble_dropdown_li_html("li_case_set_on_click", tmp_case_sets[i] + ".py");
                        $("#ul_case_set").append(newRow);
                    }
                }
            }
        }
//        beforeSend
//        timeout: 1000,
//        cache: false,
    });
});
$("#button_select_case").click(function(){
    var tmp_case_sets = [];

});
function li_case_set_on_click(_name){
    $('#button_select_case_set').text(_name);
    $.ajax({
        url: "/getCasesByCaseSet",
        type: "POST",
        data: $('#button_select_case_set').text(),
        error: function (msg) {

        },
        success: function (msg) {
            var tmp_button_select_case = $("#button_select_case").html().replace(DROPDOWN_SIGN, "").trim();
            if(msg != ""){
                alert(msg);
//                $("#ul_case_set").children().remove();
//                for(var i=0; i<tmp_case_sets.length; i++)
//                {
//                    if(tmp_case_sets[i] != ""){
//                        newRow = _addLi_assemble_dropdown_li_html("li_case_set_on_click", tmp_case_sets[i] + ".py");
//                        $("#ul_case_set").append(newRow);
//                    }
//                }
            }
        }
    });

}
function li_case_on_click(_name){
    $('#button_select_case').text(_name);
    $.ajax({
        url: "/getCasesByCaseSet",
        type: "POST",
        data: $('#button_select_case_set').text(),
        error: function (msg) {

        },
        success: function (msg) {
            var tmp_button_select_case = $("#button_select_case").html().replace(DROPDOWN_SIGN, "").trim();
            if(msg != "" && tmp_button_select_case != SELECT_CASE){

//                $("#ul_case_set").children().remove();
//                for(var i=0; i<tmp_case_sets.length; i++)
//                {
//                    if(tmp_case_sets[i] != ""){
//                        newRow = _addLi_assemble_dropdown_li_html("li_case_set_on_click", tmp_case_sets[i] + ".py");
//                        $("#ul_case_set").append(newRow);
//                    }
//                }
            }
        }
    });
}
