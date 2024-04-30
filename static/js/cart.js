
var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId)

        updateUserOrder(productId, action)
        // console.log('User:', user)
        // if (user) {
        //     console.log('authenticated')
        // }
        // else {
        //     console.log('not authenticated')
        // }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data wowow')

    var url = '../update_cart_list/'
    
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action}) //sending data to the server
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('Data:', data)
        location.reload()
    });
}