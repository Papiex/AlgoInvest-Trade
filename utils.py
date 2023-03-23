import csv


def read_actions_csv(csv_file) -> dict:
    """read and save the data in dict"""
    actions = {}
    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        if do_we_skip_the_first_line(csv_file):
            next(reader)
        for row in reader:
            if is_null_or_not(row):
                continue
            action_name = row[0]
            price = float(row[1])
            percentage = float(row[2])
            actions[action_name] = {"price": price, "percentage": percentage}

    return actions


def do_we_skip_the_first_line(csv_file):
    """if first line of csv contains strings like 'profit' etc... skip the first line"""
    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] == "name" or row[1] == "price" or row[2] == "profit":
                return True
            else:
                return False


def is_null_or_not(row):
    """determine and pass the row if value == 0 or negative"""
    row[1] = float(row[1])
    row[2] = float(row[2])
    if float(row[1]) == 0.0 or float(row[2]) == 0.0:
        return True
    elif float(row[1]) < 0 or float(row[2]) < 0:
        return True
    else:
        return False