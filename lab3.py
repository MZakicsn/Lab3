def write_file_with_name(file_path, name):
    with open(file_path, 'w') as file:
        file.write(f"Repository and git hub test file / n Good bye.")

if __name__ == "__main__":
    # Provide the file path and your name
    file_path = "mzikria.txt"  # Change this to the desired file path
    your_name = "zaki"   # Change this to your actual name

    # Call the function to write the file
    write_file_with_name(file_path, your_name)

    print(f"File '{file_path}' this file has been created.")

# Text from Professor LAb
def helloWorld():
	print ('helloWorld')
helloWorld()

print('Ops445_lab2b by "MZikria"')
