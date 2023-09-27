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



