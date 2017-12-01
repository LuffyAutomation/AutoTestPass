$("#input_new_project, #input_new_page, #input_new_sub_page").keyup(function() {
  this.value = this.value.replace(/^_*/g,'').replace(/[^a-zA-Z_]/g,'');
});

$("#input_new_element").keyup(function() {
  this.value = this.value.replace(/^_*/g,'').replace(/[^a-zA-Z_]/g,'');
  if(this.value == ""){

  }
});

var name_page = "";
$("#ul_page_names li a").click(function(){
    name_page = $(this).html();
    $("#button_select_page").html(name_page + "<span class='caret'></span>");
//    alert($("#button_select_page").html());
});