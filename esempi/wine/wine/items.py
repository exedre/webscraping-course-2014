# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class WineItem(Item):
    Tipologia = Field()
    Codice = Field()
    Fornitore = Field()
    Regione = Field()
    Bottiglia = Field()
    Categoria = Field()
    Prezzo = Field()
    Prodotto = Field()
    Annata = Field()
    
