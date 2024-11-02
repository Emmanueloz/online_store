import { addOrders, getListOrders, removeOrders } from "./ordersStorage.js";

const $ = (s) => document.querySelector(s);
const $$ = (s) => document.querySelectorAll(s);

$$(".btn-remove-order").forEach(($btn) => {
    $btn.addEventListener("click", (event) => {
        const { id_product } = $btn.dataset;
        removeOrders(id_product);
        const listOrders = getListOrders();
        console.log(`${window.location.pathname}?list=${listOrders}`);
        window.location.href = `${window.location.pathname}?list=${listOrders}`;
    });
});
