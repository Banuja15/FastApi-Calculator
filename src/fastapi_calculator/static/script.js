const display = document.getElementById("display");

const numberButtons =
    document.querySelectorAll(".number");

const operatorButtons =
    document.querySelectorAll(".operator");

const decimalButton =
    document.querySelector(".decimal");

const clearButton =
    document.querySelector(".clear");

const backspaceButton =
    document.querySelector(".backspace");

const equalsButton =
    document.querySelector(".equals");


let expression = "";


// -------------------------
// Number buttons
// -------------------------

numberButtons.forEach(button => {

    button.addEventListener("click", () => {

        expression += button.textContent;

        display.value = expression;

    });

});


// -------------------------
// Operators
// -------------------------

operatorButtons.forEach(button => {

    button.addEventListener("click", () => {

        expression += button.dataset.operation;

        display.value = expression;

    });

});


// -------------------------
// Decimal
// -------------------------

decimalButton.addEventListener("click", () => {

    expression += ".";

    display.value = expression;

});


// -------------------------
// Clear
// -------------------------

clearButton.addEventListener("click", () => {

    expression = "";

    display.value = "";

});


// -------------------------
// Equals
// -------------------------

equalsButton.addEventListener("click", () => {

    if (expression === "") {
        return;
    }


    fetch("/calculate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            expression: expression
        })

    })

    .then(response => {

        if (!response.ok) {
            return response.json().then(error => {
                throw new Error(error.detail);
            });
        }

        return response.json();

    })

    .then(data => {

        display.value = data.result;

        expression = String(data.result);

    })

    .catch(error => {

        display.value = error.message;

        expression = "";

    });

});