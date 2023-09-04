import requests


def main():
    choice = input("[R]eport or [S]ee report")
    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        if choice.lower().strip() == 's':
            see_event()
        else:
            print("scelta sbagliata")


def report_event():
    desc = input("inserisci descrizione")
    city = input("inserisci la città")

    data = {
        "description": desc,
        "location": {
            "city": city
        }
    }
    url = "http://localhost:800/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()
    result = resp.json()
    print(f"salvato elemento {result.get('id')}")


def see_event():
    url = "http://localhost:800/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
