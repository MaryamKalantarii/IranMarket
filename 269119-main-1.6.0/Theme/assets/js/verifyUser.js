
 const button = document.querySelector("button");
  let arrayInputs = [] ;
  arrayInputs = document.querySelectorAll(".inputVerify");
  arrayInputs.forEach((input, index1) => {
  input.addEventListener("keyup", (e) => {
    const currentInput = input,
      nextInput = input.nextElementSibling,
      prevInput = input.previousElementSibling;
    if (currentInput.value.length > 1) {
      currentInput.value = "";
      return;
    }
    if (
      nextInput &&
      nextInput.hasAttribute("disabled") &&
      currentInput.value !== ""
    ) {
      nextInput.removeAttribute("disabled");
      nextInput.focus();
    }
    if (e.key === "Backspace") {
      arrayInputs.forEach((input, index2) => {
        if (index1 <= index2 && prevInput) {
          input.setAttribute("disabled", true);
          input.value = "";
          prevInput.focus();
        }
      });
    }
    if (!arrayInputs[3].disabled && arrayInputs[3].value !== "") {
      button.classList.add("active");
      return;
    }
    button.classList.remove("active");
  });
});
window.addEventListener("load", () => arrayInputs[0].focus());