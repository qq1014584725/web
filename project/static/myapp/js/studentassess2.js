 function change2(){
        var c = 0;
        var list = document.getElementsByTagName("select");
        for (var i = 0; i < list.length; i++) {
            if (list[i].value == "") {
                c = c + 1;
                 document.all.btn2.disabled=true;}
            if (c == 0){
                document.all.btn2.disabled=false;}
        }
        }