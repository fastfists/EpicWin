 var render_item = (item, small=false) => {

    if (small === true){
        return `
        <div class="item-sm">
        <a href="/product/${ item.slug}">
            <img class="" src="/static/images/${item.image_name}" alt="" srcset="">
        </a>
        <a href="/product/${ item.slug}" class="subheading-2"> ${ item.name } </a>
        <h4 class="text-blue"> ${ item.cost } </h4>
        </div>
        `

    }


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
            <a href="/product/${ item.slug}" class="btn-md dark-blue">View More</a>
            <a href="" class="btn-md dark-blue">Add to cart</a>
        </div>
    </div>`
}

export default render_item;
