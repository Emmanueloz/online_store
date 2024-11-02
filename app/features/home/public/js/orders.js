import { addOrders, getListOrders, removeOrders } from "./ordersStorage.js";

const $ = (s) => document.querySelector(s);
const $$ = (s) => document.querySelectorAll(s);

const $carrito = $("#carrito-count");
const listOrders = getListOrders();

const updateCountCarrito = () => {
    $carrito.innerText = getListOrders().length;
};

/**
 * @param {Event} event
 */
const selectProduct = (event) => {
    const $btn = event.target;
    const { mode, id_product } = $btn.dataset;

    if (mode === "add") {
        addOrders(id_product);
        $btn.innerText = "Quitar del carrito";
        $btn.dataset.mode = "remove";
    } else if (mode === "remove") {
        removeOrders(id_product);
        $btn.innerText = "Agregar al carrito";
        $btn.dataset.mode = "add";
    }

    updateCountCarrito();
};

$$(".btn-select-product").forEach(($btn) => {
    const { id_product } = $btn.dataset;

    if (listOrders.includes(id_product)) {
        $btn.innerText = "Quitar del carrito";
        $btn.dataset.mode = "remove";
    } else {
        $btn.innerText = "Agregar al carrito";
        $btn.dataset.mode = "add";
    }

    $btn.addEventListener("click", selectProduct);
});

updateCountCarrito();
