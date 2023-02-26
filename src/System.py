import platform, psutil

my_sys = platform.uname()

def displaySpecification():
    print(f"System: \t{my_sys.system}")
    print(f"Node name: \t{my_sys.node}")
    print(f"Version: \t{my_sys.version}")
    print(f"Machine: \t{my_sys.machine}")
    print(f"Processor: \t{my_sys.processor}")
    print(f"Memory: \t{str(round(psutil.virtual_memory().total / (1024.0 ** 3)))} GB")