#!/usr/bin/python3
"""
0-main
"""
import sys
import importlib.util

if __name__ == '__main__':
    # Load the 0-subs module dynamically
    module_name = '0-subs'
    module_path = f'{module_name}.py'

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    number_of_subscribers = module.number_of_subscribers

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print(number_of_subscribers(sys.argv[1]))
