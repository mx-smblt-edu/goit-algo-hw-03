import argparse
from turtle import Screen, Turtle

SIZE = 300


def koch_curve(turtle: Turtle, recursion_depth: int, size: float) -> None:
    if recursion_depth == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, recursion_depth - 1, size / 3)
            turtle.left(angle)


def draw_koch_curve(recursion_depth: int, size: float) -> None:
    window = Screen()
    window.bgcolor("white")

    turtle = Turtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-size / 2, size / 3)
    turtle.pendown()

    for _ in range(3):
        koch_curve(turtle, recursion_depth, size)
        turtle.right(120)

    window.mainloop()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recursion", "-r", default="3", help="Recursion depth")
    args = vars(parser.parse_args())
    recursion_depth = int(args.get("recursion"))
    draw_koch_curve(recursion_depth, SIZE)


if __name__ == "__main__":
    main()
