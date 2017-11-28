var test1 = ""
$("#edit_newProject, #edit_newPage").keyup(function() {
  this.value=this.value.replace(/^_*/g,'').replace(/[^a-zA-Z_]/g,'')
});
$("#edit_add_new_element").keyup(function() {
  this.value=this.value.replace(/^_*/g,'').replace(/[^a-zA-Z_]/g,'')
  if(this.value == ""){

  }
  alert(test1);
});
var name_page = ""
$("#ul_page_names li a").click(function(){
    name_page = $(this).html();
    $("#button_select_page").html(name_page + "<span class='caret'></span>");
//    alert($("#button_select_page").html());
});