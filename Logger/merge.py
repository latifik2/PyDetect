import sys
import re

def write_from_file(filename):
    with open(filename, 'r') as reader:
        text = reader.read()
        with open("debug/debug.py", 'a') as writer:
            writer.write('\r\n')
            writer.write(text)

if __name__ == "__main__":
      
    if (len(sys.argv) < 2):
        print("Not enough arguments")
        exit(1)
    module_name = sys.argv[1]

    # print(module_name)
    pattern = r'sys.meta_path|exec|eval|compile'
    with open(module_name, 'r') as file:
        mw_code = file.read()
        result = re.findall(pattern, mw_code)

    if len(result) > 0:
        print("Merging files")
        write_from_file("hook.py")
        write_from_file(module_name)
    else:
        print("No pattern found")