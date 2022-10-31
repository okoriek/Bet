const selected = document.querySelector(".selected");
const code = document.querySelector(".code");
const optionsContainer = document.querySelector(".options-container");

const optionsList = document.querySelectorAll(".options");

selected.addEventListener("click", () => {
  optionsContainer.classList.toggle("active");
});

optionsList.forEach(o => {
  o.addEventListener("click", () => {
    selected.value = o.querySelector("option").innerHTML;
    code.value = o.querySelector("option").value;
    optionsContainer.classList.remove("active");
  });
});
