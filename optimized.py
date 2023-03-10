from utils import read_actions_csv

import sys


def calculate_profit(price, profit) -> float:
    """calculate profit of action and return benefit"""
    profit = profit / 100
    profit = price * profit
    profit = round(profit, 2)

    return profit


def calculate_ratio(price, benefit) -> float:
    """calculate the ratio price/benefit and return it"""
    ratio = benefit / price
    ratio = round(ratio, 2)

    return ratio


def add_benefit_to_dict(actions) -> dict:
    """convert action profit percentage to amount and add to action dict"""
    for action in actions:
        actions[action]["action_benefit"] = calculate_profit(
            actions[action]["price"], actions[action]["profit"]
        )

    return actions


def add_ratio_to_dict(actions) -> dict:
    """calculate the ratio and add in to action dict"""
    actions_dict = add_benefit_to_dict(actions)
    for action in actions_dict:
        actions_dict[action]["ratio"] = calculate_ratio(
            actions_dict[action]["price"], actions_dict[action]["action_benefit"]
        )

    return actions_dict


def sort_profits(actions) -> dict:
    """sort the action dict according to the best ratio"""
    action_dict = add_ratio_to_dict(actions)
    actions_sorted = {
        k: v
        for k, v in sorted(
            action_dict.items(), key=lambda item: item[1]["ratio"], reverse=True
        )
    }

    return actions_sorted


def calculate_best_placements(csv_file):
    """Calculate the best placements with 500 budget"""
    actions = read_actions_csv(csv_file)
    actions_sorted = sort_profits(actions)
    budget = 0
    max_cost = 500
    best_actions = []
    profit = 0

    for action in actions_sorted:
        if budget + actions_sorted[action]["price"] > max_cost:
            continue
        else:
            budget += actions_sorted[action]["price"]
            profit += actions_sorted[action]["action_benefit"]
            best_actions.append(action)

    print(
        f"la dépense totale est de {budget}€ sur {max_cost}€ pour un bénéfice total de {round(profit, 2)}€."
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: You need to specify a csv_file [py script.py csv_file_name]")
        sys.exit(1)

    csv_file = sys.argv[1]
    calculate_best_placements(csv_file)
