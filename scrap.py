import requests
from bs4 import BeautifulSoup


file= open("main.html", "w")
file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
    <title>Melien Scrap</title>
</head>
<body>''')

baseURL = 'https://www.allocine.fr/'
page = requests.get(baseURL)
soupdata = BeautifulSoup(page.content, "html.parser")
seamine = soupdata.find("div", class_="roller-slider")



for result in seamine.find_all("div", class_="roller-item"):
    image = result.find("img", class_="thumbnail-img")["src"]
    title = result.find("a", "meta-title")
    description = result.find("div", class_="meta-description").text
    link = result.find("a", "meta-title")

    if link != None : 
        link = link["href"]


    file.write(f'''
        <div class="card">
            <div class="card-header">
                {title}
            </div>
            <div class="card-body">
                <h5 class="card-title">{title}</h5>
                <figure class="thumbnail ">
                    <img class="thumbnail-img" src="{image}" alt="Vaillante" width="150" height="200">
                </figure>
                <p>{description}</p>
                <a href="https://www.allocine.fr{link}" class="btn btn-primary">Voir</a>
            </div>
        </div>'''
    )