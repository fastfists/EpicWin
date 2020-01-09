var submit_search = async function() {
    var data = new FormData();
    q = document.querySelector("#search").value;
    data.append("q", q);
}

document.querySelector(".search-form").onsubmit = async function(){
    await submit_search();
};
