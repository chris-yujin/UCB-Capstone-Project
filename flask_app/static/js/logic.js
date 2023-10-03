function testFunction() {
    console.log("Page loaded!")
    window.location.assign("/dataload");
}

function writeTable(){
    d3.json("/gettable").then(function(data){
        let content = data.data;
        let selector = d3.select("tbody");
        content.forEach((element)=>{
            selector.append("tr").html(
                `
                <td>${element[0]}</td>
                <td>${element[1]}</td>
                <td>${Math.round(element[2] * 100) / 100}</td>
                <td>${Math.round(element[3] * 100) / 100}</td>
                <td>${Math.round(element[4] * 100) / 100}</td>
                <td>${Math.round(element[5] * 100) / 100}</td>
                <td>${Math.round(element[6] * 100) / 100}</td>
                <td>${Math.round(element[7] * 100) / 100}</td>
                <td>${Math.round(element[8] * 100) / 100}</td>
                <td>${Math.round(element[9] * 100) / 100}</td>
                <td>${Math.round(element[10] * 100) / 100}</td>
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
    d = d3.select("#customRange4").property("value")
    e = d3.select("#customRange5").property("value")
    f = d3.select("#customRange6").property("value")
    g = d3.select("#customRange7").property("value")
    h = d3.select("#customRange8").property("value")
    i = d3.select("#customRange9").property("value")
    d3.json("/predict/"+a+"/"+b+"/"+c+"/"+d+"/"+e+"/"+f+"/"+g+"/"+h+"/"+i).then(function(data){
        console.log(data)
        d3.select("#dynamic_cancer").text(data["cancer_prevalance"])
        d3.select("#dynamic_diabetes").text(data["diabetes_prevalance"])
        d3.select("#dynamic_obesity").text(data["obesity_prevalance"])
        d3.select("#dynamic2").text(data["sum"])
    })
}

// Capture user input (zipcode) and trigger the update
d3.select("#text-input").on("change", function () {
    const zipcode = d3.select(this).property("value");
    
    
    // Send an AJAX request to the Flask route
    d3.json(`/update_data/${zipcode}`).then(function (data) {
        if (data.error) {
            // Handle the case where no data is found for the zipcode
            console.error(data.error);
            // Display a message to the user
            d3.select("#user-input-display").html("<strong>Zipcode Not Found</strong>");
            // Update sliders and table with default values or clear them
        } else {
            
            // Display the user input
            d3.select("#user-input-display").text(zipcode);
            // Update the table with the fetched data
            d3.select("tbody").html("");
            console.log(data);
            
            let selector = d3.select("tbody");
            
            selector.append("tr").html(
                `
                <td>${data["zipcode"]}</td>
                <td>${data["state"]}</td>
                <td>${Math.round(data["income_per_individual"] *100) / 100}</td>
                <td>${Math.round(data["lacking_health_insurance"] * 100) / 100}</td>
                <td>${Math.round(data["binge_drinking"] * 100) / 100}</td>
                <td>${Math.round(data["high_blood_pressure"] * 100) / 100}</td>
                <td>${Math.round(data["routine_check_ups"] * 100) / 100}</td>
                <td>${Math.round(data["currently_smoking"] * 100) / 100}</td>
                <td>${Math.round(data["depressed"] * 100) / 100}</td>
                <td>${Math.round(data["no_leisure_physical_activity"] * 100) / 100}</td>
                <td>${Math.round(data["less_7_hours_sleep"] * 100) / 100}</td>
                
                `
            )
            
            // Update the sliders with the fetched values
            d3.select("#customRange1").property("value", data["income_per_individual"]);
            d3.select("#customRange2").property("value", data["lacking_health_insurance"]);
            d3.select("#customRange3").property("value", data["binge_drinking"]);
            d3.select("#customRange4").property("value", data["high_blood_pressure"]);
            d3.select("#customRange5").property("value", data["routine_check_ups"]);
            d3.select("#customRange6").property("value", data["currently_smoking"]);
            d3.select("#customRange7").property("value", data["depressed"]);
            d3.select("#customRange8").property("value", data["no_leisure_physical_activity"]);
            d3.select("#customRange9").property("value", data["less_7_hours_sleep"]);
            
           

            // d3.selectAll("input"){
            //     let a = data["income_per_individual"];
            //     console.log(a);
            //     // d3.select("#"+event.target.id+"l").text(event.target.name+": "+event.target.value)
            //     d3.select(event+"#customRange1l").text(event+"Income Per Individual (Thousands):"+a);
            //     d3.select("#customRange2l").property("value", data["lacking_health_insurance"]);
            //     d3.select("#customRange3l").property("value", data["binge_drinking"]);
            //     d3.select("#customRange4l").property("value", data["high_blood_pressure"]);
            //     d3.select("#customRange5l").property("value", data["routine_check_ups"]);
            //     d3.select("#customRange6l").property("value", data["currently_smoking"]);
            //     d3.select("#customRange7l").property("value", data["depressed"]);
            //     d3.select("#customRange8l").property("value", data["no_leisure_physical_activity"]);
            //     d3.select("#customRange9l").property("value", data["less_7_hours_sleep"]);
            // }
            updateValue()
          
            
            
        }
    });
});