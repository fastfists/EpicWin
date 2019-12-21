import render_item from './items.js'

async function render_products() {

    let response = await fetch('/v1/search?page=1&per_page=12');
    console.log(response)
    let json = await response.json();
    let products = json["products"];
    let html = "<div class='items'> "
    for (let i = 0; i < products.length; i++){
        let product = products[i];
        html += render_item(product);
    }
    html += "</div>"
//
    document.querySelector("#shop-list").innerHTML = html;
}


document.addEventListener("DOMContentLoaded", function(event) {
    render_products();
});
