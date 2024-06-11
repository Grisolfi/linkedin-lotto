import secrets
from bs4 import BeautifulSoup

with open('reactions.html', 'r+') as reactions_html:
    html_content = reactions_html.read()

soup = BeautifulSoup(html_content, 'html.parser')

elements = soup.find_all(class_="text-view-model")
names = []
for element in elements:
    names.append(element.get_text(strip=True))


name = secrets.choice(names)

print(f'The winner is {name}')