const orderKey = "ordersList";

const setListOrders = (list) => {
    localStorage.setItem(orderKey, JSON.stringify(list));
};

const getListOrders = () => {
    const listOrders = JSON.parse(localStorage.getItem(orderKey));
    if (listOrders === null) {
        setListOrders([]);
        return [];
    }

    return listOrders;
};

const addOrders = (order, amount = 1) => {
    const list = getListOrders();

    list.push({
        id: parseInt(order),
        amount: amount,
    });
    setListOrders(list);
};

const removeOrders = (order) => {
    order = parseInt(order);
    const list = getListOrders().filter((o) => o.id !== order);
    setListOrders(list);
};

export { getListOrders, setListOrders, addOrders, removeOrders };
