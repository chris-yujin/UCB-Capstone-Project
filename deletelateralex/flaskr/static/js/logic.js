function testFunction() {
    console.log("Page loaded!")
    window.location.assign("/mltrain");
}

function writeTable(){
    d3.json("/gettable").then(function(data){
        let content = data.data;
        let selector = d3.select("tbody");
        content.forEach((element)=>{
            selector.append("tr").html(
                `
                <td>${Math.round(element[0] * 100) / 100}</td>
                <td>${Math.round(element[1] * 100) / 100}</td>
                <td>${Math.round(element[2] * 100) / 100}</td>
                <td>${Math.round(element[3] * 100) / 100}</td>
                `
            )
        })
    })
}

d3.selectAll("input").on("change", function(event){
    d3.select("#"+event.target.id+"l").text(event.target.name+": "+event.target.value)
    updateValue()
})

function updateValue(){
    a = d3.select("#customRange1").property("value")
    b = d3.select("#customRange2").property("value")
    c = d3.select("#customRange3").property("value")
    d3.json("/predict/"+a+"/"+b+"/"+c).then(function(data){
        d3.select("#dynamic").text(data["cluster"])
        d3.select("#dynamic2").text(data["sum"])
    })
}