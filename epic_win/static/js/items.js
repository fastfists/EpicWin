 var render_item = (item) => {
    return `
     <div class="item">
        <div class="product-info">
            <p id="name">
                ${ item.name }
            </p>
            <p id="price">
		        ${ item.cost }
            </p>
        </div>
        <img class="item-image" src="/static/images/${item.image_name}" alt="" srcset="">
        <div class="spacer"></div>
        <div class="buttons">
            <a href="" class="btn-md dark-blue">View More</a>
            <a href="" class="btn-md dark-blue">Add to cart</a>
        </div>
    </div>`
}
export default render_item;
