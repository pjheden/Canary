function parseDate(date) {
  const d = new Date(date);
  return d;
}

const TRESHOLD = 900;

let margin = {top: 50, right: 50, bottom: 50, left: 50}
  , width = window.innerWidth - margin.left - margin.right // Use the window's width 
  , height = window.innerHeight - margin.top - margin.bottom; // Use the window's height

// let xScale = d3.scaleLinear().range([0, width]);
let xScale = d3.scaleTime().range([0, width]);
let yScale = d3.scaleLinear().range([height, 0]);
let line = d3.line()
    .x(function(d, i) { return xScale(parseDate(d["datetime"])); }) // set the x values for the line generator
    .y(function(d) { return yScale(d["co2"]) }) // set the y values for the line generator 
    .curve(d3.curveMonotoneX) // apply smoothing to the line

d3.csv('./data.csv')
  .then(function(data) {
      // Set the timescale to the latest week
      const latestDate = parseDate(data[data.length-1]["datetime"]);
      const oneWeekAgo = parseDate(latestDate);
      // oneWeekAgo.setDate(oneWeekAgo.getDate() - 1);
      oneWeekAgo.setHours(oneWeekAgo.getHours() - 3);
      xScale.domain([oneWeekAgo, latestDate]);

        // Set y scale from 0 to max
      yScale.domain([0, d3.max(data, (d) => parseInt(d["co2"]))]);

      // Create SVG
      const svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // 3. Call the x axis in a group tag
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

    // 4. Call the y axis in a group tag
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

    // 9. Append the path, bind the data, and call the line generator 
    svg.append("path")
        .datum(data) // 10. Binds data to the line 
        .attr("class", "line") // Assign a class for styling 
        .attr("d", line); // 11. Calls the line generator 

    // 12. Appends a circle for each datapoint 
    svg.selectAll(".dot")
        .data(data)
      .enter().append("circle") // Uses the enter().append() method
        .attr("class", "dot") // Assign a class for styling
        .attr("cx", function(d, i) { return xScale(parseDate(d["datetime"])); })
        .attr("cy", function(d) { return yScale(d["co2"]) })
        .attr("r", 5)
        .on("mouseover", (d) => console.log(d));

    // Append treshold line
    svg.append("line")
      .attr("x1", xScale.range()[0])
      .attr("y1", yScale(TRESHOLD))
      .attr("x2", xScale.range()[1])
      .attr("y2", yScale(TRESHOLD))
      .attr("stroke-width", 2)
      .attr("stroke", "blue");
      })

  .catch(function(error){
     // handle error   
  })

