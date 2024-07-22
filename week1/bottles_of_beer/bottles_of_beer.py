num_bottles = 99

while num_bottles > 0:
    if num_bottles == 1:
        print(f"{num_bottles} bottle of beer on the wall, {num_bottles} bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        print(f"Take one down and pass it around, {num_bottles - 1} bottles of beer on the wall.")

    print()
    num_bottles -= 1

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")

# mine
bottles = 99


def plurals(n):
    """
    Takes a number and returns the relevant plurality of the word bottle for that number.
    :param n: The number of bottles.
    :return: 'n bottles' if the number is not 1, otherwise 'n bottle'
    """
    return F"{n} bottle{"s" if n != 1 else ""}"


while bottles > 0:
    print(f"""
    {plurals(bottles)} of beer on the wall
    {plurals(bottles)} of beer
    take {"one" if bottles > 1 else "it"} down, pass it around
    {f"{plurals(bottles)} of beer on the wall" if bottles > 1 else f"no more bottles of beer on the wall"}
    
    """)
    bottles -= 1
