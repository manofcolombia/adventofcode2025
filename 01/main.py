from pprint import pprint

def import_rotations():
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

    return dial_rotations

def exactly_zero_check(dial_current, dial_rotations):
    actual_combination = 0
    for rotation in dial_rotations:
        if rotation["direction"] == "L":
            dial_current = dial_current - rotation["amount"]
        else:
            dial_current = dial_current + rotation["amount"]

        # Check if the dial is at literal 0 or if divisable by 100 evenly
        if dial_current == 0 or dial_current % 100 == 0:
            actual_combination += 1

    return actual_combination

def passes_zero_check(dial_current, dial_rotations):
    actual_combination = 0



    return actual_combination

def main():
    dial_start = 50
    dial_current = dial_start
    dial_rotations = import_rotations()

    num_exactly_zero = exactly_zero_check(dial_current, dial_rotations)
    num_passes_zero = passes_zero_check(dial_current, dial_rotations)

    pprint(f"Number of Exactly Zero Hits (Part 1): {num_exactly_zero}")
    pprint(f"Number of Zero Passes (Part 2): {num_passes_zero}")

if __name__ == "__main__":
    main()
