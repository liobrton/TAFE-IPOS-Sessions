bottles = 99

while bottles > 0:
    print(f"""
    {bottles} bottle{"s" if bottles > 1 else ""} of beer on the wall
    {bottles} bottle{"s" if bottles > 1 else ""} of beer
    take {"one" if bottles > 1 else "it"} down, pass it around
    {f"{bottles - 1} bottle{"s" if bottles > 1 else ""} of beer on the wall" if bottles > 1 else f"no more bottles of beer on the wall"}
    
    """)
    bottles -= 1
