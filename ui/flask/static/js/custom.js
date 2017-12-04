var whichRowLaunchedAddLocatorsModal = 0;
var whichElementClicked = "";
var list_locators = [];
var SELECT_PAGE = "Select Page";
var SELECT_SUB_PAGE = "Select Sub Page";
//jsonUiMap = null;
//jsonUiMapPages = null;
//for(var i=0; i<jsonUiMapPages.length; i++){
//    alert(typeof(jsonUiMapPages[i]["@name1"]) == "undefined");
//    alert(jsonUiMapPages[i]["@name"]);
//}

function assemblePagesDropdown(){
    var newRow="";
//    var listOfUiMapPages = new Array();
    for(var i=0; i<jsonUiMapPages.length; i++){
//      listOfUiMapPages.push(jsonUiMapPages[i]["@name"]);
        alert(jsonUiMapPages[i]['@name']);
        newRow="<li><a href='#' onclick=\"li_new_page_on_click('"  + jsonUiMapPages[i]['@name'] +  "');\">" + jsonUiMapPages[i]['@name'] + "</a></li>";
        alert(newRow);
        //$('#ul_new_page').html(newRow);
        $('#ul_new_page').append(newRow);
    }
}
function li_new_page_on_click(){
    alert(1);
}

$("#ul_new_page li").on("click",function(){
    alert(1);
    //Can not find out the ele that created dynamically. Need other method.
});

$("#input_new_page").ready(function(){
    assemblePagesDropdown();
});

$("#table_cases td a").click(function(){
    if("#addLocatorModal" == $(this).attr("data-target")){
        whichElementClicked = $(this).html();
         $("#button_select_page").html(name_page + "<span class='caret'></span>");
    }
});
$("#button_confirm_add_locator").click(function(){
    if("#addLocatorModal" == $(this).attr("data-target")){
        whichElementClicked = $(this).html();
         $("#button_select_page").html(name_page + "<span class='caret'></span>");
    }
});

//$("#table_cases td").click(function(){
//    $('#table_locators tr').remove();
////      var tdSeq = $(this).parent().find("td").index($(this)[0]);
//    whichRowLaunchedAddLocatorsModal = $(this).parent().parent().find("tr").index($(this).parent()[0]);
//});

function appendLocatorRow(locatorType, tableId){
	alert(whichRowLaunchedAddLocatorsModal);
	var newRow="<tr>" +
                    "<td style='width:120px;'>" + locatorType + "</td>" +
                    "<td><input type='text' class='form-control'/></td>" +
                    "<td style='width:30px;'><a class='glyphicon glyphicon-remove'/></td>" +
                "</tr>";
	$('#' + tableId).append(newRow);
}

function removeLocatorRow(rowNeedRemove){
    rowNeedRemove.remove();
}



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

//var addLocatorRowInnerHtml = ;
//function appendRow(id, rowInnerHtml){
//    $(id).append(rowInnerHtml);
//}
//function delRow(id, rowInnerHtml){
//    $(id).append(rowInnerHtml);
//}


var removeContentOfDialog = 'Are you sure to delete?'

$(document).ready(function(){
//bind remove glyphiconf by table
    $('#table_locators').on("click",".glyphicon-remove",function(){
        var rowNeedRemove = $(this).parents("tr:eq(0)");
        $.confirm({
            title: '!',
            content: removeContentOfDialog,
            draggable: true,
            buttons: {
                confirm: {
                    btnClass: 'btn-blue',
                    action: function(){
                        removeLocatorRow(rowNeedRemove);
                    }
                },
                cancel: function () {
                     return;
                }
            }
        });
    });
    //bind all remove glyphiconf
    $('.glyphicon-remove').click(function(){ // only bind which has existed.
//        var content = $(this).children("td:eq(0)").text();
        if ('table_locators' != $(this).parents("table:eq(0)").attr('id')){
            var html = "<div class='modal fade' id='myConfirm' >"
                + "<div class='modal-backdrop in' style='opacity:0;'></div>"
                + "<div class='modal-dialog' style='z-index:2901; margin-top:60px; width:400px;'>"
                + "<div class='modal-content'>"
                + "<div class='modal-header'  style='font-size:16px;'>"
                + "<span class='glyphicon glyphicon-info-sign'>&nbsp;</span><button type='button' class='close' data-dismiss='modal'>"
                + "<span style='font-size:20px;' class='glyphicon glyphicon-remove'></span></button></div>"
                + "<div class='modal-body text-center' id='myConfirmContent' style='font-size:18px; '>"
                + removeContentOfDialog
                + "</div>"
                + "<div class='modal-footer' style=''>"
                + "<button class='btn btn-primary' id='confirmOk'>Confirm<Button>"
                + "<button class='btn btn-default' data-dismiss='modal'>Cancel<Button>"
                + "</div>" + "</div></div></div>";
            $("body").append(html);
            $("#myConfirm").modal("show");
        }
        else {

        }



//        $(this).parents("tr:eq(0)").remove();
    });
});
