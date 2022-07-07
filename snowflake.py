from turtle import *
from tlv8 import Entry

bgcolor("#549")


def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)


if __name__ == "__main__":
    speed(0)
    length = 450.0
    penup()
    backward(length/2.0)
    pendown()
    for i in range(3):
        snowflake(length, 4)
        right(120)
    mainloop()
