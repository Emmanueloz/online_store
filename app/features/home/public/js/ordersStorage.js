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

const addOrders = (order) => {
    const list = getListOrders();
    list.push(order);
    setListOrders(list);
};

const removeOrders = (order) => {
    const list = getListOrders();
    const index = list.indexOf(order);
    list.splice(index, 1);
    setListOrders(list);
};

export { getListOrders, setListOrders, addOrders, removeOrders };
