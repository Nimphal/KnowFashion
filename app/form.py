__author__ = 'nevelina'
from flask.ext.wtf import Form
from app import app
from wtforms.fields import TextField, SelectField, DecimalField
from wtforms import validators

# this would ideally be generated and updated by the users
brand_choices = [
    ('dorothy perkins', 'Dorothy Perkins'),
    ('quiz', 'Quiz'),
    ('people tree', 'People Tree'),
]

colour_choices = [
    ('',''),
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('pink', 'Pink'),
    ('brown', 'Brown'),
    ('beige', 'Beige'),
    ('cream', 'Cream'),
    ('grey', 'Grey'),
    ('navy', 'Navy'),
    ('pink', 'Pink'),
    ('white', 'White'),
    ('black', 'Black'),
    ('multi', 'Multi'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
    ('silver', 'Silver'),
    ('gold', 'Gold'),
]

clothing_choices = [
    ('',''),
    ('accessories', 'Accessories'),
    ('bag', 'Bag'),
    ('coat', 'Coat'),
    ('jacket', 'Jacket'),
    ('hoodie/sweatshirt', 'Hoodie/Sweatshirt'),
    ('jeans', 'Jeans'),
    ('jewellery', 'Jewellery'),
    ('jumper', 'Jumper'),
    ('cardigan', 'Cardigan'),
    ('jumpsuit', 'Jumpsuit'),
    ('playsuit', 'Playsuit'),
    ('kimono', 'Kimono'),
    ('lingerie', 'Lingerie'),
    ('nightwear', 'Nightwear'),
    ('shoes', 'Shoes'),
    ('socks', 'Socks'),
    ('tights', 'Tights'),
    ('suit', 'Suit'),
    ('swimwear', 'Swimwear'),
    ('leggings', 'Leggings'),
    ('dress', 'Dress'),
    ('blazer', 'Blazer'),
    ('skirt', 'Skirt'),
    ('trousers', 'Trousers'),
    ('top', 'Top'),
]

store_choices = [
    ('debenhams', 'Debenhams'),
    ('house of fraser', 'House of Fraser'),
    ('asos', 'ASOS'),
]


class SimpleForm(Form):
    clothing_type = SelectField('Clothing type',
                                [validators.Required()],
                                choices=clothing_choices,

    )
    brand = TextField('Brand name',
                      [validators.Required()],
    )
    store = TextField('Store name',
    )
    colour = SelectField('Colour',
                         [validators.Required()],
                         choices=colour_choices,

    )
    country = SelectField('Country',
                          [validators.Required()],
                          choices=app.config['COUNTRY_CHOICES'],
    )
    price = DecimalField('Price',
                         [validators.Optional()],
    )
    currency = SelectField('Currency',
                           choices=app.config['CURRENCY_CHOICES'],
    )
    date_purchased = TextField('Date of Purchase',
    )
    upload_url = TextField('Upload URL',
    )


class BrowseForm(Form):
    clothing_type = SelectField('Clothing type',
                                choices=clothing_choices,

    )
    brand = TextField('Brand name',
    )
    store = TextField('Store name',
    )
    colour = SelectField('Colour',
                         choices=colour_choices,
    )
    country = SelectField('Country',
                          choices=app.config['COUNTRY_CHOICES'],
    )