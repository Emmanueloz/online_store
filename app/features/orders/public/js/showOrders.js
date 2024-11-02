import {
    getListOrders,
    removeOrders,
    decrementAmount,
    incrementAmount,
    removeAllOrders,
} from "../../../../static/js/ordersStorage.js";

const $ = (s) => document.querySelector(s);
const $$ = (s) => document.querySelectorAll(s);

const updatePage = () => {
    const listOrders = getListOrders();
    const listIds = listOrders.map((o) => o.id);
    const listAmount = listOrders.map((o) => o.amount);
    window.location.href = `${window.location.pathname}?list=${listIds}&amount=${listAmount}`;
};

$$(".btn-remove-order").forEach(($btn) => {
    $btn.addEventListener("click", (event) => {
        const { id_product } = $btn.dataset;
        removeOrders(id_product);
        updatePage();
    });
});

$$(".btn-increment-amount").forEach(($btn) => {
    $btn.addEventListener("click", (event) => {
        const { id_product } = $btn.dataset;
        incrementAmount(id_product);
        updatePage();
    });
});

$$(".btn-decrement-amount").forEach(($btn) => {
    $btn.addEventListener("click", (event) => {
        const { id_product } = $btn.dataset;
        decrementAmount(id_product);
        updatePage();
    });
});

$(`#pay-link`).addEventListener("click", (event) => {
    event.preventDefault();

    removeAllOrders();
    window.location.href = event.target.href;
});
