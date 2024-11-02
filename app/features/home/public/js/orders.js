import {
    addOrders,
    getListOrders,
    removeOrders,
} from "../../../../static/js/ordersStorage.js";

const $ = (s) => document.querySelector(s);
const $$ = (s) => document.querySelectorAll(s);

const $carrito = $("#carrito-count");
const $carritoLink = $("#carrito-link");
const listOrders = getListOrders();

const updateCountCarrito = () => {
    const newListOrders = getListOrders();
    if ($carritoLink) {
        const { default_href } = $carritoLink.dataset;

        const listIds = newListOrders.map((o) => o.id);
        const listAmount = newListOrders.map((o) => o.amount);
        console.log(listAmount);

        $carritoLink.href = `${default_href}?list=${listIds}&amount=${listAmount}`;
    }
    $carrito.innerText = newListOrders.length;
};

/**
 *
 * @param {HTMLButtonElement} $btn
 */
const setBtnAdd = ($btn) => {
    $btn.innerText = "Agregar al carrito";
    $btn.dataset.mode = "add";
    $btn.classList.add("btn-dark");
    $btn.classList.remove("btn-outline-danger");
};

/**
 *
 * @param {HTMLButtonElement} $btn
 */
const setBtnRemove = ($btn) => {
    $btn.innerText = "Quitar del carrito";
    $btn.dataset.mode = "remove";
    $btn.classList.add("btn-outline-danger");
    $btn.classList.remove("btn-dark");
};

/**
 * @param {Event} event
 */
const selectProduct = (event) => {
    const $btn = event.target;
    const { mode, id_product } = $btn.dataset;

    if (mode === "add") {
        addOrders(id_product);
        setBtnRemove($btn);
    } else if (mode === "remove") {
        removeOrders(id_product);
        setBtnAdd($btn);
    }

    updateCountCarrito();
};

$$(".btn-select-product").forEach(($btn) => {
    const { id_product } = $btn.dataset;

    const listIds = listOrders.map((o) => o.id);
    console.log(listIds);

    if (listIds.includes(parseInt(id_product))) {
        setBtnRemove($btn);
    } else {
        setBtnAdd($btn);
    }

    $btn.addEventListener("click", selectProduct);
});

updateCountCarrito();
