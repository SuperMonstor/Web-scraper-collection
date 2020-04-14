from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=38'

# Opening connection and getting html page
uClient = uReq(my_url)
html_page = uClient.read()
uClient.close()

# html parsing
page_soup = soup(html_page, "html.parser")

# grab each product
containers = page_soup.findAll("div", {"class" : "item-container"})
print("No of containers: " +str(len(containers)))

filename = "./datasets/newegg_gpus.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand_container = container.findAll("div", {"class": "item-branding"})
    brand = brand_container[0].a.img['title']

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    price_shipping = shipping_container[0].text.strip()

    f.write(brand + "," + product_name.replace(",", "|") + "," + price_shipping +"\n")
    print("brand: " +brand)
    print("product_name: " +product_name)
    print("price_shipping: " +price_shipping)
    print()

f.close()