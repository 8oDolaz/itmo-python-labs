import json

class Item:
    def __init__(self, stats: dict):
        self.name = stats['name']
        self.points = stats['points']
        self.size = stats['size']
        self.short_name = stats['short_name']

    def __repr__(self):
        return '{' + f'{self.name}, {self.points}, {self.size}' + '}'

def memory_table_repr(mem_table: list[list[int]]) -> str:
    return '\n'.join(
        '\t'.join(str(i) for i in row)
        for row in mem_table
    )

def get_memory_table(items: list[Item], ks_size: int) -> list[list[int]]:
    items = [None] + items
    mt = [
        [0 for _ in range(ks_size + 1)]
        for _ in range(len(items))
    ]

    for k in range(1, len(items)):
        for s in range(ks_size + 1):
            if s >= items[k].size:
                mt[k][s] = max(
                    mt[k - 1][s - items[k].size] + items[k].points,
                    mt[k - 1][s]
                )
            else:
                mt[k][s] = mt[k - 1][s]

    return mt

def get_items(mem_table: list[list[int]], items: list[Item]) -> list[int]:
    packed_items = []
    i, j = len(mem_table) - 1, len(mem_table[0]) - 1
    while mem_table[i][j] != 0:
        if mem_table[i - 1][j] == mem_table[i][j]:
            i -= 1
            continue

        packed_items.append(i - 1)
        j -= items[i - 1].size
        i -= 1

    return packed_items

def main():
    with open('items.json', 'r') as file:
        items_json = json.load(file)

    items = [Item(i) for i in items_json]

    memory_table = get_memory_table(items, knapsack_size)

    print('Таблица памяти', memory_table_repr(memory_table) + '\n', sep='\n')

    packed_items = get_items(memory_table, items)

    survival_points = start_points
    knapsack = []
    for i in range(len(items)):
        if i in packed_items:
            survival_points += items[i].points
            knapsack.extend([items[i].short_name] * items[i].size)
        else:
            survival_points -= items[i].points

    knapsack = [knapsack[:4], knapsack[4:]]

    print('\n'.join(
        ', '.join(f'[{short_name}]' for short_name in row)
        for row in knapsack
    ))

    print(f'Итоговые очки выживания: {survival_points}', end='\n\n')

    additional_mem_table = get_memory_table(items, additional_task_volume)
    total_items_points = sum(i.points for i in items)

    print(f'Дополнительное задание:')
    print(f'Построим таблицу памяти для вместителньости рюкзака 7. Получим следующее:')
    print(memory_table_repr(additional_mem_table), '\n')
    print(f'Итоговые очки выживания {2*additional_mem_table[-1][-1] + start_points - total_items_points}')
    print(f'Значит, для рюкзака размера 7 ячеек нельзя упаковать предметы так, чтобы Том выжил')

if __name__ == '__main__':
    knapsack_size = 8
    additional_task_volume = 7
    start_points = 15

    main()
