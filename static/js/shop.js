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


document.addEventListener('input', function(event) {
    if (event.target.classList.contains('count')) {
        event.target.value = parseInt(event.target.value);
        const counter = event.target.closest('.counter');
        let count = parseInt(counter.querySelector('.count').value);
        if (isNaN(count) || count < 0) {
            counter.querySelector('.count').value = 0;
            count = 0;
        }

        if (count === 0) {
            convertCounterToButton(counter, counter.dataset.productId);
            updateProductCount(counter.dataset.productId, count);
            return;
        }
        setTimeout(() => {
            newCount = parseInt(counter.querySelector('.count').value);
            if (count === newCount) {
                updateProductCount(counter.dataset.productId, count);
            }
        }, 2000);
    }
    
});

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('minus')) {
        const counter = event.target.closest('.counter');
        const count = parseInt(counter.querySelector('.count').value) - 1;
        counter.querySelector('.count').value = count;
        if (count === 0) {
            convertCounterToButton(counter, counter.dataset.productId);
            updateProductCount(counter.dataset.productId, count);
            return;
        }
        setTimeout(() => {
            newCount = parseInt(counter.querySelector('.count').value);
            if (count === newCount) {
                updateProductCount(counter.dataset.productId, count);
            }
        }, 2000);
    };
    if (event.target.classList.contains('plus')) {
        const counter = event.target.closest('.counter');
        const count = parseInt(counter.querySelector('.count').value) + 1;
        counter.querySelector('.count').value = count;
        if (count === 0) {
            convertCounterToButton(counter, counter.dataset.productId);
            updateProductCount(counter.dataset.productId, count);
            return;
        }
        setTimeout(() => {
            newCount = parseInt(counter.querySelector('.count').value);
            if (count === newCount) {
                updateProductCount(counter.dataset.productId, count);
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
    // element.outerHTML = 
    let newElementHtml = `
                <div class="counter" data-product-id=${productId}>
                    <button class="minus">-</button>
                    <input class="count" inputmode="numeric" value="${productCount}"></input>
                    <button class="plus">+</button>
                </div>
            `;
    let newElement = document.createElement('div');
    newElement.innerHTML = newElementHtml;
    animateReplace(element, newElement)
}

function convertCounterToButton(element, productId) {
    let newElementHtml = `
    <a href="" class="buy-button" data-product-id=${productId}>Купить</a>
    `;
    let newElement = document.createElement('div');
    newElement.innerHTML = newElementHtml;
    animateReplace(element, newElement)
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

function animateReplace(oldElement, newElement) {
    // Анимация исчезновения
    const fadeOut = oldElement.animate(
        [
            { opacity: 1, transform: 'scale(1)' },
            { opacity: 0, transform: 'scale(0.8)' }
        ],
        { duration: 150, easing: 'ease' }
    );

    // После завершения — замена
    fadeOut.onfinish = () => {
        oldElement.replaceWith(newElement);
        // Анимация появления нового элемента
        newElement.animate(
            [
                { opacity: 0, transform: 'scale(0.8)' },
                { opacity: 1, transform: 'scale(1)' }
            ],
            { duration: 150, easing: 'ease' }
        );
    };
}