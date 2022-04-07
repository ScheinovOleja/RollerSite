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
const orderNumbers = document.querySelectorAll('.parent');
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
    speed: 300,
    autoplay: true,
    autoplaySpeed: 2000,
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

function mailSendToTg() {
    let error = false
    let name = $("input[name='name']").val();
    let phone = $("input[name='tel']").val();
    let email = $("input[name='mail']").val();
    let text = $("textarea[name='user-message']").val()
    if (!name) {
        $(".error-name").show('slow');
        error = true
    } else if (!phone) {
        $(".error-phone").show('slow');
        error = true
    } else if (!email) {
        $(".error-email").show('slow');
        error = true
    } else if (!text) {
        $(".error-text").show('slow');
        error = true
    }
    setTimeout(function () {
        $(".submit-info").hide('slow');
        $(".error-name").hide('slow');
        $(".error-phone").hide('slow');
        $(".error-email").hide('slow');
        $(".error-text").hide('slow');
    }, 3000);
    if (error) {
        return false
    }
    $(".submit-info").show('slow');
    setTimeout(function () {
        $(".submit-info").hide('slow');
    }, 3000);
    $.ajax({
        type: "POST",
        method: "POST",
        headers: {'X-CSRFToken': csrfToken},
        mode: 'same-origin',
        url: "send_tg/",
        data: {'name': name, 'phone': phone, 'email': email, 'text': text},
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
        for (let child of orderStatus) {
            let entry = jQuery.inArray(orderNumbers[i].dataset.target, child.classList)
            if (entry !== -1) {
                child.classList.toggle('active')
            }
        }
    });
}

{
    let tab;
    let myUrl = window.location.href.split('#')[1];
    if (myUrl === undefined) {
        tab = document.getElementById('personal-information-tab');
    } else {
        tab = document.getElementById(myUrl);
    }
    tabcontent = document.getElementsByClassName('tab-content');
    tab.className += ' active';
    for (let i = 0; i < tabcontent.length; i++) {
        let content = jQuery.inArray(tab.id.split('-tab')[0], tabcontent[i].classList)
        if (content === -1) {
            tabcontent[i].style.display = 'none';
        } else {
            tabcontent[i].style.display = 'block';
        }
    }
}


function openTab(evt, tabName) {
    let i, tabcontent, tablinks;
    window.history.replaceState({}, '', '#' + tabName + '-tab');
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


function ChangeAvatar() {
    $.ajax({
        type: "POST",
        method: "POST",
        headers: {'X-CSRFToken': csrfToken},
        mode: 'same-origin',
        url: "change_avatar/",
        success: function (status) {
            location.reload();
        }
    });
    return false;
}

const inpRadio = document.getElementsByName('social-radio');
for (let i = 0; i < inpRadio.length; i++) {
    inpRadio[i].addEventListener('click', () => {
        if (inpRadio[i].checked) {
            if (i === 0) {
                socialIcon[i].classList.add('telegram-active')
                socialIcon[1].classList.remove('viber-active')
                socialIcon[2].classList.remove('whatsapp-active')
            } else if (i === 1) {
                socialIcon[0].classList.remove('telegram-active')
                socialIcon[i].classList.add('viber-active')
                socialIcon[2].classList.remove('whatsapp-active')
            } else if (i === 2) {
                socialIcon[0].classList.remove('telegram-active')
                socialIcon[1].classList.remove('viber-active')
                socialIcon[i].classList.add('whatsapp-active')
            }
        }
        let network = inpRadio[i].value
        if (inpRadio[i].type === "radio" && inpRadio[i].checked) {
            let request = $.ajax({
                type: "POST",
                method: "POST",
                headers: {'X-CSRFToken': csrfToken},
                mode: 'same-origin',
                data: {'network': network},
                url: "change_social_network/",
            });
            request.fail(function () {
                // alert('не успех')
            });
            request.done(function () {
                // alert('успех')
            });
            return false;
        }
    });
}

const socialIcon = document.getElementsByClassName('social-icon')
for (let i = 0; i < socialIcon.length; i++) {
    if (inpRadio[i].disabled) {
        socialIcon[i].classList.remove(socialIcon[i].classList.item(1));
        socialIcon[i].classList.toggle('disabled-social-icon');
    }
    if (inpRadio[i].checked) {
        if (i === 0) {
            socialIcon[i].classList.add('telegram-active')
        } else if (i === 1) {
            socialIcon[i].classList.add('viber-active')
        } else if (i === 2) {
            socialIcon[i].classList.add('whatsapp-active')
        }
    }
}



