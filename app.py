import bs4, requests, webbrowser
from pprint import pprint
import png

import urllib.request as req
from IPython.display import display
from PIL import Image
import cv2
LINK = "https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2332490.m570.l1313&_nkw=Ruote+invernali+Mercedesz&_sacat=0"

response = requests.get(LINK)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_list=soup.find_all('div', class_="s-item__image-wrapper image-treatment")

src_image=[]
# image = div_list.find('img')
for lista_div in div_list:
    src_image.append(str(lista_div.find('img').attrs['src']))
pprint(src_image)

div_list_price = soup.find_all('span', class_="s-item__price")
for div_price in div_list_price[1:]:
    print(div_price.text)
count = 0
while count<75:
    
    name = "./images/images_"+str(count+1)+".jpg"
    save_with_text ="./images_2/images_"+str(count+1)+".jpg"
    im = cv2.imread(name)
    # response = requests.get(src)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_price = div_list_price[count+1].text
    cv2.putText(im,text_price , (30,30), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.imwrite(save_with_text, im)
    count+= 1
# url = str(src_image)
# response = requests.get(url)
# with open("image_4.png", "wb") as f:
#     f.write(response.content)