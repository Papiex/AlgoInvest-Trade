from utils import read_actions_csv, print_action_by_action

import sys
from time import perf_counter


def calculate_profit(price, percentage) -> float:
    """calculate profit of action and return benefit"""
    profit = percentage / 100
    profit = price * profit
    profit = round(profit, 2)

    return profit


def calculate_ratio(price, benefit) -> float:
    """calculate the ratio price/benefit and return it"""
    ratio = benefit / price
    ratio = round(ratio, 2)

    return ratio


def add_profit_to_dict(actions) -> dict:
    """convert action profit percentage to amount and add to action dict"""
    for action in actions:
        actions[action]["profit"] = calculate_profit(
            actions[action]["price"], actions[action]["percentage"]
        )
    return actions


def add_ratio_to_dict(actions) -> dict:
    """calculate the ratio and add in to action dict"""
    actions_dict = add_profit_to_dict(actions)
    for action in actions_dict:
        actions_dict[action]["ratio"] = calculate_ratio(
            actions_dict[action]["price"], actions_dict[action]["profit"]
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
    start_time = perf_counter()
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
            profit += actions_sorted[action]["profit"]
            best_actions.append(action)
    elapsed_time = perf_counter() - start_time

    print(
        f"[Dépense totale: {budget}€ sur {max_cost}€]\n"
        f"[Bénéfice total: {round(profit, 2)}€] \n"
        f"[Temps d'éxécution: {elapsed_time:.3f}] \n"
        f"Avec cette liste d'action: \n {best_actions}"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: You need to specify a csv_file [py script.py csv_file_name]")
        sys.exit(1)

    csv_file = sys.argv[1]
    calculate_best_placements(csv_file)
