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
    if(log_beta.length==0&&molecules.length==0)
    {
        return false;
    }
    if(!molecules.includes(',')&&molecules.length>0){
        return false;
    }
    var req = new XMLHttpRequest();
    req.onreadystatechange = function()
    {
        var response = JSON.parse(req.responseText);
        console.log(response)
        log_beta=""
        molecules=""
        out=response["out"];
        graph();
        trend();
        clear();
    }               
    req.open('POST', '/ajax');
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    var postVars = 'num='+log_beta+'&name='+molecules
    req.send(postVars);                       
}

function graph(){
    let id=0;
    for(let i=0;i<5;i++){
        var tempLabel=document.getElementById(i+"label");
        tempLabel.setAttribute("value", out[mols][i])
        for(let j=0;j<1002;j++)
        {
            id+=1
            var temp=document.getElementById("ball"+id)
            var xco=(parseFloat(out[ph][j])-parseFloat(out[xmin]))*parseFloat(out[xscale])
            var yco=(parseFloat(out[concen][i][j])*parseFloat(out[yscale]))
            var zco=(i+1)*(-5)
            temp.setAttribute("position",xco+" "+yco+" "+zco)
            var tempData = document.getElementById("data"+id)
            tempData.setAttribute("value","m: "+out[mols][i]+" ph: "+out[ph][j]+" c: "+out[concen][i][j])
        }
    }
}

function trend(){
    console.log(out[points])
    for(let i=0;i<out[points].length;i++)
    {
        var temp = document.getElementById(i+"trend")
        temp.setAttribute("points",out[points][i])
        var button = document.getElementById("button"+i)
        var button2 = document.getElementById("button2"+i)
        button.setAttribute("value","show trend \nfor "+out[mols][i])
        button2.setAttribute("value","show datas \nfor "+out[mols][i])
    }
}

function inputNum(el){
    log_beta+=el.getAttribute("value")
    document.getElementById("numWindow").setAttribute("value",log_beta)
}

function inputMol(el){
    molecules+=el.getAttribute("value")
    document.getElementById("molWindow").setAttribute("value",molecules)
}

function delNum(){
    log_beta=log_beta.substring(0,log_beta.length-1)
    document.getElementById("numWindow").setAttribute("value",log_beta)
}

function delMol(){
    molecules=molecules.substring(0,molecules.length-1)
    document.getElementById("molWindow").setAttribute("value",molecules)
}

function clear()
{
    log_beta=""
    molecules=""
    document.getElementById("molWindow").setAttribute("value",molecules)
    document.getElementById("numWindow").setAttribute("value",log_beta)
}
