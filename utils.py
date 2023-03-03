import csv


def read_actions_csv(csv_file) -> dict:
    """read and save the data in dict"""
    actions = {}
    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in reader:
            action_name = row[0]
            price = int(row[1])
            profit = float(row[2].replace(",", "."))
            actions[action_name] = {"price": price, "profit": profit}

    return actions
