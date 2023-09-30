const loginform=document.querySelector(".registerform")

function loginpopup(){
    loginform.classList.toggle("openform")
}

const addform=document.querySelector(".addform-form")
const table=document.querySelector(".table-div")

function openform(){
    addform.classList.toggle("openaddform")
    //table.style.display="none"
   
        table.classList.toggle("closetable")
   
}
const ulnav=document.querySelector(".ulnav")

// for categor dropdown
const dropdowncat=document.querySelector(".mytopcat")
function dropdown(){
    dropdowncat.classList.toggle("dropdownnav")
    ulnav.classList.remove('openmobilnavbar')
}

// mobile responsivenes

function openmobilnavbar(){
ulnav.classList.toggle("openmobilnavbar")
}