# THIS IS stuff I NEED
csv = "stuff.csv"
def num2():
    with open(csv) as file:
        for line in file:
            line = line.strip() #preprocess line
            print(line) #take action on line instead of storing in a list. more memory efficient at the cost of execution speed.
# USE THIS FOR THE GRAPH


def num1():
    with open(csv, "r") as infile:
        lines = infile.readlines()
    with open(csv, "w") as outfile:
        for pos, line in enumerate(lines):
            if pos != 0:
                outfile.write(line)
    with open(csv, "a") as addfile:
        # GET REAL VALUES
        moist = 1
        temp = 1
        addfile.write(f"\n{moist},{temp}")

# USE THIS FOR THE BG SAVE
num1()
