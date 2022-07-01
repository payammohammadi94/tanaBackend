let wrapper = document.querySelector('.slideWrapper')
let itemMenu = document.querySelectorAll('.itemMenu')

itemMenu.forEach((item,index)=>{
    
    item.addEventListener("mouseover",()=>{
        console.log(wrapper)
        wrapper.style.transform = `translateX(${-100*index}vw)`

    })
})

