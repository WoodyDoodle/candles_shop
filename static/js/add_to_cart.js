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
        product = data.data.find(item => item.product == productId);
        if (product) {
            button.outerHTML = `
                <div class="counter">
                    <button class="minus" data-product-id=${productId}>-</button>
                    <span class="count">${product.count}</span>
                    <button class="plus" data-product-id=${productId}>+</button>
                </div>
            `;
        }
    });
});



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



document.addEventListener('DOMContentLoaded', function() {
document.querySelectorAll('.minus, .plus').forEach(button => {
    button.addEventListener('click', event => {
        console.log('Button clicked');
        const countElement = event.target.parentElement.querySelector('.count');
        let count = parseInt(countElement.textContent);

        if (event.target.classList.contains('minus')) {
            count--;
        } else {
            count++;
        }

        countElement.textContent = count;

        const dataProductId = event.target.getAttribute('data-product-id');

        // Показываем колесико загрузки
        // ...

        // Отправляем POST-запрос
        fetch('../api/change-count-product', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({
                count: count, 
                product_id: dataProductId 
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response:', 'nothing');
            // Скрываем колесико загрузки
            // ...
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
})});