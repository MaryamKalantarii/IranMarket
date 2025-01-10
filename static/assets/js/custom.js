function formatPriceInToman(element) {
    let rawPrice = parseFloat(element.innerText);
    let formatter = new Intl.NumberFormat('fa-IR');
    let formattedPrice = formatter.format(rawPrice);
    element.innerText = `${formattedPrice} تومان`;
}

document.addEventListener("DOMContentLoaded", function() {
    let priceElements = document.querySelectorAll('.formatted-price');
    priceElements.forEach(element => formatPriceInToman(element));
});



document.getElementById('openModal').addEventListener('click', function () {
    document.getElementById('reviewModal').classList.remove('hidden');
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('reviewModal').classList.add('hidden');
});

