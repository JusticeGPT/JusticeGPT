import json

def load_data():
    with open("data/kars.json", "r", encoding="utf-8") as f:
        return json.load(f)

def analyze(text, data):
    matches = []
    for entry in data:
        if any(word in text.lower() for word in entry["nimetus"].lower().split()):
            matches.append(entry)
    return matches

if __name__ == "__main__":
    data = load_data()
    user_input = input("Sisesta kuriteo kirjeldus: ")
    result = analyze(user_input, data)
    if result:
        for r in result:
            print(f"§{r['paragrahv']} – {r['nimetus']}")
            print(f"Karistus: {r['karistus']}")
            print()
    else:
        print("Paragrahvi ei leitud.")
