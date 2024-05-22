// const rangeInput = document.querySelectorAll(".range-input input"),
//   priceInput = document.querySelectorAll(".price-input input"),
//   range = document.querySelector(".slider .progress");
// let priceGap = 100;

// priceInput.forEach((input) => {
//   input.addEventListener("input", (e) => {
//     let minPrice = parseInt(priceInput[1].value),
//       maxPrice = parseInt(priceInput[0].value);

//     if (maxPrice - minPrice >= priceGap && maxPrice <= rangeInput[1].max) {
//       if (e.target.className === "input-min") {
//         rangeInput[0].value = minPrice;
//         range.style.left = (minPrice / rangeInput[0].max) * 100 + "%";
//       } else {
//         rangeInput[1].value = maxPrice;
//         range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
//       }
//     }
//   });
// });

// rangeInput.forEach((input) => {
//   input.addEventListener("input", (e) => {
//     let minVal = parseInt(rangeInput[0].value),
//       maxVal = parseInt(rangeInput[1].value);

//     if (maxVal - minVal < priceGap) {
//       if (e.target.className === "range-min") {
//         rangeInput[0].value = maxVal - priceGap;
//       } else {
//         rangeInput[1].value = minVal + priceGap;
//       }
//     } else {
//       priceInput[1].value = minVal;
//       priceInput[0].value = maxVal;
//       range.style.right = (minVal / rangeInput[0].max) * 100 + "%";
//       range.style.left = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
//     }
//   });
// });
const rangeInput = document.querySelectorAll(".range-input input"),
  priceInput = document.querySelectorAll(".price-input input"),
  range = document.querySelector(".slider .progress");
let priceGap = 1000;

rangeInput.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minVal = parseInt(rangeInput[0].value),
      maxVal = parseInt(rangeInput[1].value);

    if (maxVal - minVal < priceGap) {
      if (e.target.className === "range-min") {
        rangeInput[1].value = maxVal + priceGap;
      } else {
        rangeInput[0].value = minVal - priceGap;
      }
    } else {
      priceInput[1].value = minVal;
      priceInput[0].value = maxVal;
    //   range.style.left = 100 - (minVal / rangeInput[0].max) * 100 + "%";
    //   range.style.right = (maxVal / rangeInput[1].max) * 100 + "%";
    }
  });
});