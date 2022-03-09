let log_beta=""
let molecules=""
let out=[]
const concen=0
const mols = 1
const ph = 2
const xmin = 3 
const xmax = 4
const ymin = 5
const ymax = 6
const xscale = 7
const yscale = 8
const xstep = 9
const ystep = 10 
const points = 11 
const minmax = 12
function submit()
{
    var req = new XMLHttpRequest();
    req.onreadystatechange = function()
    {
        var response = JSON.parse(req.responseText);
        console.log(response)
        log_beta=""
        molecules=""
        out=response;
        graph();
        clear();
    }               
    req.open('POST', '/ajax');
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    var postVars = 'num='+log_beta+'&name='+molecules
    req.send(postVars);                       
}

function graph(){
    let id=0;
    let output= out["out"]
    for(let i=0;i<5;i++){
        for(let j=0;j<1001;j++)
        {
            id+=1
            var temp=document.getElementById("ball"+id)
            var xco=(parseFloat(output[ph][j])-parseFloat(output[xmin]))*parseFloat(output[xscale])
            var yco=(parseFloat(output[concen][i][j])*parseFloat(output[yscale]))
            var zco=(i+1)*(-5)
            temp.setAttribute("position",xco+" "+yco+" "+zco)
            console.log(xco+" "+yco+" "+zco)
        }
        console.log(i+"done")
    }
}

function trend(){

}

function inputNum(el){
    log_beta+=el.getAttribute("value")
    document.getElementById("numWindow").setAttribute("value",log_beta)
}

function inputMol(el){
    molecules+=el.getAttribute("value")
    document.getElementById("molWindow").setAttribute("value",log_beta)
}

function clear()
{
    log_beta=""
    molecules=""
    document.getElementById("molWindow").setAttribute("value",molecules)
    document.getElementById("numWindow").setAttribute("value",log_beta)
}