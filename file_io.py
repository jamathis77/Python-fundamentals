
# # Create a python file in python, that itself modifies the testing.txt file to say
# # I'm sorry, I cannot do that.

# python_file = open("./file_io_hub/change_text.py", "x")

# valid_code = """

# to_change = open("./testing.txt", "w")

# to_change.write("I'm sorry, I cannot do that")

# to_change.close()

# """

# python_file.write(valid_code)

# python_file.close()


with open("with_statement.py", "w") as f:
    f.write("# Im a comment\nprint('Hello world')")

