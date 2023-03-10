import itertools
import sys
from time import perf_counter

from utils import read_actions_csv


def get_best_combinations(csv_file):
    """get the best combinations with bruteforce"""
    start_time = perf_counter()
    # Dictionnaire d'actions
    actions = read_actions_csv(csv_file)

    # Ajouter le bénéfice pour chaque action
    for action in actions:
        price = actions[action]["price"]
        percentage = actions[action]["percentage"]
        benefit = price * percentage / 100
        actions[action]["benefit"] = benefit

    # Trouver la combinaison optimale d'actions
    max_budget = 500
    max_profit = 0
    max_combination = ()
    count = 0
    optimal_price = 0

    for actions_number in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions.keys(), actions_number):
            count += 1
            #print(count, end="\r")
            total_price = sum([actions[action]["price"] for action in combination])
            if total_price <= max_budget:
                total_benefit = sum([actions[action]["benefit"] for action in combination])
                if total_benefit > max_profit:
                    max_profit = total_benefit
                    max_combination = combination
                    optimal_price = total_price

    elapsed_time = perf_counter() - start_time

    print(
        f"[Dépense totale: {optimal_price}€ sur {max_budget}€] \n"
        f"[Bénéfice total: {round(max_profit, 2)}€] \n"
        f"[Temps d'éxécution: {elapsed_time:.3f}] \n"
        f"[Nombre de combinaisons: {count}] \n"
        f"Avec cette liste d'action: \n {max_combination}"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: You need to specify a csv_file [py script.py csv_file_name]")
        sys.exit(1)

    csv_file = sys.argv[1]
    get_best_combinations(csv_file)
