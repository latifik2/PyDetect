from datetime import datetime


saved_exec = exec
saved_compile = compile
saved_eval = eval

def decode_code(code):
    if type(code) is bytes:
        return code.decode()
    return code

def write_logs(code, source: str, filename: str = None):
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    log = f"[!] {time} {source} ==> {decode_code(code)}"
    if filename is not None:
        log += f" Trying to read data from file! Path: {filename}"

    with open("logs.txt", 'a') as file:
        file.write(log + '\n')

def debug_exec(code, globals=None, locals=None, closure=None):
    write_logs(code, 'EXEC')
    return saved_exec(code, globals, locals, closure)

def debug_compile(code, file, mode, flag: int = 0, dont_inherit: bool = False, optimize: int = -1):
    write_logs(code, 'COMPILE', file)
    return saved_compile(code, file, mode, flag, dont_inherit, optimize)
    
    
def debug_eval(code, globals=None, locals=None):
    write_logs(code, 'EVAL')
    return saved_eval(code, globals, locals)

exec = debug_exec
eval = debug_eval
compile = debug_compile