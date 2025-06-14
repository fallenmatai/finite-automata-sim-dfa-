
def load_dfa_from_file(filename):
    with open(filename, "r") as file:

        lines = [line.strip() for line in file if line.strip()]

    states = lines[0].split(":")[1].split(",")
    alphabet = lines[1].split(":")[1].split(",")
    start = lines[2].split(":")[1]
    accept = lines[3].split(":")[1].split(",")

    transitions = {}
    for line in lines[4:]:
        if "->" in line:
            parts = line.split("->")
            from_state, symbol = parts[0].strip().split(",")
            to_state = parts[1].strip()
            transitions[(from_state, symbol)] = to_state

    return start, accept, transitions


def run_dfa(input_string, start, accept, transitions):
    current_state = start
    for symbol in input_string:
        if (current_state, symbol) not in transitions:
            return "NO"
        current_state = transitions[(current_state, symbol)]
    if current_state in accept:
     return "yes"
    else: "no"



config = "config.txt"
start, accept, transitions = load_dfa_from_file(config)


while True:
    s = input("")
    print(run_dfa(s, start, accept, transitions))
