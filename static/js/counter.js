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
});