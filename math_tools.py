import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

def calc_once():
    expr = input("Enter expression like 3 + 4: ").strip()
    parts = expr.split()
    if len(parts) != 3:
        print("Format must be: number op number")
        return
    a_str, op, b_str = parts
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Numbers only")
        return
    if op not in OPS:
        print("Allowed ops: + - * /")
        return
    if op == "/" and b == 0:
        print("No divide by zero")
        return
    result = OPS[op](a, b)
    print(f"Result: {result}")

def basic_calculator():
    while True:
        print("\nMath Tools")
        print("1) Calculate once")
        print("0) Back")
        choice = input("Select: ").strip()
        if choice == "1":
            calc_once()
        elif choice == "0":
            return
        else:
            print("Invalid choice")