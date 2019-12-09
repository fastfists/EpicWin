import autoapp
from epic_win.ext import db
from epic_win.products.models import Product

for i in range(10):

    product = Product(
            prodcut_type="Basketball",
            image_name="item.png",
            name=f"Nike Air Hurricane {i}",
            slug="nike-air-hurricane",
            cost=39.99,
            description_long="Ipsum esse sapiente nesciunt ex vero, aperiam maxime necessitatibus. Animi quam ratione iure non neque? Repellendus inventore sit quos nesciunt velit odio ad. Doloremque animi voluptas quod quis maxime Quibusdam fugiat cumque eius distinctio maxime necessitatibus Quos eius excepturi harum placeat pariatur eaque enim enim, harum? Nemo qui laudantium corrupti delectus eligendi Reprehenderit velit delectus asperiores distinctio totam Quasi fugit sint id soluta nesciunt! Amet repellendus saepe autem repudiandae at. Optio nobis natus molestiae placeat architecto Eligendi maxime quam eum cumque maxime Sed obcaecati aliquam eius eligendi corporis. Porro obcaecati quod vel alias unde. Amet debitis eius autem dolor enim.",
            description_short="Dolor ab sit aliquam minima doloribus. Id iure incidunt quidem iure doloribus Ipsum quas deserunt ex ut quasi Laborum repellat veritatis praesentium accusamus veniam, explicabo? Molestiae non veritatis laborum neque?",
            )

    db.session.add(product)
    db.session.commit()
