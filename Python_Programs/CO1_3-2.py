transition = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

start = 'q0'
final = 'q2'

string = input("Enter String: ")

state = start
path = [state]

for ch in string:
    if (state, ch) in transition:
        state = transition[(state, ch)]
        path.append(state)
    else:
        print("Invalid Input")
        exit()

print("Transition Path:")
print(" -> ".join(path))

if state == final:
    print("Accepted")
else:
    print("Rejected")