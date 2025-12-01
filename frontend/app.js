async function getPrice() {
    const setId = document.getElementById("setId").value;
    const response = await fetch(`http://127.0.0.1:5000/api/price/${setId}`);
    const data = await response.json();

    document.getElementById("result").innerText =
        `Set ${data.set_id} price: ${data.price}`;
}
