def esc(code):
    return f'\u001b[{code}m'

def draw_pattern(size=3):
    colors = [BLACK, WHITE]

    pattern = []
    for i in range(size):
        color_offset = i % 2
        row = [
            f'{colors[(j + color_offset) % len(colors)]}'
            for j in range(size + 1)
        ]

        pattern.append(f'{" ".join(row)}{END}')
    
    print('\n'.join(pattern))

if __name__ == '__main__':
    BLACK = esc(40)
    WHITE = esc(47)
    END = esc(0)

    draw_pattern(5)
