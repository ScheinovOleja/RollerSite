let csrfToken;
$(document).on('input', 'div.field-width, div.field-height, div.field-count, div.field-hardware_color, div.field-price', changeProduct)
$(document).on('input', 'input#id_extra_charge, input#id_delivery_price, input#id_installation_price', changeForm);
$(document).on('input', 'div.field-type_construction', changeMaterial);
$(document).on('DOMContentLoaded', function () {
    csrfToken = $("input[name='csrfmiddlewaretoken']").val();
})
$(document).on('click', 'a.inline-copylink', countSum)
$(document).on('click', 'div.add-row > a', function (e) {
    e.preventDefault();
    let curOpt = document.querySelectorAll('div.field-type_construction > div > div > select');
    for (let element of curOpt) {
        if (element.id !== 'id_productlist_set-__prefix__-type_construction') {
            let parents = $(element).parents()
            reloadMaterials(element.value, parents[2], e)
        }
    }
})

{
    $('#id_order_price').prop('readonly', true);
}

function reloadMaterials(curOpt, parent, event) {
    let request = $.ajax({
        type: "POST",
        method: "POST",
        headers: {'X-CSRFToken': csrfToken},
        mode: 'same-origin',
        data: {
            'construct': curOpt
        },
        url: "/ru/ajax_calc/get_material/",
    });
    request.done(function (materials) {
        let select = parent.parentElement.querySelector('div.field-material > div > div > select');
        let price = parent.querySelector('div.form-row.field-price');
        let new_price = document.createElement('div');
        $(select.options).each(function () {
            $(this).remove()
        })
        let all_materials = jQuery.parseJSON(materials)
        for (let option in all_materials) {
            if (option === 'is_special' && all_materials[option]) {
                new_price.classList.add("form-row", "field-price")
                new_price.innerHTML = '<div>' +
                    '<label class="required" for="id_productlist_set-0-price">Цена за единицу:</label>' +
                    '<input type="number" name="productlist_set-0-price" step="any" id="id_productlist_set-0-price">' +
                    '</div>'
            } else {
                new_price.classList.add("form-row", "field-price")
                new_price.innerHTML = '<div>' +
                    '<label>Цена:</label>' +
                    '<div class="readonly">-</div>' +
                    '</div>'
                changeProduct(event)
            }
            price.replaceWith(new_price)
            if (option === 'is_special') {
            } else {
                let newOption = new Option(option, all_materials[option]);
                select.append(newOption)
            }
        }
    });
    request.fail(function (materials) {
        let select = document.querySelector('div.field-material > div > div > select');
        $(select.options).each(function () {
            $(this).remove()
        })
    });
}

function changeMaterial(e) {
    e.preventDefault();
    let curOpt = e.target.value
    reloadMaterials(curOpt, e.currentTarget.parentElement, e)
}

function countSum() {
    let float_sum = 0.0;
    let sum = document.querySelector('fieldset.module.aligned > .field-order_price > div > input');
    let all_product = document.getElementsByClassName('dynamic-productlist_set');
    let extra_change = document.getElementById('id_extra_charge');
    let delivery_price = document.getElementById('id_delivery_price');
    let installation_price = document.getElementById('id_installation_price');
    let all_field_form = [extra_change, delivery_price, installation_price];
    if (all_product.length > 0) {
        for (let i = 0; i < all_product.length; i++) {
            let all_price = all_product[i].querySelector('fieldset.module > .field-price > div > .readonly');
            let price_value;
            if (!all_price) {
                all_price = all_product[i].querySelector('fieldset.module > .field-price > div > input');
                price_value = all_price.textContent
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
    sum.value = float_sum;
}

function changeForm(e) {
    e.preventDefault();
    countSum();
}

function changeProduct(e) {
    e.preventDefault();
    let width = e.currentTarget.parentElement.querySelector('fieldset.module > .field-width > div > input');
    let height = e.currentTarget.parentElement.querySelector('fieldset.module > .field-height > div > input');
    let count = e.currentTarget.parentElement.querySelector('fieldset.module > .field-count > div > input');
    let multiply_field = e.currentTarget.parentElement.querySelector('fieldset.module > .field-hardware_color > div > div > select')
    let type_construct = e.currentTarget.parentElement.querySelector('fieldset.module > .field-type_construction > div > div > select');
    let multiply_value = multiply_field.options[multiply_field.selectedIndex].value;
    let price = e.currentTarget.parentElement.querySelector('fieldset.module > .field-price > div > input');
    let price_value;
    if (!price) {
        price = e.currentTarget.parentElement.querySelector('fieldset.module > .field-price > div > div.readonly')
        price_value = null
    } else {
        price_value = price.value
    }
    let request = $.ajax({
        type: "POST",
        method: "POST",
        headers: {'X-CSRFToken': csrfToken},
        mode: 'same-origin',
        data: {
            'width': width.value, 'height': height.value, 'count': count.value, 'multiply': multiply_value,
            'construct': type_construct.value, 'price': price_value
        },
        url: "/ru/ajax_calc/counting_price/",
    });
    request.done(function (price_field) {
        price.innerText = price_field
        countSum();
    });
    return false;
}
