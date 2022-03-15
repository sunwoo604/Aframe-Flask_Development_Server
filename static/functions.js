
let beta1=""
let beta2=""
let c01=""
let c02=""
let cadded0=""
let cadded1=""
let molecules=""
let windows=0
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
    if(beta1.length==0&&molecules.length==0&&beta2.length==0&&c01.length==0&&c02.length==0&&cadded0.length==0&&cadded1.length==0)
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
    var postVars = 'name='+molecules+'&beta1='+beta1+'&beta2='+beta2+'&c01='+c01+'&c02='+c02+'&cadded0='+cadded0+'&cadded1='+cadded1;
    req.send(postVars);                       
}

function wind(num){
    windows=num
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
    if(windows==0){
        beta1+=el.getAttribute("value")
        console.log(beta1)
        document.getElementById("beta1").setAttribute("value",beta1)
        console.log(document.getElementById("beta1").getAttribute("value"))
    }
    else if(windows==1){
        beta2+=el.getAttribute("value")
        document.getElementById("beta2").setAttribute("value",beta2)
    }
    else if(windows==2){
        c01+=el.getAttribute("value")
        document.getElementById("c01").setAttribute("value",c01)
    }
    else if(windows==3){
        c02+=el.getAttribute("value")
        document.getElementById("c02").setAttribute("value",c02)
    }
    else if(windows==4){
        cadded0+=el.getAttribute("value")
        document.getElementById("cadded0").setAttribute("value",cadded0)
    }
    else if(windows==5){
        cadded1+=el.getAttribute("value")
        document.getElementById("cadded1").setAttribute("value",cadded1)
    }
}

function inputMol(el){
    molecules+=el.getAttribute("value")
    document.getElementById("molWindow").setAttribute("value",molecules)
}

function delNum(){
    if(windows==0){
        beta1=beta1.substring(0,beta1.length-1)
        document.getElementById("beta1").setAttribute("value",beta1)
    }
    else if(windows==1){
        beta2=beta2.substring(0,beta2.length-1)
        document.getElementById("beta2").setAttribute("value",beta2)
    }
    else if(windows==2){
        c01=c01.substring(0,c01.length-1)
        document.getElementById("c01").setAttribute("value",c01)
    }
    else if(windows==3){
        c02=c02.substring(0,c02.length-1)
        document.getElementById("c02").setAttribute("value",c02)
    }
    else if(windows==4){
        cadded=cadded0.substring(0,cadded0.length-1)
        document.getElementById("cadded0").setAttribute("value",cadded0)
    }
    else if(windows==5){
        cadded1=cadded1.substring(0,cadded1.length-1)
        document.getElementById("cadded1").setAttribute("value",cadded1)
    }
}

function delMol(){
    molecules=molecules.substring(0,molecules.length-1)
    document.getElementById("molWindow").setAttribute("value",molecules)
}

function clear()
{
    beta1=""
    beta2=""
    c01=""
    c02=""
    cadded0=""
    cadded1=""
    molecules=""
    document.getElementById("molWindow").setAttribute("value",molecules)
    document.getElementById("beta1").setAttribute("value",beta1)
    document.getElementById("beta2").setAttribute("value",beta2)
    document.getElementById("c01").setAttribute("value",c01)
    document.getElementById("c02").setAttribute("value",c02)
    document.getElementById("cadded0").setAttribute("value",cadded0)
    document.getElementById("cadded1").setAttribute("value",cadded1)
}
