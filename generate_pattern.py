import random
import svgwrite

NUM_SEGMENTS = 5

LEN_MARGIN = 10
IMAGE_WIDTH = 256


def generate_pattern():
    """左右対称のパターンを生成する"""
    pattern = []
    for _ in range(NUM_SEGMENTS):
        def a(): return random.choice([0, 1])
        row = [a() for _ in range(NUM_SEGMENTS)]
        for x in range(NUM_SEGMENTS//2, NUM_SEGMENTS):
            row[-x-1] = row[x]
        pattern.append(row)
    return pattern


def get_color():
    color = random.choice([
        'lightgreen',
        'lightpink',
        'lightblue',
        'lavender',
        'khaki'
    ])
    return color

def create_svg(pattern):
    image = svgwrite.Drawing('icon.svg', size=(
        str(IMAGE_WIDTH), str(IMAGE_WIDTH)))
    rect_size = (IMAGE_WIDTH - 2*LEN_MARGIN)//NUM_SEGMENTS
    color = get_color()

    for y in range(NUM_SEGMENTS):
        for x in range(NUM_SEGMENTS):
            if pattern[y][x] == 1:
                posx = rect_size * x + LEN_MARGIN
                posy = rect_size * y + LEN_MARGIN
                image.add(svgwrite.shapes.Rect(insert=(posx, posy),
                                               size=(rect_size, rect_size), fill=color))

    return image


def main():
    pattern = generate_pattern()
    image = create_svg(pattern)
    image.save()


def api():
    pattern = generate_pattern()
    image = create_svg(pattern)
    return image.tostring()


if __name__ == '__main__':
    main()
