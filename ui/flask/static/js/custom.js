var TITLE_DIALOG_TIP = "!";

var whichRowObjClicked = null;
var whichRowClicked_StepsTable = 0;
var whichElementClicked_StepsTable = "";
var whichElementClicked_Json = null;
var whichPageByElementClicked_StepsTable = "";
var whichSubpageByElementClicked_StepsTable = "";
var list_locators = [];
var SELECT_PAGE = "[Select Page]";
var SELECT_SUBPAGE = "[Select Sub Page]";
var SELECT_ELEMENT = "[Select Element]";
var DROPDOWN_SIGN = "<span class=\"caret\"></span>";
var jsonUiMapPagesForOperation = null;
var ifReassembleUls = false;
var digitObjFromCaseClicked = null;
//$("button_add_page").on("click",function(){

//    //Can not find out the ele that created dynamically. Need other method.
//});
//$("button_add_subpage").on("click",function(){

//    //Can not find out the ele that created dynamically. Need other method.
//});
//$("button_add_element").on("click",function(){

//    //Can not find out the ele that created dynamically. Need other method.
//});
function getStringForAddPageAndSubPage(page_name, string_subpage, description){
    var description = arguments[2] ? arguments[2] : "";
    return "{\"@name\":\"" + page_name + "\",\"@description\":\"" + description + "\", \"page\":[" + string_subpage + "]}";
}
function getJsonForAddPage(page_name, element_json_string, description){
    return JSON.parse(getStringForAddPage(page_name, element_json_string, description));
}
function getStringForAddPage(page_name, element_json_string, description){
    var description = arguments[2] ? arguments[2] : "";
    return "{\"@name\":\"" + page_name + "\",\"@description\":\"" + description + "\", \"element\":[" + element_json_string + "]}";
}
function getStringForAddElement(element_name, locator_type, element_locator){
    return "{\"@name\":\"" + element_name + "\", \""+ locator_type +"\":[" + element_locator + "]}";
}
function getJsonForAddElement(element_name, locator_type, element_locator){
    return JSON.parse(getStringForAddElement(element_name, locator_type, element_locator));
}
function stringToJson(str){
    return JSON.parse(str);
}
function jsonToString(json){
    return JSON.stringify(json);
}
function changeObjToArrayAndPush(obj, json){
    var t = obj;
    obj = [];
    obj.push(t);
    obj.push(json);
    return obj;
}
function _addRemoveElementToJson_handleNonArrayElement(obj, element_json){
    if(typeof(obj['@name']) == "undefined" || obj['@name'] == element_json['@name'] ){
        obj = element_json;
    }
    else
    {
        obj = changeObjToArrayAndPush(obj, element_json);
    }
    return obj;
}
function deepCopyJson(obj){
    try{
        return stringToJson(jsonToString(obj));
    }
    catch(e){alert(e);}
}
function addRemoveElementToJson(addOrRemove, page_name, element_json, subpage_name){
//    var subpage_name = arguments[2] ? arguments[2] : null;
    ifReassembleUls = true;
    if (addOrRemove == "remove" && typeof(element_json['@name']) == "undefined"){ // for removing simply
        //element_json['@name'] = element_json;  wrong
        element_json = getJsonForAddElement(element_json, "forremoving", null);
    }
    if(jsonUiMapPagesForOperation == null){
        jsonUiMapPagesForOperation = deepCopyJson(jsonUiMapPages);
    }
//    alert(JSON.stringify(jsonUiMapPages));
//    alert(JSON.stringify(jsonUiMapPagesForOperation));
    var isNewPage = false;
    for(var i=0; i<jsonUiMapPagesForOperation.length; i++){
        if(jsonUiMapPagesForOperation[i]["@name"] == page_name){
            try{
//            jsonUiMapPagesForOperation[i].element = "23232323";
                if(subpage_name != null && subpage_name != SELECT_SUBPAGE){
                    for(var j=0; j<jsonUiMapPagesForOperation[i]['page'].length; j++){
                        if(jsonUiMapPagesForOperation[i]['page'][j]['@name'] == subpage_name){
                            for(var k=0; k<jsonUiMapPagesForOperation[i]['page'][j]['element'].length; k++){
                                if(jsonUiMapPagesForOperation[i]['page'][j]['element'][k]['@name'] == element_json['@name']){
                                    if(addOrRemove == "add"){
                                        jsonUiMapPagesForOperation[i]['page'][j]['element'][k] = element_json;
                                    }
                                    else{
                                        jsonUiMapPagesForOperation[i]['page'][j]['element'].splice(k, 1);
                                    }
                                    return;
                                }
                            }
                            if(addOrRemove == "add"){
                                jsonUiMapPagesForOperation[i]['page'][j]['element']  = _addRemoveElementToJson_handleNonArrayElement(jsonUiMapPagesForOperation[i]['page'][j]['element'] , element_json);
                            }
                            else{
                                if (element_json['@name'] != SELECT_ELEMENT){
                                    delete jsonUiMapPagesForOperation[i]['page'][j]['element'];
                                }
                                else{
                                    jsonUiMapPagesForOperation[i]['page'].splice(j,1);
                                    //delete jsonUiMapPagesForOperation[i];   deleted but a null left...
                                }
                            }
                            return;
                        }
                     }
                }
                else{
                    if (typeof(jsonUiMapPagesForOperation[i]['element']) != "undefined"){ // for removing simply
                        for(var k=0; k<jsonUiMapPagesForOperation[i]['element'].length; k++){
                            if(jsonUiMapPagesForOperation[i]['element'][k]['@name'] == element_json['@name']){
                                if(addOrRemove == "add"){
                                    jsonUiMapPagesForOperation[i]['element'][k] = element_json;
                                }
                                else{
                                    jsonUiMapPagesForOperation[i]['element'].splice(k, 1);
                                    //delete delete jsonUiMapPagesForOperation[i]['element'][k];   deleted but a null left...
                                }
                                return;
                            }
                        }
                    }
                    if(addOrRemove == "add"){
                        jsonUiMapPagesForOperation[i]['element'] = _addRemoveElementToJson_handleNonArrayElement(jsonUiMapPagesForOperation[i]['element'], element_json);
                    }
                    else{
                        if (element_json['@name'] != SELECT_ELEMENT){
                                delete jsonUiMapPagesForOperation[i]['element'];
                        }
                        else{
                            jsonUiMapPagesForOperation.splice(i,1);
                            //delete jsonUiMapPagesForOperation[i];   deleted but a null left...
                        }
                    }
                    return;
                    //delete jsonUiMapPagesForOperation[i];
                }
            }
            catch(e){alert(e);}
            //alert(JSON.stringify(jsonUiMap));
            return;
        }
    }
    if($('#button_select_subpage').text() == SELECT_SUBPAGE){
        element_json = getJsonForAddPage(page_name, JSON.stringify(element_json), "");
    } else{
    element_json = stringToJson(getStringForAddPageAndSubPage(page_name, getStringForAddPage(subpage_name, JSON.stringify(element_json), ""), ""));
    }
    jsonUiMapPages.push(element_json);
}
function close_add_locator_modal(){
    $('#button_close_add_locator').click();
}
$("#button_close_add_locator, #button_x_add_locator").click(function(){
//    alert("1         " + jsonToString(jsonUiMapPagesForOperation));
//    alert("1         " + jsonToString(jsonUiMapPages));
    jsonUiMapPagesForOperation = deepCopyJson(jsonUiMapPages);
//    alert("2         " + jsonToString(jsonUiMapPagesForOperation));
//    alert("2         " + jsonToString(jsonUiMapPages));
});

$("#button_save_add_locator").click(function(){
//    alert($("#table_locators input").eq(0).val());
    var locators = "";
    var locator_type = "";
    var locator_value = "";

    var selected_element_name = $('#button_select_element').text().trim();
    var selected_page_name = $('#button_select_page').text().trim();
    var selected_subpage_name = $('#button_select_subpage').text().trim();
    var locators_name_dict = {};
    var locators_array = {};

    $("#table_locators tr").each(function() {
        locator_type = $(this).children().eq(0).text().trim();
        locator_value = $(this).children().eq(1).children().val().trim();
        if(locator_value == ""){
            locators_array = {};
            return false;
        }
        locators_array[locator_type] = locators_array[locator_type]||[];
        locators_array[locator_type].push("\"" + locator_value + "\"");
    });
    for(var key in locators_array){
        if(locators != ""){
            locators += ",";
        }
        locators += "\"" + key + "\":[" + locators_array[key] + "]";
    }
    var dialog_tip = "";
//    if(locators != ""){
//        locators = "{\"" + "@name\":\"" + selected_element_name + "\"," +  locators + "}";
//    }
//    else{
//        dialog_tip = "Please add locator(s) or the locator can not be empty.";
//    }
//    if(selected_element_name == SELECT_ELEMENT){
//        dialog_tip = "Please select or create an element.";
//    }
//    else if(selected_page_name == SELECT_PAGE){
//        dialog_tip = "Please select or create an page.";
//    }
    if(ifReassembleUls == true)
    {
        dialog_tip = "Save the change(s)?";
    }
    if(dialog_tip != ""){
        $.confirm({
            buttons: {
                confirm: {
                    btnClass: 'btn-blue',
                    action: function(){
                        ifReassembleUls = false;
                        if(selected_page_name != SELECT_PAGE && locators != ""){
                    //        var newJson='{"name":"liubei","sex":"男"}';
                    //        var sss='{"@name":"liubei","element":"222"}';
                            if(selected_subpage_name != SELECT_SUBPAGE){
                                addRemoveElementToJson("add", selected_page_name, stringToJson(locators), selected_subpage_name);
                            }
                            else{
                                addRemoveElementToJson("add", selected_page_name, stringToJson(locators), null);
                            }
                        }
                        //the ele in table_cases needs to be modified if the ele was updated in table_locators
                        if(selected_page_name != whichPageByElementClicked_StepsTable || whichElementClicked_StepsTable != selected_element_name || selected_subpage_name != whichSubpageByElementClicked_StepsTable){
                            whichRowObjClicked.attr("page", selected_page_name);
                            if(selected_subpage_name == SELECT_SUBPAGE){
                                selected_subpage_name = "";
                            }
                            whichRowObjClicked.attr("subpage", selected_subpage_name);
                            whichRowObjClicked.html(selected_element_name);
                        }
                        jsonUiMapPages = deepCopyJson(jsonUiMapPagesForOperation);
                        return;
                    }
                },
                cancel: function () {
                    jsonUiMapPagesForOperation = deepCopyJson(jsonUiMapPages);
                    return;
                }
            },
            title: TITLE_DIALOG_TIP,
            content: dialog_tip,
            draggable: true
        });
    }


    $.ajax({
        url: "/sendJsonUiMap",
        type: "POST",
        data: jsonToString(jsonUiMap),
        success: function (msg) {
            //alert(msg.time)
        }
    });
});
$("#button_add_new_page").on("click",function(){
    if($("#input_new_page").val().trim() != ""){
        $('#button_select_page').text($("#input_new_page").val().trim());
    }
});
$("#button_add_new_subpage").on("click",function(){
    if($("#input_new_subpage").val().trim() != ""){
        $('#button_select_subpage').text($("#input_new_subpage").val().trim());
    }
});
$("#button_add_new_element").on("click",function(){
    if($("#input_new_element").val().trim() != ""){
        $('#button_select_element').text($("#input_new_element").val().trim());
    }
});
function reset_ul_pages(){
//    $('#ul_pages li').remove();  because function _addLi_assemble_dropdown_li_html(name_func, value){
    $('#ul_pages').children().remove()
    $('#button_select_page').text(SELECT_PAGE);
}
function reset_ul_subpages(){
//    $('#ul_subpages li').remove();
    $('#ul_subpages').children().remove()
    $('#button_select_subpage').text(SELECT_SUBPAGE);
}
function reset_ul_elements(){
    //$('#ul_elements li').remove();
    $('#ul_elements').children().remove();
    $('#button_select_element').text(SELECT_ELEMENT);
}
function _addLi_assemble_dropdown_li_html(name_func, value){
    return "<li style=\"float:left;width:80%;\" ><a href='#' onclick=\"" + name_func + "('"  + value +  "');\">" + value + "</a></li><a style=\"float:right;margin-top:4px;\" id=\""+ value +"\" href=\"#\" class=\"glyphicon glyphicon-remove\"/>";
    //return "<li style=\"float:left;width:80%;\" ><a href='#' onclick=\"" + name_func + "('"  + value +  "');\">" + value + "</a></li><a style=\"float:right;margin-top:4px;\" id=\""+ value +"\" href=\"#\" class=\"glyphicon glyphicon-remove\"/><input style=\"float:right;\" id=\"checkBox\" type=\"checkbox\">";
}
function addLi(list_objs, name_attri, name_func, ul_obj){
    if (typeof(list_objs) == "undefined"){
        return;
    }
    if(list_objs.length >= 1){
        for(var i=0; i<list_objs.length; i++)
        {
            if (typeof(list_objs[i]) == "object")
            {
                value = list_objs[i][name_attri];
                newRow = _addLi_assemble_dropdown_li_html(name_func, value);
                $(ul_obj).append(newRow);
            }
        }
    }
    else{
        //list_objs.length cannot equal to 1 in this case.
        value = list_objs[name_attri];
        newRow = _addLi_assemble_dropdown_li_html(name_func, value);
        $(ul_obj).append(newRow);
    }
}
function li_subpage_on_click(subpage_name){
    reset_ul_elements();
    $('#button_select_subpage').text(subpage_name);
    for(var i=0; i<jsonUiMapPages.length; i++){
        if(jsonUiMapPages[i]["@name"] == $('#button_select_page').text() ){
            for(var j=0; j<jsonUiMapPages[i]['page'].length; j++){
                if(jsonUiMapPages[i]['page'][j]['@name'] == subpage_name){
                    addLi(jsonUiMapPages[i]['page'][j]['element'], '@name', 'li_element_on_click', '#ul_elements');
                    whichElementClicked_Json = jsonUiMapPages[i]['page'][j]['element'];
                    return;
                }
            }
        }
    }
}
function li_element_on_click(_name){
    $('#button_select_element').text(_name);
    assembleLocatorsTableForClickedElement(whichElementClicked_Json);
}
function li_page_on_click(_name){
//    reset_ul_pages()
    reset_ul_subpages();
    reset_ul_elements();
    $('#button_select_page').text(_name);
    for(var i=0; i<jsonUiMapPages.length; i++){
        if(jsonUiMapPages[i]["@name"] == _name){
            addLi(jsonUiMapPages[i]['page'], '@name', 'li_subpage_on_click', '#ul_subpages');
            addLi(jsonUiMapPages[i]['element'], '@name', 'li_element_on_click', '#ul_elements');
            whichElementClicked_Json = jsonUiMapPages[i]['element'];
            return;
        }
    }
}
function _assembleLocatorsTableForClickedElement(eleObj, eleName){
    if(eleObj['@name'] == eleName){
        for(var key in eleObj){
            if(key != "@name"){
                if(typeof(eleObj[key]) != "string"){ //"string" will evoke   s t r i n g
                    for(var i=0; i<eleObj[key].length; i++){
                        appendLocatorRow(key, eleObj[key][i]);
                    }
                }
                else{
                    appendLocatorRow(key, eleObj[key]);
                }
            }
        }
    }
}
function assembleLocatorsTableForClickedElement(eleObj){
    $("#table_locators tr").remove();
    var eleName = $("#button_select_element").html();
    eleName = eleName.replace(DROPDOWN_SIGN, "");
    if(eleName != SELECT_ELEMENT){
        if(typeof(eleObj.length) == "undefined"){
            _assembleLocatorsTableForClickedElement(eleObj, eleName);
        }
        else{
            for(var k=0; k<eleObj.length; k++){
                _assembleLocatorsTableForClickedElement(eleObj[k], eleName);
            }
        }
    }
}
$("#ul_new_page li").on("click",function(){

    //Can not find out the ele that created dynamically. Need other method.
});
function assemblePagesDropdown(){
    addLi(jsonUiMapPages, '@name', 'li_page_on_click', '#ul_pages');
}
$("#input_new_page").ready(function(){
    //assemble all Pages in Page Dropdown
    //assemblePagesDropdown();
});
$("#table_cases td a").click(function(){
    if("#addLocatorModal" == $(this).attr("data-target")){
        $("#ul_pages").css("display","");  // closed Add Locators modal and reopen
        $("#ul_subpages").css("display","");
        $("#ul_elements").css("display","");
        $("#ul_pages").empty();

        assemblePagesDropdown();

        whichElementClicked_StepsTable = $(this).html();
        whichPageByElementClicked_StepsTable = $(this).attr("page");
        whichSubpageByElementClicked_StepsTable = $(this).attr("subpage");
        whichRowClicked_StepsTable = $(this).parent().parent().find("td").html();
        whichRowObjClicked = $(this);
        if (typeof(whichPageByElementClicked_StepsTable) == "undefined" || whichPageByElementClicked_StepsTable == ""){
            whichPageByElementClicked_StepsTable = SELECT_PAGE;
        }
        else{
            li_page_on_click(whichPageByElementClicked_StepsTable);
        }
        if (typeof(whichSubpageByElementClicked_StepsTable) == "undefined" || whichSubpageByElementClicked_StepsTable == ""){
            whichSubpageByElementClicked_StepsTable = SELECT_SUBPAGE;
        }
        else{
            li_page_on_click(whichSubpageByElementClicked_StepsTable);
        }
        $("#button_select_page").html(whichPageByElementClicked_StepsTable + DROPDOWN_SIGN);
        $("#button_select_subpage").html(whichSubpageByElementClicked_StepsTable + DROPDOWN_SIGN);
        $("#button_select_element").html(whichElementClicked_StepsTable + DROPDOWN_SIGN);
        assembleLocatorsTableForClickedElement(whichElementClicked_Json);
    }
    else if($(this).attr("trigger") == "digit"){
        //can not use onkeyup as independent function since it is dynamic.
        //onafterpaste=\"this.value=this.value.replace(/[^\\d]/g,'')\"
        //replace(/^[^1-9][^\\d]*$/,'').replace(/[^\\d]/g,'')
        //(/^((\d*[1-9])|(0?\.\d{2}))$/g,'')
        ///^[1-9]\\d*$/
        digitObjFromCaseClicked = $(this);
        var html = getModalHtml("<input id='input_change_digit' type='text' onkeyup=\"this.value=this.value.replace(/^[^1-9]([^\\d]*)$/,'')\" class='form-control' placeholder='only digit allowed.' aria-describedby='' value='" + $(this).html() + "'/>");
        $("body").append(html);
        $("#changeDigitModal").modal("show");

    }
});

function button_save_dynamic_modal_clicked()
{
    //$("#input_change_digit").text()      doesn't work for dynamic
    // document.getElementById("input_change_digit").value works
    // document.querySelector('#input_change_digit').value works   document.querySelector document.querySelectorAll   performance is low.
    var input_value = document.getElementById('input_change_digit').value;
    if(input_value.trim() != ""){
        digitObjFromCaseClicked.text(input_value.trim());
    }
}

$("#button_save_dynamic_modal").click(function(){

});
$("#button_save_add_locator").click(function(){
    if("#addLocatorModal" == $(this).attr("data-target")){
        whichElementClicked_StepsTable = $(this).html();
        $("#button_select_page").html(name_page + "<span class='caret'></span>");
    }
});
//$("#table_cases td").click(function(){
//    $('#table_locators tr').remove();
////      var tdSeq = $(this).parent().find("td").index($(this)[0]);
//    whichRowClicked_StepsTable = $(this).parent().parent().find("tr").index($(this).parent()[0]);
//});
function appendLocatorRow(locatorType, locatorValue){
	var newRow="<tr>" +
                    "<td style='width:120px;'>" + locatorType + "</td>" +
                    "<td><input type='text' class='form-control' value=\"" + locatorValue + "\"/></td>" +
                    "<td style='width:30px;'><a class='glyphicon glyphicon-remove'/></td>" +
                "</tr>";
	$('#table_locators').append(newRow);
}
function removeLocatorRow(rowNeedRemove){
    rowNeedRemove.remove();
}
//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
var clearFlag = 0;
var count = 3;
var showModal = function(){
    $('#myModal').modal('toggle')
    clearFlag = self.setInterval("autoClose()",1000);
}
var autoClose = function(){
    if(count>0){
        $("#num").html(count);
        count--;
    }else if(count<=0){
        window.clearInterval(clearFlag);
        $("#num").html("");
        $("#myModal").fadeOut("slow");
        count = 3;
        $("#myModal").modal('hide');
    }
}
$(function(){
  var $up = $(".up")
  $up.click(function() {
    var $tr = $(this).parents("tr");
    if ($tr.index() != 0) {
      $tr.fadeOut().fadeIn();
      $tr.prev().before($tr);
    }
  });
  var $down = $(".down");
  var len = $down.length;
  $down.click(function() {
    var $tr = $(this).parents("tr");
    if ($tr.index() != len - 1) {
      $tr.fadeOut().fadeIn();
      $tr.next().after($tr);
    }
  });
  var $top = $(".top");
  $top.click(function(){
    var $tr = $(this).parents("tr");
    $tr.fadeOut().fadeIn();
    $(".table").prepend($tr);
    $tr.css("color","#f60");
  });
});
function showShowCss(id)
{
    $("#" + id).css('display','block');
//    $(id).hide();
}
function hideShowCss(id)
{
    $("#" + id).css('display','none');
}
function setFocus(id){
    $("#" + id).focus();
}
$(function() {
    $("[data-toggle='progress']").popover({
        html : true,
        title: title(),
        delay:{show:300, hide:1000},
        content: function() {
          return content();
        }
    });
});
function title() {
    return '';
}
$(function() {
    $("[data-toggle='addLocator']").popover({
        html : true,
        title: title(),
        delay:{show:300, hide:1000},
        content: function() {
          return content2();
        }
    });
});
function content2() {
  var data = $("<div id='loginModal' class='modal show'>" +
  "<div class='modal-dialog'>" +
    "<div class='modal-content'>" +
      "<div class='modal-header'>" +
        "<button  data-dismiss='modal' class='close'>x</button>" +
        "<h1 class='text-center text-primary'>登录</h1>" +
      "</div><div class='modal-body'><form action='' class='form col-md-12 center-block'>" +
          "<div class='form-group'><input type='text' class='form-control input-lg' placeholder='电子邮件'></div>" +
          "<div class='form-group'>" +
            "<input type='password' class='form-control input-lg' placeholder='登录密码'>" +
          "</div>" +
          "<div class='form-group'>" +
            "<button class='btn btn-primary btn-lg btn-block'>立刻登录</button>" +
            "<span><a href='#'>找回密码</a></span>" +
            "<span><a href='#' class='pull-right'>注册</a></span>" +
          "</div>" +
        "</form>" +
      "</div>" +
      "<div class='modal-footer'>" +
      "</div>" +
    "</div>" +
  "</div>" +
"</div>");
  return data;
}
function content1() {
  var data = $("<div id='loginModal' class='modal show'>" +
  "<div class='modal-dialog'>" +
    "<div class='modal-content'>" +
      "<div class='modal-header'>" +
        "<button type='button' class='close'>x</button>" +
        "<h1 class='text-center text-primary'>Please wait...</h1>" +
      "</div><div class='modal-body'>" +
          "<div class='progress'>" +
    "<div class='progress-bar progress-bar-striped active' role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 100%;'>" +
    "<span class='sr-only'>100% Complete</span>"+
    "</div>" +
    "</div>" +
      "</div>" +
      "<div class='modal-footer'>" +
      "</div>" +
    "</div>" +
  "</div>" +
"</div>");
  return data;
}
function content() {
    var data = $("<div>Please wait...</div><div class='progress' style='Width:250px;'>" +
    "<div class='progress-bar progress-bar-striped active' role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 100%;'>" +
    "<span class='sr-only'>100% Complete</span>"+
    "</div>" +
    "</div>");
    return data;
}
$(function(){
    $('#alternation').click(function(){
        $('tbody > tr:odd', $('#table_cases')).toggleClass('alternation');
    });

    $('#table_cases').ready(tableDropdown);
    //('#sort').click(tableDropdown);
});
function tableDropdown()
{
    var caseTableName = "table_cases"
    var idColNum = 0
    var stepColNum = 1
    var tbody = $('#' + caseTableName + ' > tbody');
    var rows = tbody.children();
    var selectedRow;
    //压下鼠标时选取行
    rows.mousedown(function(){
        selectedRow = this;
        tbody.css('cursor', 'move');
        return false;	//防止拖动时选取文本内容，必须和 mousemove 一起使用
    });
    rows.mousemove(function(){
        return false;	//防止拖动时选取文本内容，必须和 mousedown 一起使用
    });
    //释放鼠标键时进行插入
    rows.mouseup(function(){
//        if(selectedRow)
//        {
//            if(selectedRow != this)
//            {
//                thisRowNum = parseInt($(this).children("td").get(idColNum).innerHTML)
//                selectedRownNum = parseInt($(selectedRow).children("td").get(idColNum).innerHTML)
//                tmp = rows.eq(thisRowNum - 1).children("td").get(stepColNum).innerHTML
//                rows.eq(thisRowNum - 1).children("td").get(stepColNum).innerHTML = rows.eq(selectedRownNum - 1).children("td").get(stepColNum).innerHTML
//                rows.eq(selectedRownNum - 1).children("td").get(stepColNum).innerHTML = tmp
//                $(this).fadeOut("fast").fadeIn("fast");
//            }
//            tbody.css('cursor', 'default');
//            selectedRow = null;
//        }
        if(selectedRow)
        {
            if(selectedRow != this)
            {
                try{
                    thisRowNum = parseInt($(this).children("td").get(idColNum).innerHTML)
                    selectedRownNum = parseInt($(selectedRow).children("td").get(idColNum).innerHTML)
                    if((thisRowNum - selectedRownNum >= 1) || (thisRowNum == rows.length))
                    {
                        $(this).after($(selectedRow)).removeClass('mouseOver');
                    }
                    else
                    {
                        $(this).before($(selectedRow)).removeClass('mouseOver');
                    }
                }
                catch(e){}
                rows = tbody.children();
                for(var i=0;i<rows.length;i++){
                    rows.eq(i).children("td").get(0).innerHTML = i + 1;
                }
            }
            tbody.css('cursor', 'default');
            selectedRow = null;
        }
    });
    //标示当前鼠标所在位置
    rows.hover(
        function(){
            if(selectedRow && selectedRow != this)
            {
                $(this).addClass('mouseOver');
            }
        },
        function(){
            if(selectedRow && selectedRow != this)
            {
                $(this).removeClass('mouseOver');
            }
        }
    );

    tbody.mouseover(function(event){
        event.stopPropagation();
    });
    $('#contain').mouseover(function(event){
        if($(event.relatedTarget).parents('#content'))
        {
            tbody.css('cursor', 'default');
            selectedRow = null;
        }
    });
}
function getModalHtml(content){
     return   "<div class='modal fade' id='changeDigitModal' >"
            + "<div class='modal-backdrop in' style='opacity:0;'></div>"
            + "<div class='modal-dialog' style='z-index:2901; margin-top:60px; width:400px;'>"
            + "<div class='modal-content'>"
            + "<div class='modal-header'  style='font-size:16px;'>"
            + "<span class='glyphicon glyphicon-info-sign'>&nbsp;</span><button type='button' class='close' data-dismiss='modal'>"
            + "<span style='font-size:20px;' class='glyphicon glyphicon-remove'></span></button></div>"
            + "<div class='modal-body text-center' id='myConfirmContent' style='font-size:18px; '>"
            + content
            + "</div>"
            + "<div class='modal-footer' style=''>"
            + "<button id='button_close_dynamic_modal' type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"
            + "<button id='button_save_dynamic_modal' type='button' class='btn btn-primary' data-dismiss='modal' onclick=\"button_save_dynamic_modal_clicked();\">Save</button>"
            + "</div>" + "</div></div></div>";
}
function get_dialog_content_for_add_new(obj){
    value = $(obj).val();
    if(value.trim() == ""){
        return "The value can not be empty."
    }
    if(obj == "#input_new_page"){
        if($('#button_select_page').text().trim() == SELECT_PAGE || $('#button_select_page').text().trim() == ""){
            return "Please select an item."
        }
    }
    else if(obj == "#input_new_subpage"){
        if($('#button_select_subpage').text().trim() == SELECT_SUBPAGE || $('#button_select_subpage').text().trim() == ""){
            return "Please select an item."
        }
    }
    else if(obj == "#input_new_element"){
        if($('#button_select_element').text().trim() == SELECT_ELEMENT || $('#button_select_element').text().trim() == ""){
            return "Please select an item."
        }
    }
}

$(document).ready(function(){

    var confirmDialogContent = "";
    var removeContentOfDialog = 'Are you sure to delete?'

    $("#button_select_page").click(function(){
        if($("#ul_pages").css("display") == "block"){
            $("#ul_pages").css("display","");
            $("#button_select_page").click(); // need click twice to open/close?
            return;
        }
    });
    $("#button_select_subpage").click(function(){
        if($("#ul_subpages").css("display") == "block"){
            $("#ul_subpages").css("display","");
            $("#button_select_subpage").click(); // need click twice to open/close?
            return;
        }
    });
    $("#button_select_element").click(function(){
        if($("#ul_elements").css("display") == "block"){
            $("#ul_elements").css("display","");
            $("#button_select_element").click(); // need click twice to open/close?
            return;
        }
    });

//    $('#table_locators, #table_page_subpage_element').on("click",".glyphicon-remove, .glyphicon-plus",function(){
    $('#table_locators, #table_page_subpage_element').on("click",".glyphicon-remove, .glyphicon-plus",function(e){
        var getThis = $(this); //$(this) is different  in $.confirm({
        var currentParentObjectId = getThis.parents("table:eq(0)").attr('id');
        var currentObjectClass = getThis.attr('class');
        var currentObjectId = getThis.attr('id');
//        var rowNeedRemove = getThis.parents("tr:eq(0)");

        if (('table_locators' == currentParentObjectId) && (currentObjectClass == "glyphicon glyphicon-remove")){
            rowNeedRemove = getThis.parents("tr:eq(0)");
            removeLocatorRow(rowNeedRemove);
            return;
            confirmDialogContent = removeContentOfDialog;
        }
        else if(('table_page_subpage_element' == currentParentObjectId) && (currentObjectClass == "glyphicon glyphicon-remove")){

            var ul_clicked_id = getThis.parents("ul:eq(0)").attr('id');
            $("#" + ul_clicked_id).css("display","block");
            var li_clicked_value = getThis.prev().text();
            var subpage_name = $('#button_select_subpage').text().trim();
            var page_name = $('#button_select_page').text().trim();
            var element_name = $('#button_select_element').text().trim();
            getThis.prev().remove();
            getThis.remove();
            if($("#" + ul_clicked_id + " li").length == 0){
                $("#" + ul_clicked_id).css("display","");
            }
            if(ul_clicked_id == "ul_pages"){
                addRemoveElementToJson("remove", li_clicked_value, SELECT_ELEMENT, SELECT_SUBPAGE);
                if(li_clicked_value == page_name){
                    $('#button_select_page').text(SELECT_PAGE);
                    reset_ul_subpages();
                    reset_ul_elements();
                }
            }
            else if(ul_clicked_id == "ul_subpages"){
                addRemoveElementToJson("remove", page_name, SELECT_ELEMENT, li_clicked_value);
                if(li_clicked_value == subpage_name){
                    $('#button_select_subpage').text(SELECT_SUBPAGE);
                    reset_ul_elements();
                }
            }
            else if(ul_clicked_id == "ul_elements"){
                addRemoveElementToJson("remove", page_name, li_clicked_value, subpage_name);
                if(li_clicked_value == element_name){
                    $('#button_select_element').text(SELECT_ELEMENT);
                    reset_ul_elements();
                }
            }

            return;
            confirmDialogContent = removeContentOfDialog;
        }
        else if('table_page_subpage_element' == currentParentObjectId && currentObjectClass == "glyphicon glyphicon-plus"){
            return;
            if (currentObjectId == "button_add_page"){
                confirmDialogContent = get_dialog_content_for_add_new("#input_new_page");
            }
            else if (currentObjectId == "button_add_subpage"){
                confirmDialogContent = get_dialog_content_for_add_new("#input_new_subpage");
            }
            else if (currentObjectId == "button_add_element"){
                confirmDialogContent = get_dialog_content_for_add_new("#input_new_element");
            }
        }
        $.confirm({
            buttons: {
                confirm: {
                    btnClass: 'btn-blue',
                    action: function(){
                        if ('table_locators' == currentParentObjectId && currentObjectClass == "glyphicon glyphicon-remove"){

                        }
                        else if(('table_page_subpage_element' == currentParentObjectId) && (currentObjectClass == "glyphicon glyphicon-remove")){

                        }
                    }
                },
                cancel: function () {
                     return;
                }
            },
            title: TITLE_DIALOG_TIP,
            content: confirmDialogContent,
//            draggable: true,
//            onOpen: function(action){
//
//            }
        });
    });

function lightCopy(obj){
    return $.extend({}, obj);
}
function deepCopy(obj){

//    try{
//        alert(11);
////        return $.extend(true, {}, obj);
//    }
//    catch(e){alert(e);}
}



//    $('.glyphicon-remove, .glyphicon-plus').click(function(){ // only bind which has existed.
////        var content = $(this).children("td:eq(0)").text();
//        if ('table_locators' != $(this).parents("table:eq(0)").attr('id')){
//            var html = getConfirmModalHtml("");
//            $("body").append(html);
//            $("#myConfirm").modal("show");
//        }
//        else {
//
//        }
//    });
});
