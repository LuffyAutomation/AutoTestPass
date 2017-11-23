$( "#edit_newProject, #edit_newPage").keyup(function() {
  this.value=this.value.replace(/^_*/g,'').replace(/[^a-zA-Z_]/g,'')
});