const searchIcon = document.querySelector('.search-icon')

const searchInput = document.querySelector('#search')

    searchIcon.addEventListener('click', ()=>{
        if(searchInput.classList.contains('show')){
            searchInput.classList.remove('show')
        }else{
            searchInput.classList.add('show')
        }
    })


const filterOpen = document.querySelector('.filter-icon')
const filterClose = document.querySelector('.filter-icon-x')

const filterContainer = document.querySelector('.filter-left-side')
    filterOpen.addEventListener('click', ()=>{
        filterContainer.classList.add('filter-show')
        console.log(filterContainer.classList)
    })
    filterClose.addEventListener('click', ()=>{
        filterContainer.classList.remove('filter-show')
        console.log(filterContainer.classList)
    })