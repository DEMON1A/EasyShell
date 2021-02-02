import importlib , concurrent.futures

def Main(Script , Input):
    Import = "scripts.{0}".format(Script)
    with concurrent.futures.ThreadPoolExecutor() as Runner:
        Function = importlib.import_module(Import)
        _ = Runner.submit(Function.Run , Input)