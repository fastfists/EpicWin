document.addEventListener('DOMContentLoaded', function() {
    var colapse_elems = document.querySelectorAll('.collapsible');
    var colapse_instances = M.Collapsible.init(colapse_elems, {accordion : false} );

    var select_elems = document.querySelectorAll('select');
    var select_instances = M.FormSelect.init(select_elems, {});
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
