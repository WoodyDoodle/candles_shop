fetch('../api/cart', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}',
    },
})
.then(response => response.json())
.then(data => {
    document.querySelectorAll('.buy-button').forEach(button => {
        const productId = button.dataset.productId;
        let product = data.data.find(item => item.product == productId);
        if (product) {
            convertElementToCounter(button, productId, product.count);
        }
    });
});


document.addEventListener('click', function(event) {
    if (event.target.classList.contains('buy-button')) {
        event.preventDefault();
        const productId = event.target.dataset.productId;
        fetch('../api/add-to-cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({ product_id: productId }),
        })
        .then(response => response.json())
        .then(data => {
            // document.querySelector('.count_product_cart').textContent = data.cart_count;
            if (data.success) {
                convertElementToCounter(event.target, productId, 1);
            } else {
                alert(data.error);
            }
        });
    };
});