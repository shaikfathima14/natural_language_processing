# Function to check whether the string ends with 'ab'

def finite_state_automaton(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


# Main Program
text = input("Enter a string: ")

if finite_state_automaton(text):
    print("Accepted: String ends with 'ab'")
else:
    print("Rejected: String does not end with 'ab'")