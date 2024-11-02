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

const removeAllOrders = () => {
    setListOrders([]);
};

const incrementAmount = (order) => {
    order = parseInt(order);
    const list = getListOrders();
    const orderIndex = list.findIndex((o) => o.id === order);

    if (orderIndex === -1) {
        return;
    }

    list[orderIndex].amount++;
    setListOrders(list);
};

const decrementAmount = (order) => {
    order = parseInt(order);
    const list = getListOrders();
    const orderIndex = list.findIndex((o) => o.id === order);

    if ((orderIndex === -1, list[orderIndex].amount === 1)) {
        return;
    }

    list[orderIndex].amount--;
    setListOrders(list);
};

export {
    getListOrders,
    setListOrders,
    addOrders,
    removeOrders,
    incrementAmount,
    decrementAmount,
    removeAllOrders,
};
