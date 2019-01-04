function showTime()
        {
            var time = new Date();
            var year=time.getFullYear();
            var month=time.getMonth()+1;
        if(month<10)
        {
            month="0"+month;
        }
        var day=time.getDate();
        if(day<10)
        {
            day="0"+day;
        }
        var hour=time.getHours();
        if(hour<10)
        {
            hour="0"+hour;
        }
        var minute=time.getMinutes();
        if(minute<10)
        {
            minute="0"+minute;
        }
        var second=time.getSeconds();
        if(second<10)
        {
            second="0"+second;
        }
        var wd= time.getDay();
        switch(wd)
        {
            case 0:
            wd="星期日";
            break;
            case 1:
            wd="星期一";
            break;
            case 2:
            wd="星期二";
            break;
            case 3:
            wd="星期三";
            break;
            case 4:
            wd="星期四";
            break;
            case 5:
            wd="星期五";
            break;
            case 6:
            wd="星期六";
            break;
        }
        document.timeform.timearea.value= year+"年"+month+"月"+day+"日"+" "+wd+" "+hour+":"+ minute+":"+second;
        setTimeout("showTime()",1000);
        }