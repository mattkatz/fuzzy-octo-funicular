//######################################################################################
// Author: ricocheting.com
// Version: v2.0
// Date: 2011-03-31
// Description: displays the amount of time until the "dateFuture" entered below.

// NOTE: the month entered must be one less than current month. ie; 0=January, 11=December
// NOTE: the hour is in 24 hour format. 0=12am, 15=3pm etc
// format: dateFuture1 = new Date(year,month-1,day,hour,min,sec)
// example: dateFuture1 = new Date(2003,03,26,14,15,00) = April 26, 2003 - 2:15:00 pm

dateFuture1 = new Date(2029,8,6,0,1,00);

// TESTING: comment out the line below to print out the "dateFuture" for testing purposes
//document.write(dateFuture +"<br />");


//###################################
//nothing beyond this point
function GetCount(ddate,element_or_id){

    dateNow = new Date();//grab current date
    amount = ddate.getTime() - dateNow.getTime();//calc milliseconds between dates
    delete dateNow;
    let element = element_or_id;
    if(typeof(element_or_id) === "string"){
      element = document.getElementById(element_or_id);
    }


    // if time is already past
    if(amount < 0){
          element.innerHTML="Now!";
        }
    // else date is still good
    else{
          years=0;weeks=0;days=0;hours=0;mins=0;secs=0;out="";

          amount = Math.floor(amount/1000);//kill the "milliseconds" so just secs

          years=Math.floor(amount/31536000);//years (no leapyear support)
          amount=amount%31536000;

          weeks=Math.floor(amount/604800);//weeks
          amount=amount%604800;

          days=Math.floor(amount/86400);//days
          amount=amount%86400;

          hours=Math.floor(amount/3600);//hours
          amount=amount%3600;

          mins=Math.floor(amount/60);//minutes
          amount=amount%60;

          secs=Math.floor(amount);//seconds

          out += years +" "+((years==1)?"year":"years")+", ";
          out += weeks +" "+((weeks==1)?"week":"weeks")+", ";
          out += days +" "+((days==1)?"day":"days")+", ";
          if(hours != 0){out += hours +" "+((hours==1)?"hour":"hours")+", ";}
          out += mins +" "+((mins==1)?"min":"mins")+", ";
          out += secs +" "+((secs==1)?"sec":"secs")+", ";
          out = out.substr(0,out.length-2);
          element.innerHTML=out;

          setTimeout(function(){GetCount(ddate,element)}, 1000);
        }
}

window.onload=function(){
  elements = document.getElementsByClassName("timer")
  for(let element of elements){
    let countdown_date = new Date(element.getAttribute("data-date"));
    GetCount(countdown_date, element);
  }
    //GetCount(dateFuture1, 'timer0');
    //you can add additional countdowns here (just make sure you create dateFuture2 and countbox2 etc for each)
};
