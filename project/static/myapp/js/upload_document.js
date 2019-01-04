function fileChange1(target){
//检测上传文件的类型
var imgName = document.all.up_file1.value;
<!--var imgName = document.all.up_file2.value;-->
     var ext,idx;
    if (imgName == ''){
       document.all.submit_upload1.disabled=true;
        <!--alert("请选择需要上传的文件!");-->
        return;
    } else {
        idx = imgName.lastIndexOf(".");
        if (idx != -1){
            ext = imgName.substr(idx+1).toUpperCase();
            ext = ext.toLowerCase( );
           // alert("ext="+ext);
            if (ext != 'pdf'){
              document.all.submit_upload1.disabled=true;
                alert("只能上传 .pdf 类型的文件!");
                return;
            }
        } else {
          document.all.submit_upload1.disabled=true;
           alert("只能上传.pdf 类型的文件!");
            return;
        }
    }

    //检测上传文件的大小
    var isIE = /msie/i.test(navigator.userAgent) && !window.opera;
    var fileSize = 0;
    if (isIE && !target.files){
        var filePath = target.value;
        var fileSystem = new ActiveXObject("Scripting.FileSystemObject");
        var file = fileSystem.GetFile (filePath);
        fileSize = file.Size;
    } else {
        fileSize = target.files[0].size;
    }

    var maxsize = 400* 1024*1024;

    if(fileSize>maxsize){
    document.all.submit_upload1.disabled=true;
        alert("文件大小不能超过400M");
    }else{
    document.all.submit_upload1.disabled=false;
    }
}