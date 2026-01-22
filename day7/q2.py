"""
2. Problem
Write a program that:
1. Reads a file input.txt
2. Writes its content to output.txt line by line
3. If any line is empty, raise a custom error
4. Handle the error and print: "Empty line detected"
5. Ensure files are always properly closed
Constraints:
Must use with
Must use try–except–finally
Must use raise
No shortcuts
"""


class EmptyLineError(Exception):
    pass

try:
    with open("input.txt", "r") as infile:
        try:
            with open("output.txt", "w") as outfile:
                for line in infile:
                    if line.strip() == "":
                        raise EmptyLineError("Empty line detected")
                    outfile.write(line)

        except EmptyLineError:
            print("Empty line detected")

except FileNotFoundError:
    print("File not found")

finally:
    print("File operation completed")