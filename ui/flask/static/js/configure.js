/*!
*
*
*
*/
function MoveDown(e2){
    try{
        var FirstSelectedIndex = 0, LastSelectedIndex = 0;
        FirstSelectedIndex = e2.options.selectedIndex;
        if  (FirstSelectedIndex != -1) {
            LastSelectedIndex = FirstSelectedIndex;
            try{
                for(var i=FirstSelectedIndex + 1;i<e2.options.length;i++){
                    if(e2.options[i].selected){
                        LastSelectedIndex = i;
                    }
                    else{
                        break;
                    }
                }
            }
            catch(e){}
            if (LastSelectedIndex == e2.options.length -1){
                return;
            }
            var selectedItemsCount = LastSelectedIndex - FirstSelectedIndex + 1;
            var tmpNextLastSelected = e2.options[LastSelectedIndex + 1].text
            for(var i=0;i<selectedItemsCount;i++){
                e2.options[LastSelectedIndex - i + 1].text = e2.options[LastSelectedIndex - i].text;
                e2.options[LastSelectedIndex - i + 1].value = e2.options[LastSelectedIndex - i].text;
                e2.options[LastSelectedIndex - i + 1].selected = true;
            }
            e2.options[FirstSelectedIndex].text = tmpNextLastSelected;
            e2.options[FirstSelectedIndex].value = tmpNextLastSelected;
            e2.options[FirstSelectedIndex].selected = false;
            for(var i=0;i<e2.options.length;i++){
                    e2.options[i].text = e2.options[i].text.replace(e2.options[i].text.split('-')[0] + "-", (i + 1 + "-"));
                    e2.options[i].value = e2.options[i].value.replace(e2.options[i].value.split('-')[0] + "-", (i + 1 + "-"));
            }
        }
    }
    catch(e){alert(e.message);}
}
function MoveUp(e2){
    try{
        var FirstSelectedIndex = 0, LastSelectedIndex = 0;
        FirstSelectedIndex = e2.options.selectedIndex;
        if  ((FirstSelectedIndex != -1) && (FirstSelectedIndex != 0)){
            LastSelectedIndex = FirstSelectedIndex;
            try{
                for(var i=FirstSelectedIndex + 1;i<e2.options.length;i++){
                    if(e2.options[i].selected){
                        LastSelectedIndex = i;
                    }
                    else{
                        break;
                    }
                }
            }
            catch(e){}
            var selectedItemsCount = LastSelectedIndex - FirstSelectedIndex + 1;
            var tmpPreviousFirstSelected = e2.options[FirstSelectedIndex - 1].text
            for(var i=0;i<selectedItemsCount;i++){
                e2.options[FirstSelectedIndex + i - 1].text = e2.options[FirstSelectedIndex + i].text;
                e2.options[FirstSelectedIndex + i - 1].value = e2.options[FirstSelectedIndex + i].text;
                e2.options[FirstSelectedIndex + i - 1].selected = true;
            }
            e2.options[LastSelectedIndex].text = tmpPreviousFirstSelected;
            e2.options[LastSelectedIndex].value = tmpPreviousFirstSelected;
            e2.options[LastSelectedIndex].selected = false;
            for(var i=0;i<e2.options.length;i++){
                    e2.options[i].text = e2.options[i].text.replace(e2.options[i].text.split('-')[0] + "-", (i + 1 + "-"));
                    e2.options[i].value = e2.options[i].value.replace(e2.options[i].value.split('-')[0] + "-", (i + 1 + "-"));
            }
        }
    }
    catch(e){alert(e.message);}
}
function AddConfig(e1, e2 , numRecord){
    try{
        var numRightList = parseInt(numRecord.value)
        //var numRightList = GetRightListMarkNum(e2)
        for(var i=0;i<e1.options.length;i++){
            if(e1.options[i].selected){
                var e = e1.options[i];
                var e2Num = 1
                if (e2.options.length > 0) {
                    e2Num = e2.options.length + 1
                }
                e2.options.add(new Option(e2Num + "-" + getConfigName(e.text) + (numRightList + 1), e2Num + "-" + getConfigName(e.value) + (numRightList + 1)));
                numRightList += 1;
                numRecord.value = parseInt(numRecord.value) + 1;
                e1.options[i].selected = false;
                i = i - 1;
            }
        }
    }
    catch(e){alert(e.message);}
}
function AddAllConfig(e1, e2 , numRecord){
    try{
        var numRightList = parseInt(numRecord.value)
        //var numRightList = GetRightListMarkNum(e2)
        for(var i=0;i<e1.options.length;i++){
                var e = e1.options[i];
                var e2Num = 1
                if (e2.options.length > 0) {
                    e2Num = e2.options.length + 1
                }
                e2.options.add(new Option(e2Num + "-" + getConfigName(e.text) + (numRightList + 1), e2Num + "-" + getConfigName(e.value) + (numRightList + 1)));
                numRightList += 1;
                numRecord.value = parseInt(numRecord.value) + 1;
                e1.options[i].selected = false;
        }
    }
    catch(e){alert(e.message);}
}
function DelConfig(e2){
    try{
        var n = 1;
        for(var i=0;i<e2.options.length;i++){
            if(e2.options[i].selected){
                n += 1;
            }
          }
        for(var i=0;i<n;i++){
            for(var i=0;i<e2.options.length;i++){
                if(e2.options[i].selected){
                    e2.remove(i);
                    break;
                }
            }
        }
        for(var i=0;i<e2.options.length;i++){
                e2.options[i].text = e2.options[i].text.replace(e2.options[i].text.split('-')[0] + "-", (i + 1 + "-"));
                e2.options[i].value = e2.options[i].value.replace(e2.options[i].value.split('-')[0] + "-", (i + 1 + "-"));
        }
    }
    catch(e){alert(e.message);}
}
function DelAllConfigs(e2){
    try{
        var t = e2.options.length
        for(var i= 0;i < t ; i++){
                e2.remove(0);
        }
    }
    catch(e){alert(e.message);}
}
function GotoSetSettings(e2, selectedXmlName, configForm){
    try{
        for(var i=0;i<e2.options.length;i++){
            if(e2.options[i].selected){
                ListRightSelectAll(e2)
                selectedXmlName.value = e2.options[i].text;
                if (selectedXmlName.value.indexOf('LoopScan.xml') != -1){
                    configForm.handleEvent.value = 'EditScanSettings'
                }
                else if (selectedXmlName.value.indexOf('SendEmail.xml') != -1){
                    configForm.handleEvent.value = 'Edit'
                }
                else{
                    alert("Only LoopScan.xml supports Edit.");
                    return 0;
                }
                configForm.submit();
                //window.location.href = "/setSettings";
                return 0;
                //alert("The selected .xml does not support EDIT.");
            }
        }
        alert("Please select a xml file.");
    }
    catch(e){alert(e.message);}
}
function saveConfig(e2, configForm){
    try{
        if(e2.options.length > 0){
            ListRightSelectAll(e2)
            configForm.handleEvent.value = 'Save'
            configForm.submit();
            return 0;
        }
        alert("Please add one of xml files at least.");
    }
    catch(e){alert(e.message);}
}

function saveCancelSettings(settingsForm, status){
    try{
        if (status == 0) {
            settingsForm.handleSetSettingsEvent.value = 'Cancel'
        }
        else{
           settingsForm.handleSetSettingsEvent.value = 'Save'
        }
        alert(settingsForm.handleSetSettingsEvent.value);
        settingsForm.submit();
        return 0;
    }
    catch(e){alert(e.message);}
}
function GetRightListMarkNum(e2){
    var a = 0;
    try{
        for(var i=0;i<e2.options.length;i++){
            try{
                if (parseInt((e2.options[i].text).split(".xml")[1]) > a){
                    a = parseInt((e2.options[i].text).split(".xml")[1]);
                }
            }
            catch(e){return 0;}
            }
        return a;
        }
    catch(e){alert(e.message);}
}
function ListRightSelectAll(e2){
    try{
        //alert(e1.options.length);
        for(var i=0;i<e2.options.length;i++){
                e2.options[i].selected = true
            }
        }
    catch(e){}
}
function getConfigName(e2){
    var t = e2.split("-")[0];
    var a = t + "-";
    return e2.replace(a, "");
}

function moveOptionOld(e1, e2){
    try{
        for(var i=0;i<e1.options.length;i++){
            if(e1.options[i].selected){
                var e = e1.options[i];
                e2.options.add(new Option(e.text, e.value));
                e1.remove(i);
                i=i-1
            }
        }
    document.configForm.city.value=getvalue(document.configForm.listRight);
    }
    catch(e){alert(e)}
}

function getvalue(geto){
    var allvalue = "";
    for(var i=0;i<geto.options.length;i++){
        allvalue +=geto.options[i].value + ",";
    }
    return allvalue;
}
function changepos(obj,index){
    if(index==-1){
        if (obj.selectedIndex>0){
            obj.options(obj.selectedIndex).swapNode(obj.options(obj.selectedIndex-1))
        }
    }else if(index==1){
        if (obj.selectedIndex<obj.options.length-1){
            obj.options(obj.selectedIndex).swapNode(obj.options(obj.selectedIndex+1))
        }
    }
}