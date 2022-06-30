let wrapper = document.querySelector('.slideWrapper')
let itemMenu = document.querySelectorAll('.itemMenu')

itemMenu.forEach((item,index)=>{
    
    item.addEventListener("click",()=>{
        wrapper.style.transform = `translateX(${-100*index}vw)`

    })
})