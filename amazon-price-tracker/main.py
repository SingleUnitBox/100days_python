import requests


params = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}
response = requests.get("https://www.amazon.co.uk/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5N1WBH/ref=sr_1_1_sspa?crid="
                        "2EWBIVOLJY2MX&keywords=macbook&qid=1666214131&qu=eyJxc2MiOiI1LjEzIiwicXNhIjoiNS4wNiIsInFzcCI6Ij"
                        "MuOTUifQ%3D%3D&sprefix=macbook%2Caps%2C73&sr=8-1-spons&psc=1", headers=params)
webpage = response.text
print(webpage)