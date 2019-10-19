//training set. [length, width, color(0=blue and 1=red)]
var dataB1 = [1, 1, 0];
var dataB2 = [2, 1,   0];
var dataB3 = [2, .5, 0];
var dataB4 = [3,   1, 0];

var dataR1 = [3, 1.5, 1];
var dataR2 = [3.5,   .5, 1];
var dataR3 = [4, 1.5, 1];
var dataR4 = [5.5,   1,   1];

//unknown type (data we want to find)
var dataU = [4.5,  1, "it should be 1"];

var all_points = [dataB1, dataB2, dataB3, dataB4, dataR1, dataR2, dataR3, dataR4];

function sigmoid(x) {
  return 1/(1+Math.exp(-x));
}

// training
function train() {
  let w1 = Math.random()*.2-.1;
  let w2 = Math.random()*.2-.1;
  let b = Math.random()*.2-.1;
  let learning_rate = 0.2;
  for (let iter = 0; iter < 50000; iter++) {
    // pick a random point
    let random_idx = Math.floor(Math.random() * all_points.length);
    let point = all_points[random_idx];
    let target = point[2]; // target stored in 3rd coord of points

    // feed forward
    let z = w1 * point[0] + w2 * point[1] + b;
    let pred = sigmoid(z);

    // now we compare the model prediction with the target
    let cost = (pred - target) ** 2;

    // now we find the slope of the cost w.r.t. each parameter (w1, w2, b)
    // bring derivative through square function
    let dcost_dpred = 2 * (pred - target);

    // bring derivative through sigmoid
    // derivative of sigmoid can be written using more sigmoids! d/dz sigmoid(z) = sigmoid(z)*(1-sigmoid(z))
    let dpred_dz = sigmoid(z) * (1-sigmoid(z));

    // I think you forgot these in your slope calculation? 
    let dz_dw1 = point[0];
    let dz_dw2 = point[1];
    let dz_db = 1;

    // now we can get the partial derivatives using the chain rule
    // notice the pattern? We're bringing how the cost changes through each function, first through the square, then through the sigmoid
    // and finally whatever is multiplying our parameter of interest becomes the last part
    let dcost_dw1 = dcost_dpred * dpred_dz * dz_dw1;
    let dcost_dw2 = dcost_dpred * dpred_dz * dz_dw2;
    let dcost_db =  dcost_dpred * dpred_dz * dz_db;

    // now we update our parameters!
    w1 -= learning_rate * dcost_dw1;
    w2 -= learning_rate * dcost_dw2;
    b -= learning_rate * dcost_db;
  }

  return {w1: w1, w2: w2, b: b};
}

let canvas = document.createElement("canvas");
canvas.width = 400;
canvas.height = 400;
document.body.appendChild(canvas);
let ctx = canvas.getContext("2d");
ctx.font = "Helvetica";

// map points from graph coordinates to the screen
let graph_size = {width: 7, height: 7};
function to_screen(x, y) {
  return {x: (x/graph_size.width)*canvas.width, y: -(y/graph_size.height)*canvas.height + canvas.height};
}

// map points from screen coordinates to the graph
function to_graph(x, y) {
  return {x: x/canvas.width*graph_size.width, y: graph_size.height - y/canvas.height*graph_size.height};
}

// draw the graph's grid lines
function draw_grid() {
  ctx.strokeStyle = "#AAAAAA";
  for (let j = 0; j <= graph_size.width; j++) {

    // x lines
    ctx.beginPath();
    let p = to_screen(j, 0);
    ctx.moveTo(p.x, p.y);
    p = to_screen(j, graph_size.height);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();

    // y lines
    ctx.beginPath();
    p = to_screen(0, j);
    ctx.moveTo(p.x, p.y);
    p = to_screen(graph_size.width, j);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
  }
}

// draw points
function draw_points() {
    // unknown
    let p = to_screen(dataU[0], dataU[1]);
    ctx.fillStyle = "#555555";
    ctx.fillText("???", p.x-8, p.y-5);
    ctx.fillRect(p.x-2, p.y-2, 4, 4);

    // draw points
    ctx.fillStyle = "#0000FF";
    for (let j = 0; j < all_points.length; j++) {
      let point = all_points[j];
      if (point[2] == 0) {
        ctx.fillStyle = "#0000FF";
      } else {
        ctx.fillStyle = "#FF0000";
      }
      p = to_screen(point[0], point[1]);
      ctx.fillRect(p.x-2, p.y-2, 4, 4);
    }
}

// visualize model output on grid of points
function visualize_params(params) {
  ctx.save();
  ctx.globalAlpha = 0.2;
  let step_size = .1;
  let box_size = canvas.width/(graph_size.width/step_size);

  for (let xx = 0; xx < graph_size.width; xx += step_size) {
    for (let yy = 0; yy < graph_size.height; yy += step_size) {
      let model_out = sigmoid( xx * params.w1 + yy * params.w2 + params.b );
      if (model_out < .5) {
        // blue
        ctx.fillStyle = "#0000FF";
      } else {
        // red
        ctx.fillStyle = "#FF0000";
      }
      let p = to_screen(xx, yy);
      ctx.fillRect(p.x, p.y, box_size, box_size);
    }
  }
  ctx.restore();
}

// find parameters
var params = train();

// visualize model output
ctx.clearRect(0, 0, canvas.width, canvas.height);
draw_grid();
draw_points();
visualize_params(params);

// say what the model would say for a given mouse position
window.onmousemove = function(evt) {
  ctx.clearRect(0, 0, 100, 50);

  let p = {x: 10, y: 20};

  let mouse = {x: evt.offsetX, y: evt.offsetY};
  let mouse_graph = to_graph(mouse.x, mouse.y);

  ctx.fillText("x: " + Math.round(mouse_graph.x*100)/100, p.x, p.y);
  ctx.fillText("y: " + Math.round(mouse_graph.y*100)/100, p.x, p.y + 10);
  // model output
  let model_out = sigmoid( mouse_graph.x * params.w1 + mouse_graph.y * params.w2 + params.b );
  model_out = Math.round(model_out*100)/100;
  ctx.fillText("prediction: " + model_out, p.x, p.y + 20);
}