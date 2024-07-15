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
