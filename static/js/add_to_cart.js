
document.querySelectorAll('.buy-button').forEach(button => {
    button.addEventListener('click', event => {
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
            document.querySelector('.count_product_cart').textContent = data.cart_count;
        });
    });
});