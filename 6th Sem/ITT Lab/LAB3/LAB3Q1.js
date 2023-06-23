var size=5;
var flag=0;
var text1="8=";
function shrink(){
    text="8="
    if(size ==55)
    {
        flag=1;
    }
    else if(size==15){
        flag=0;
    }   
    if(flag==0){
        text1+="=";
        size+=10;
        document.getElementById("text").innerHTML =text1+"D";
        // document.getElementById("talk").innerHTML ="When Sonam Bajwa";
        document.getElementById("text").setAttribute("style","font-size:"+size+"pt;color:red;");
        
    }
    if(flag==1){
        size-=10;
        text1=text1.replace('=','')
        document.getElementById("text").innerHTML = text1+"D";
        // document.getElementById("talk").innerHTML ="When Nisha";
        document.getElementById("text").setAttribute("style","font-size:"+size+"pt;color:blue;");
        
}
setTimeout(shrink,1000);
}