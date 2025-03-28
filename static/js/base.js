function convertElementToCounter(element, productId, productCount) {
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