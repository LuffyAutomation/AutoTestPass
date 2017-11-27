$("#edit_newProject, #edit_newPage").keyup(function() {
  this.value=this.value.replace(/^_*/g,'').replace(/[^a-zA-Z_]/g,'')
});

var name_page = ""
$("#ul_page_names li a").click(function(){
    name_page = $(this).html();
    $("#button_select_page").html(name_page + "<span class='caret'></span>");
//    alert($("#button_select_page").html());
});