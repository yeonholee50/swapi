import requests
import random

def main():
    number = random.randint(1, 83)
    url = f"https://swapi.dev/api/people/{number}/"
    response = requests.get(url)
    response = response.json()
    return response

if __name__ == "__main__":
    main()