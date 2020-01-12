document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {accordion : false} );
});

var flip_to_page = function(i) {
    let old_window = window.location;
    let new_window = old_window;
    if (old_window.search === ""){
        new_window += `?page=${i}`
    }else {
        if (old_window.search.includes("page") === true) {
            console.log("regEx time");
            let regex = /page=\d/g;
            new_window = new_window.search.replace(regex,`page=${i}`)
        }else {
            new_window += `&page=${i}`
        }
    }
    window.location.replace(new_window);
}
