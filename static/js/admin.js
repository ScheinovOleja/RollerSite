let csrfToken;
$(document).on('input', 'div.field-width, div.field-height, div.field-count, div.field-price', changeProduct)
$(document).on('input', 'input#id_extra_charge, input#id_delivery_price, input#id_installation_price, input#id_prepayment', changeForm);
$(document).on('DOMContentLoaded', function () {
    csrfToken = $("input[name='csrfmiddlewaretoken']").val();
})
$(document).on('click', 'a.inline-copylink', countSum)
$(document).on('click', 'div.add-row > a', function (e) {
    e.preventDefault();
    let hardware = document.querySelectorAll('div.field-hardware_color > div > div > span > span > span > span[role="textbox"]')
    for (let element of hardware) {
        if (element.id !== 'id_productlist_set-__prefix__-hardware_color') {
            $(element).on('DOMSubtreeModified', changeProduct)
        }
    }
})

{
    $('#id_order_price').prop('readonly', true);
}

function countSum() {
    let float_sum = 0.0;
    let sum = document.querySelector('fieldset.module.aligned > .field-order_price > div > input');
    let all_product = document.getElementsByClassName('dynamic-productlist_set');
    let extra_change = document.getElementById('id_extra_charge');
    let delivery_price = document.getElementById('id_delivery_price');
    let installation_price = document.getElementById('id_installation_price');
    let prepayment = document.getElementById('id_prepayment');
    let all_field_form = [extra_change, delivery_price, installation_price];
    if (all_product.length > 0) {
        for (let i = 0; i < all_product.length; i++) {
            let all_price = all_product[i].querySelector('fieldset.module > .field-price > div > .readonly');
            let price_value;
            if (!all_price) {
                all_price = all_product[i].querySelector('fieldset.module > .field-price > div > input');
                price_value = all_price.textContent
                all_price.value = all_price.textContent
            } else {
                price_value = all_price.innerText
            }
            float_sum = float_sum + parseFloat(price_value);
        }
    }
    for (let field of all_field_form) {
        if (isNaN(field.valueAsNumber)) {
            field.valueAsNumber = 0.0
        }
    }
    float_sum = float_sum + extra_change.valueAsNumber + delivery_price.valueAsNumber + installation_price.valueAsNumber
    sum.value = float_sum - prepayment.valueAsNumber;
}

function changeForm(e) {
    e.preventDefault();
    countSum();
}

function changeProduct(e) {
    e.preventDefault();
    if (e.type === 'DOMSubtreeModified'){
        e.currentTarget = e.currentTarget.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement
    }
    let width = e.currentTarget.parentElement.querySelector('fieldset.module > .field-width > div > input');
    let height = e.currentTarget.parentElement.querySelector('fieldset.module > .field-height > div > input');
    let count = e.currentTarget.parentElement.querySelector('fieldset.module > .field-count > div > input');
    let multiply_field = e.currentTarget.parentElement.querySelector('fieldset.module > .field-hardware_color > div > div > select')
    let type_construct = e.currentTarget.parentElement.querySelector('fieldset.module > .field-type_construction > div > div > select');
    let multiply_value = multiply_field.options[multiply_field.selectedIndex].value;
    let price = e.currentTarget.parentElement.querySelector('fieldset.module > .field-price > div > input');
    let prod_sum = e.currentTarget.parentElement.querySelector('fieldset.module > .field-price > div.child_sum > div.readonly')
    let price_value = price.value
    let request = $.ajax({
        type: "POST", method: "POST", headers: {'X-CSRFToken': csrfToken}, mode: 'same-origin', data: {
            'width': width.value,
            'height': height.value,
            'count': count.value,
            'multiply': multiply_value,
            'construct': type_construct.value,
            'price': price_value
        }, url: "/ru/ajax_calc/counting_price/",
    });
    request.done(function (price_field) {
        if (prod_sum) {
            prod_sum.innerText = price_field
        } else {
            price.innerText = price_field
            price.value = parseFloat(price_field)
        }
        countSum();
    });
    return false;
}
