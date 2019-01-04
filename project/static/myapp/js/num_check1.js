function kp1(txt){
                <!--var kp = function(txt){-->
                    if(!/^([1-9]|10)$/.test(txt.value)){
                        txt.style.borderColor = "red";
                        s = txt.value * 1;
                        <!--return false;-->
                        document.all.btn1.disabled=true;
                    }else{
                        txt.style.borderColor = "";
                        s = "-11";
                        <!--return true;-->
                        document.all.btn1.disabled=true;
                    }
                }
                function judge1(){
                                    var c = 0;

                            if(s > 10 || s == 0){
                                alert("请输入数字1-10")
                                <!--return false;-->
                        document.all.btn1.disabled=true;
                        return;
                            }
                            if(s == "-11"){
                                    <!--return turn;-->
                                    var list = document.getElementsByTagName("input");
                                    var regexp1 = /^([1-9]|10)$/;
                                    for (var i = 0; i < list.length; i++) {
                                    // 判断是否为文本框
                                        if (list[i].type == "text") {
                                        // 判断文本框是否为空
                                            if (list[i].value == "") {
                                            document.all.btn1.disabled=true;}
                                            //判断list的第i个值是否为1-10
                                             if (list[i].value > 10 || list[i].value < 1) {
                                                c = c + 1;
                                             <!--if(!regexp1.test(list[i].value)){-->
                                            <!--if (!list[i].value < 11 ) {-->
                                                <!--if (list[i].value > 0 ) {-->
                                                    document.all.btn1.disabled=true;}

                                }
                                if(c == 0) {
                                    document.all.btn1.disabled=false;}
                                }

                                }

                             else{
                                alert("格式不对");
                        document.all.btn1.disabled=true;
                         }
    }
