// script.js
document.addEventListener('DOMContentLoaded', () => {
    const dialNumbers = document.querySelectorAll('.dial-number');
    const display = document.getElementById('display');
    let dialedNumber = '';

    dialNumbers.forEach(number => {
        number.addEventListener('click', () => {
            dialedNumber += number.textContent;
            display.textContent = `Dialed Number: ${dialedNumber}`;
        });
    });
});
