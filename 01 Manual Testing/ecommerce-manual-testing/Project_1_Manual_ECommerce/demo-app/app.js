/**
 * app.js - Demo E-commerce Application logic matching Test Scenarios
 */

// Handle Login (TC01, TC02, TC03)
function login() {
    const user = document.getElementById('username').value.trim();
    const pass = document.getElementById('password').value.trim();
    const err = document.getElementById('error');
    
    // TC03: Login with empty fields
    if (!user || !pass) {
        err.innerText = "Please fill in all fields (User ID & Password)";
        return;
    }
    
    // TC01: Login with valid credentials
    if (user === 'admin' && pass === '1234') {
        err.innerText = "";
        window.location.href = 'dashboard.html';
    } 
    // TC02: Login with invalid credentials
    else {
        err.innerText = "Invalid credentials. Try admin / 1234";
    }
}

// Handle Add to Cart
function addToCart(id, name, price) {
    let cart = JSON.parse(localStorage.getItem('cart') || '[]');
    cart.push({ id, name, price });
    localStorage.setItem('cart', JSON.stringify(cart));
    alert(name + " added to cart successfully!");
}

// Load Cart Page
function loadCart() {
    let cart = JSON.parse(localStorage.getItem('cart') || '[]');
    let ul = document.getElementById('cart-items');
    let totalSpan = document.getElementById('total-price');
    let total = 0;
    
    ul.innerHTML = '';
    
    if (cart.length === 0) {
        ul.innerHTML = '<li>Empty Cart</li>';
    } else {
        cart.forEach((item, index) => {
            let li = document.createElement('li');
            li.innerHTML = `<span>${item.name}</span> <span>$${item.price}</span>`;
            ul.appendChild(li);
            total += item.price;
        });
    }
    
    totalSpan.innerText = total;
}

// Checkout Navigation
// BUG-001 is kept intentionally alive: No logic prevents empty checkout!
function checkout() {
    window.location.href = 'payment.html';
}