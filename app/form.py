__author__ = 'nevelina'
from flask.ext.wtf import Form
from wtforms.fields import TextField, SelectField, DecimalField

#this would ideally be generated and updated by the users
brand_choices = [
	('dorothy perkins', 'Dorothy Perkins'),
	('quiz', 'Quiz'),
	('people tree', 'People Tree'),
]

colour_choices = [
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
	('accessories', 'Accessories'),
	('bag', 'Bag'),
	('coat', 'Coat'),
	('jacket', 'Jacket'),
	('hoodie/swetachirt', 'Hoodie/Sweatshirt'),
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

currency_choices = [
	('eur', 'EUR'),
	('gbp', 'GBP'),
	('usd', 'USD'),
]

store_choices = [
	('debenhams', 'Debenhams'),
	('house of fraser', 'House of Fraser'),
	('asos', 'ASOS'),
]

country_choices = [
	('china', 'China'),
	('united kingdom', 'United Kingdom'),
	('vietnam', 'Vietnam'),
]
	
class SimpleForm(Form):
    clothing_type = SelectField('Clothing type', choices = clothing_choices)
    brand = SelectField('Brand name', choices = brand_choices)
    store = SelectField('Store name', choices = store_choices)
    colour = SelectField('Colour', choices = colour_choices)
    country = SelectField('Country', choices = country_choices)
    price = DecimalField('Price')
    currency = SelectField('Currency', choices = currency_choices)    
    date_purchased = TextField('Date of Purchase')
    
    
    
    
    
    
    
    
    
    
