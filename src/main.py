import inquirer

methods = [
    inquirer.Checkbox(
        "methods",
        message="Select methods using SPACE, confirm with ENTER",
        choices=["BFS - Breadth First Search", "DFS - Depth First Search"],
    ),
]

answers = inquirer.prompt(methods)
print(answers["methods"])
