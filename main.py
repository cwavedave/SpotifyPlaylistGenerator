from bs4 import BeautifulSoup
import requests

bb_search = input("Find out what the top 100 songs were the year you were born! /n Write your birthdate in this format YYYY-MM-DD")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{bb_search}")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
td_data = soup.findAll(name="a", class_="storylink")
