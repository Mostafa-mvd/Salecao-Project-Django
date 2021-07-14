const arrow_up = document.getElementById('js-top');

function scrollFunc() {
    const y = window.scrollY;

    if (y > 0)
    {
        arrow_up.style.visibility = 'visible'
    }

    else
    {
        arrow_up.style.visibility = 'hidden'
    }
}

window.addEventListener("scroll", scrollFunc);

function scrollToTop()
{
    const c = document.documentElement.scrollTop || document.body.scrollTop;

    if (c > 0)
    {
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
    }
}


arrow_up.onclick = function (e) {
    e.preventDefault();
    scrollToTop();
}

