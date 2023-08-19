
function ColorFlipper() {
  let colors = ["purple", "green", "blue", "yellow", "grey", "black", "white", "orange", "pink", "violet"];
  let box = document.createElement("div");
  box.style.backgroundColor = "green";
  box.style.padding = "60px";
  box.style.margin = "5px";
  box.style.border = "2px solid black";
  document.body.appendChild(box);

  let button = document.createElement("button");
  button.innerHTML = "CLICK ME";
  document.body.appendChild(button);

  button.addEventListener("click", function() {
    let randomChoice = Math.floor(Math.random() * colors.length);
    box.style.backgroundColor = colors[randomChoice];
  });
}

ColorFlipper();

