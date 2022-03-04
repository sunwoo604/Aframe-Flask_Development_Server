let log_beta=""
let molecules=""
let output=[]
function submit()
{
    var req = new XMLHttpRequest();
    req.onreadystatechange = function()
    {
        var response = JSON.parse(req.responseText);
        console.log(response)
        log_beta=""
        molecules=""
        output=response;
    }                   
    req.open('POST', '/ajax');
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    var postVars = 'num='+log_beta
    req.send(postVars);                       
}

function graph(){

}

function trend(){

}

function inputNum(el){
    console.log(log_beta)
    log_beta+=el.getAttribute("value")
    console.log(log_beta)
    document.getElementById("numWindow").setAttribute("value",log_beta)
}

function inputMol(el){
    molecules+=el.getAttribute("value")
}