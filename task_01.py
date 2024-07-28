"""
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, 
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. 
Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

import heapq

def min_cost_to_connect_cables(cables):
    if len(cables) == 0:
        return 0

    heapq.heapify(cables)
    total_cost = 0
    order = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

        order.append((first, second, cost))

    return total_cost, order


cables = [1, 1, 2, 1, 2, 2]
total_cost, order = min_cost_to_connect_cables(cables)

print("Порядок об'єднання, який мінімізує загальні витрати:")
for i, step in enumerate(order):
    print(f"{step[0]} + {step[1]} = {step[2]}")

print(f"Мінімальні витрати на з'єднання кабелів: {total_cost}")
