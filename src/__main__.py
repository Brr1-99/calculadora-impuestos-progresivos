LEVELS = {
    3000: 15,
    6000: 20,
    10000: 25,
    20000: 30
}


def main() -> None:
    money = int(input("€:"))
    clean_money = 0
    tax = 0
    for level, perc in LEVELS.items():
        if not level == list(LEVELS.keys())[-1]:
            if level > money:
                level_tax = float((money - clean_money)*perc*0.01)
                tax += level_tax
                break
            else:
                level_tax = float((level - clean_money)*perc*0.01)
                clean_money = level
                tax += level_tax
        else:
            if level > money:
                level_tax = float((money - clean_money)*perc*0.01)
                tax += level_tax
                break
            else:
                level_tax = float((money - clean_money)*perc*0.01)
                clean_money = level
                tax += level_tax

    print(f"You receive: {money - tax}€ and pay {tax}€")

if __name__ == "__main__":
    main()
