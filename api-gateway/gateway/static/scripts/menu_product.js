const SELECT_MENU = document.querySelector("#menu-btn");
const aside = document.querySelector("aside");

var state = 0; // 0 - display is none

SELECT_MENU.addEventListener("click", () => {
    state = ~state
    if(state === -1){
        aside.classList.add("aside-visible");
    }
    if(state === 0){
        aside.classList.remove("aside-visible");
    }
})

