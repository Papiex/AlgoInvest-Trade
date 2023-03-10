import itertools

from utils import read_actions_csv


def get_best_combinations():
    """get the best combinations with bruteforce"""

    # Dictionnaire d'actions
    actions = read_actions_csv("dataset/dataset_test.csv")

    # Ajouter le bénéfice pour chaque action
    for action in actions:
        price = actions[action]["price"]
        profit = actions[action]["profit"]
        benefit = price * profit / 100
        actions[action]["benefit"] = benefit

    max_budget = 500


    # Trouver la combinaison optimale d'actions
    max_profit = 0
    max_combination = ()
    count = 0

    for actions_number in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions.keys(), actions_number):
            count += 1
            total_price = sum([actions[action]["price"] for action in combination])
            if total_price <= max_budget:
                total_benefit = sum([actions[action]["benefit"] for action in combination])
                if total_benefit > max_profit:
                    max_profit = total_benefit
                    max_combination = combination

    # Afficher la combinaison optimale et le bénéfice total et le nombre de combinaisons testée
    print("Combinaison optimale d'actions: ", max_combination)
    print(f"Pour un total de {count} combinaisons possible")
    print("Bénéfice total: ", round(max_profit, 2), "euros")


get_best_combinations()
