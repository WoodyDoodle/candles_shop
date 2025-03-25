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
            convertButtonToCounter(button, productId, product.count);
        }
    });
});


document.addEventListener('click', function(event) {
    if (event.target.classList.contains('minus')) {
        const counter = event.target.closest('.counter');
        const count = parseInt(counter.querySelector('.count').textContent) - 1;
        counter.querySelector('.count').textContent = count;
        // ПОдождать 2 секунды перед отправкой запроса
        setTimeout(() => {
            newCount = parseInt(counter.querySelector('.count').textContent);
            if (count === newCount) {
                alert('Обновление');
                updateProductCount(counter.dataset.productId, count);
            } else {
                alert('Обновление не прошло');
            }
        }, 2000);

        if (count === 0) {
            convertCounterToButton(counter, counter.dataset.productId);
        }
    };
    if (event.target.classList.contains('plus')) {
        const counter = event.target.closest('.counter');
        const count = parseInt(counter.querySelector('.count').textContent) + 1;
        counter.querySelector('.count').textContent = count;
        setTimeout(() => {
            newCount = parseInt(counter.querySelector('.count').textContent);
            if (count === newCount) {
                alert('Обновление');
                updateProductCount(counter.dataset.productId, count);
            } else {
                alert('Обновление не прошло');
            }
        }, 2000);
    };
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
                convertButtonToCounter(event.target, productId, 1);
            } else {
                alert(data.error);
            }
        });
    };
});


function convertButtonToCounter(element, productId, productCount) {
    element.outerHTML = `
                <div class="counter" data-product-id=${productId}>
                    <button class="minus">-</button>
                    <span class="count">${productCount}</span>
                    <button class="plus">+</button>
                </div>
            `;
}

function convertCounterToButton(element, productId) {
    element.outerHTML = `
                <button class="buy-button" data-product-id=${productId}>Купить</button>
            `;
}


function updateProductCount(productId, count) {
    // Отправка запроса на сервер для обновления количества товара в корзине
    fetch('../api/change-count-product', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify({ 
            count: count, 
            product_id: productId 
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        // document.querySelector('.count_product_cart').textContent = data.count_product;
        
    });
}