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

$(function(){
    $('#alternation').click(function(){
        $('tbody > tr:odd', $('#example')).toggleClass('alternation');
    });

    $('#example').ready(tableDropdown);
    //('#sort').click(tableDropdown);
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
//function content() {
//  var data = $("<div id='loginModal' class='modal show'>" +
//  "<div class='modal-dialog'>" +
//    "<div class='modal-content'>" +
//      "<div class='modal-header'>" +
//        "<button type='button' class='close'>x</button>" +
//        "<h1 class='text-center text-primary'>登录</h1>" +
//      "</div><div class='modal-body'><form action='' class='form col-md-12 center-block'>" +
//          "<div class='form-group'><input type='text' class='form-control input-lg' placeholder='电子邮件'></div>" +
//          "<div class='form-group'>" +
//            "<input type='password' class='form-control input-lg' placeholder='登录密码'>" +
//          "</div>" +
//          "<div class='form-group'>" +
//            "<button class='btn btn-primary btn-lg btn-block'>立刻登录</button>" +
//            "<span><a href='#'>找回密码</a></span>" +
//            "<span><a href='#' class='pull-right'>注册</a></span>" +
//          "</div>" +
//        "</form>" +
//      "</div>" +
//      "<div class='modal-footer'>" +
//      "</div>" +
//    "</div>" +
//  "</div>" +
//"</div>");
//  return data;
//}

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
function tableDropdown()
{
    var caseTableName = "example"
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
        if(selectedRow)
        {
            if(selectedRow != this)
            {
                thisRowNum = parseInt($(this).children("td").get(idColNum).innerHTML)
                selectedRownNum = parseInt($(selectedRow).children("td").get(idColNum).innerHTML)
//                maxRowNum = 1
//
//
//                tmax = Math.max(thisRowNum, selectedRownNum)

//              $(this).before($(selectedRow)).removeClass('mouseOver');
                tmp = rows.eq(thisRowNum - 1).children("td").get(stepColNum).innerHTML
                rows.eq(thisRowNum - 1).children("td").get(stepColNum).innerHTML = rows.eq(selectedRownNum - 1).children("td").get(stepColNum).innerHTML
                rows.eq(selectedRownNum - 1).children("td").get(stepColNum).innerHTML = tmp
                $(this).fadeOut().fadeIn();
//                tbody = $('#example > tbody');
//                var rows = tbody.children();
//                for(var i=0; i <tmax; i++)
//                {
//                    rows.eq(i).children("td").get(0).innerHTML = i + 1
//                }
//                alert("thisRowNum:" + thisRowNum + "   selectedRownNum:" + selectedRownNum)

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
                $(this).addClass('mouseOver');	//区分大小写的，写成 'mouseover' 就不行
            }
        },
        function(){
            if(selectedRow && selectedRow != this)
            {
                $(this).removeClass('mouseOver');
            }
        }
    );

    //当用户压着鼠标键移出 tbody 时，清除 cursor 的拖动形状，以前当前选取的 selectedRow
    tbody.mouseover(function(event){
        event.stopPropagation(); //禁止 tbody 的事件传播到外层的 div 中
    });
    $('#contain').mouseover(function(event){
        if($(event.relatedTarget).parents('#content')) //event.relatedTarget: 获取该事件发生前鼠标所在位置处的元素
        {
            tbody.css('cursor', 'default');
            selectedRow = null;
        }
    });
}