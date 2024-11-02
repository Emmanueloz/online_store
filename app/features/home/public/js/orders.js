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

    const listIds = listOrders.map((o) => o.id);
    console.log(listIds);

    if (listIds.includes(parseInt(id_product))) {
        $btn.innerText = "Quitar del carrito";
        $btn.dataset.mode = "remove";
    } else {
        $btn.innerText = "Agregar al carrito";
        $btn.dataset.mode = "add";
    }

    $btn.addEventListener("click", selectProduct);
});

updateCountCarrito();
