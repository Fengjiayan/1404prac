"""
Wimbledon
Estimate: 30 minutes
Actual:   26 minutes
"""


def main():
    rows = read_datas("wimbledon.csv")
    show_champions(rows)
    print()
    show_champion_country(rows)


def read_datas(filename):
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        read_header = False
        for line in in_file.readlines():
            if not read_header:
                read_header = True
                continue
            rows.append(line.strip().split(","))
    return rows


def show_champions(rows):
    champion_count = {}
    for row in rows:
        champion = row[2]
        if champion not in champion_count:
            champion_count[champion] = 0
        champion_count[champion] += 1
    print("Wimbledon Champions:")
    for champion in champion_count:
        print(f"{champion} {champion_count[champion]}")


def show_champion_country(rows):
    countries = set()
    for row in rows:
        country = row[1]
        countries.add(country)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(list(countries))))


main()
