with open("story.txt", "r") as file:
    lines = file.readlines()

num_lines = len(lines)

print("Number of lines in 'story.txt':", num_lines)