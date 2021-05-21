f = open("a_example", "r")

first_line = f.readline()
rest = f.read()

team = list(first_line.split(" "))
team.pop()
total_pizza = int(team[0])
team.pop(0)
pizza = list(rest.split("\n"))
pizza.pop()

