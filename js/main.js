let active = true

document.getElementsByClassName("header__burger")[0].addEventListener("click", () => {
  if (active) {
    document.getElementsByClassName("header__burger")[0].classList.add("active")
    document.getElementsByClassName("header__menu-container")[0].classList.add("active")
    active = false
  } else {
    document.getElementsByClassName("header__burger")[0].classList.remove("active")
    document.getElementsByClassName("header__menu-container")[0].classList.remove("active")
    active = true
  }
})
