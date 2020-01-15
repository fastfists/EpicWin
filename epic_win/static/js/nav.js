var submit_search = async function() {
    var data = new FormData();
    q = document.querySelector("#search").value;
    data.append("q", q);
}


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });