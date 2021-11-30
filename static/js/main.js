const slideTopArrow = document.querySelector(".slideTop");
const socialBtn = document.querySelector(".social-button");
const socialItems = document.querySelectorAll(".social-round");
const socialPhone = document.querySelector(".social-phone");
const callModal = document.querySelector(".callback-modal");
const menu = document.querySelector(".navigation-list");
const menuBtn = document.querySelector(".header-hamburger");
const menuCLose = document.querySelector(".close");
const modalClose = document.querySelector('.close-modal');
const userLogo = document.querySelector('.user-logo');
const csrfToken = $("input[name='csrfmiddlewaretoken']").val();
const codeStatusText = document.querySelector('.code-status');
const getCodeBtn = document.querySelector('.get-code');
const orderNumbers = document.querySelectorAll('.order-number');
const orderStatus = document.querySelectorAll('.order-row');

function mobileMenuShow() {
    if (!menu.classList.contains("active")) {
        menu.classList.add("active");
    }
}

function mobileMenuHide() {
    if (menu.classList.contains("active")) {
        menu.classList.remove("active");
    }
}

function hideCallModal() {
    if (callModal.classList.contains("callback-modal-show")) {
        callModal.classList.remove("callback-modal-show");
    }
}

menuBtn.addEventListener("click", mobileMenuShow);

menuCLose.addEventListener("click", mobileMenuHide);

modalClose.addEventListener('click', hideCallModal)

function openSocialMenu() {
    if (socialBtn) {
        socialItems.forEach((item) => {
            item.classList.toggle("active");
        });
    }
}

function showCallModal(e) {
    e.preventDefault();
    if (!callModal.classList.contains("active")) {
        callModal.classList.add("callback-modal-show");
        socialItems.forEach(item => {
            item.classList.remove('active');
        })
    } else {
        callModal.classList.remove("callback-modal-show");
    }
}

socialPhone.addEventListener("click", showCallModal);

socialBtn.addEventListener("click", openSocialMenu);

$(".slider-wrapper").slick({
    infinity: true,
    dots: true,
});

$(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
        $(".slideTop").addClass("active");
    } else {
        $(".slideTop").removeClass("active");
    }
});

$(".slideTop").click(function () {
    $("html, body").animate({scrollTop: 0}, "slow");
    return false;
});

function backCallModal() {
    let name = $("input[name='modal-name']").val();
    let phone = $("input[name='modal-phone']").val();
    $(".modal_back_call").show('slow');
    setTimeout(function () {
        $(".modal_back_call").hide('slow');
    }, 3000);
    $.ajax({
        type: "POST",
        method: "POST",
        headers: {'X-CSRFToken': csrfToken},
        mode: 'same-origin',
        url: "mailing/",
        data: {'name': name, 'phone': phone},
    });
    return false;
}


function backCallForm() {
    let name = $("input[name='name']").val();
    let phone = $("input[name='phone']").val();
    $(".form_back_call").show('slow');
    setTimeout(function () {
        $(".form_back_call").hide('slow');
    }, 3000);
    $.ajax({
        type: "POST",
        method: "POST",
        headers: {'X-CSRFToken': csrfToken},
        mode: 'same-origin',
        url: "mailing/",
        data: {'name': name, 'phone': phone},
    });
    return false;
}


function openLoginForm(e) {
    e.preventDefault();
    if (!userLogo.classList.contains("active-login")) {
        $(".form-login-auth").show('slow');
        userLogo.classList.add("active-login");
    } else {
        $(".form-login-auth").hide('slow');
        userLogo.classList.remove("active-login");
    }
}


userLogo.addEventListener("click", openLoginForm);


for (let i = 0; i < orderNumbers.length && orderStatus.length; i++) {
    orderNumbers[i].addEventListener('click', () => {
        for (elem of document.querySelectorAll('[data-target]')){
            let test = jQuery.inArray(elem.dataset.target, orderStatus[i].classList)
            if (test != -1){
                let test_2 = document.getElementsByClassName(elem.dataset.target)
                for (clas of test_2){
                    clas.classList.toggle('active')
                }

            }
            // orderStatus[i].classList.toggle('active');
        }
    });
}

getCodeBtn.addEventListener('click', () => {
    codeStatusText.classList.add('active');
});

function openTab(evt, tabName) {
    let i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName('tab-content');
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = 'none';
    }

    tablinks = document.getElementsByClassName('tab-link');
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(' active', '');
    }

    document.getElementById(tabName).style.display = 'block';
    evt.currentTarget.className += ' active';
}


// Accordeon

const accButtons = document.getElementsByClassName('accordeon');
const accContents = [...document.getElementsByClassName('tab-content')];
for (let item of accButtons) {
    item.addEventListener('click', (e) => {
        if (e.target.classList.contains('b1')) {
            accContents[0].classList.toggle('mobiled');
            accContents[0].style.display = 'block';
            accContents[1].classList.remove('mobiled');
            accContents[2].classList.remove('mobiled');
        } else if (e.target.classList.contains('b2')) {
            accContents[1].classList.toggle('mobiled');
            accContents[1].style.display = 'block';
            accContents[0].classList.remove('mobiled');
            accContents[2].classList.remove('mobiled');
        } else {
            accContents[2].classList.toggle('mobiled');
            accContents[2].style.display = 'block';
            accContents[0].classList.remove('mobiled');
            accContents[1].classList.remove('mobiled');
        }
    })
}
