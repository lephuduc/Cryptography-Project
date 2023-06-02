let products = [];

fetch("/json/products.json")
    .then(response => response.json())
    .then(data => {
        products = JSON.parse(data);
        loadProducts(products);
    })


const containerProducts = document.querySelector("#container-products");
const buttonCategory = document.querySelectorAll(".button-category");
const mainTitle = document.querySelector("#main-title");
let addButton = document.querySelectorAll(".product-add");
const quantity = document.querySelector("#quantity");


buttonCategory.forEach(boton => boton.addEventListener("click", () => {
    aside.classList.remove("aside-visible");
}))


function loadProducts(chooseProduct) {

    containerProducts.innerHTML = "";

    chooseProduct.forEach(product => {

        const div = document.createElement("div");
        div.classList.add("product");
        div.innerHTML = `
            <img class="product-image" src="${product.image}" alt="${product.title}">
            <div class="product-details">
                <h3 class="product-title">${product.title}</h3>
                <p class="product-price">$${product.price}</p>
                <button class="product-add" id="${product.id}">Buy now</button>
            </div>
        `;

        containerProducts.append(div);
    })

    addedButtonProduct();
}


buttonCategory.forEach(boton => {
    boton.addEventListener("click", (e) => {

        buttonCategory.forEach(boton => boton.classList.remove("active"));
        e.currentTarget.classList.add("active");

        if (e.currentTarget.id != "all") {
            const productCategory = products.find(product => product.category.id === e.currentTarget.id);
            mainTitle.innerText = productCategory.category.name;
            const productButton = products.filter(product => product.category.id === e.currentTarget.id);
            loadProducts(productButton);
        } else {
            mainTitle.innerText = "All Products";
            loadProducts(products);
        }

    })
});

function addedButtonProduct() {
    addButton = document.querySelectorAll(".product-add");

    addButton.forEach(boton => {
        boton.addEventListener("click", addedProduct);
    });
}

let productInCart;

let productInCartLS = localStorage.getItem("product-in-cart");

if (productInCartLS) {
    productInCart = JSON.parse(productInCartLS);
    updateQuantity();
} else {
    productInCart = [];
}

function addedProduct(e) {

    Toastify({
        text: "Product Added",
        duration: 3000,
        close: true,
        gravity: "top",
        position: "right", 
        stopOnFocus: true, 
        style: {
          background: "linear-gradient(to right, #e96d08, #000333)",
          borderRadius: "2rem",
          textTransform: "uppercase",
          fontSize: ".75rem"
        },
        offset: {
            x: '1.5rem', 
            y: '1.5rem' 
          },
        onClick: function(){} // Callback after click
      }).showToast();

    const idButton = e.currentTarget.id;
    const productAdd = products.find(product => product.id === idButton);

    if(productInCart.some(product => product.id === idButton)) {
        const index = productInCart.findIndex(product => product.id === idButton);
        productInCart[index].cantidad++;
    } else {
        productAdd.cantidad = 1;
        productInCart.push(productAdd);
    }

    updateQuantity();

    localStorage.setItem("product-in-cart", JSON.stringify(productInCart));
}

function updateQuantity() {
    let newQuantity = productInCart.reduce((acc, product) => acc + product.cantidad, 0);
    quantity.innerText = newQuantity;
}