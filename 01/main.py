from pprint import pprint

def main():
    actual_combination = 0
    dial_start = 50
    dial_current = dial_start
    dial_rotations = list()

    with open("input.txt", "r") as text_input:
        combo_input = text_input.readlines()

    for combo in combo_input:
        direction = combo[0]
        amount = int(combo.split(direction)[1])
        rotation = {
            "direction": direction,
            "amount": amount
        }
        dial_rotations.append(rotation)

    for rotation in dial_rotations:
        pprint(rotation)
        if rotation["direction"] == "L":
            dial_current = dial_current - rotation["amount"]
        else:
            dial_current = dial_current + rotation["amount"]
        pprint(f"Current Dial: {dial_current}")

        # Check if the dial is at literal 0 or if divisable by 100 evenly
        if dial_current == 0 or dial_current % 100 == 0:
            actual_combination += 1

    pprint(f"Actual Combination: {actual_combination}")

if __name__ == "__main__":
    main()
