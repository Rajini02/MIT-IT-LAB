function fun() {
    var adj=document.getElementById("userinput").value;
    var arr=[];
    for (var i = 0; i < adj.length; i++) {         
        for (var j = 0; j < adj.length; j++) {        
            for (var k = 0; k < adj.length; k++) {     
                if (i == j || i == k || j == k) continue;  
                let res=adj.charAt(i)+adj.charAt(j)+adj.charAt(k);
                 var link ='https://wordsapiv1.p.mashape.com/words/';
                 link=link+res;
                    const response = fetch(link);
                    if(response){
                        arr.push(res);
                    }
                   
                  }
            }
        }
    }
    console.log(arr);
    document.getElementById("text").innerHTML =arr;
