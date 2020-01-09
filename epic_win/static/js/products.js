import render_item from './items.js'

async function parse_query_string(query) {
  var vars = query.split("&");
  var query_string = {};
  for (var i = 0; i < vars.length; i++) {
    var pair = vars[i].split("=");
    var key = decodeURIComponent(pair[0]);
    var value = decodeURIComponent(pair[1]);
    // If first entry with this name
    if (typeof query_string[key] === "undefined") {
      query_string[key] = decodeURIComponent(value);
      // If second entry with this name
    } else if (typeof query_string[key] === "string") {
      var arr = [query_string[key], decodeURIComponent(value)];
      query_string[key] = arr;
      // If third or later entry with this name
    } else {
      query_string[key].push(decodeURIComponent(value));
    }
  }
  return query_string;
}

async function render_products({page, per_page}) {

    var query_string = window.location.search.substring(1);
    let response = await fetch(`/api/v1/search?page=${page}&per_page=${per_page}&${query_string}`);

    let json = await response.json();
    let products = json["products"];
    let html = "<div class='items'> "
    for (let i = 0; i < products.length; i++){
        let product = products[i];
        html += render_item(product, true);
    }
    html += "</div>"
//
    document.querySelector("#shop-list").innerHTML = html;
}

document.addEventListener("DOMContentLoaded", function(event) {
    render_products({"page" : 1, "per_page": 12});
    var elems = document.querySelectorAll('.collapsible');
    var options = {accordion: false}
    var instances = M.Collapsible.init(elems, options);
});
