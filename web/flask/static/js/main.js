/*!
*
*
*
*/
function mouseOver(){
    try{
          document.getElementsByName('cc').item(0).style.height = "120px";

       }
    catch(e){alert(e.message);}
}
function mouseOut(){
        try{
            //document.getElementsByName('cc').item(0).scrollTop = 0;
            document.getElementsByName('cc').item(0).style.height = "20px";
            }
    catch(e){alert(e.message);}
}
function mainSubmit(mainForm){
    try{
        if (isNaN(mainForm.FlatBedPosition.value)){
            alert("Please input number in [Flatbed Postion in Readiris] textbox.")
            return 0;
        }
        if (mainForm.FlatBedPosition.value <= 0){
            alert("The value of [Flatbed Postion in Readiris] textbox should be larger than 0.")
            return 0;
        }
        mainForm.submit();
    }
    catch(e){alert(e.message);}
}
