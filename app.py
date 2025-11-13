import requests


def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erreur lors de la récupération de la blague :", response.status_code)
        return

    data = response.json()

    if data["type"] == "single":
        print("\n🤣 Blague :")
        print(data["joke"])
    else:
        print("\n😂 Blague :")
        print(data["setup"])
        print(data["delivery"])


if __name__ == "__main__":
    print("=== Joke Fetcher ===")
    get_joke()
