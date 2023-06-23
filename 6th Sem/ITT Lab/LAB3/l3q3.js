function fun() {
    var adj=document.getElementById("userinput").value;
    const letter = adj.split("");
    if (letter.length>10){
        document.getElementById("text").innerHTML ="Please enter 10-digit number.";
    }
    else{
        var res = adj.replace(/\D/g,'').substr(0, 3);
        var res2 = adj.replace(/\D/g,'').substr(3,11);
        console.log(res);
        console.log(adj);
        document.getElementById("text").innerHTML =res+" "+res2;
    }
}