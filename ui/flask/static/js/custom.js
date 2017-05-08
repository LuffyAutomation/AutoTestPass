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