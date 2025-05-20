import json

def load_data():
    with open("data/kars.json", "r", encoding="utf-8") as f:
        return json.load(f)

def analyze_input(user_input, laws):
    matches = []
    for law in laws:
        for keyword in law.get("märksõnad", []):
            if keyword.lower() in user_input.lower():
                matches.append(law)
                break
    return matches

if __name__ == "__main__":
    laws = load_data()
    user_input = input("Sisesta kuriteo kirjeldus: ")
    results = analyze_input(user_input, laws)
    if results:
        for r in results:
            print(f"Võimalik paragrahv: §{r['paragrahv']} – {r['nimetus']}")
            print(f"Karistus: {r['karistus']}")
            print("-" * 40)
    else:
        print("Sobivat paragrahvi ei leitud. Bot võib küsida lisaküsimusi tulevikus.")
