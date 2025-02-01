from src.framework.infra.core import Core


# this is an idiom in python and a default practice. this ensures that the script is only executed
# when run directly and not when imported as a module in another script. purpose is to help keep the
# script modular and prevent code from running when imported elsewhere
# __name__ builtin variable, represents the script or module
# `if __name__ conditional '__main__':`, represents whether this is executed as a script or module
if __name__ == '__main__':
    print(r'Data Driven Tree : User Acquisition Campaign')
    Core()
