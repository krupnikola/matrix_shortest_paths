import sys
from path_finder import PathFinder
import os


def main():

    try:
        map = sys.argv[1]
    except IndexError:
        print("First argument must be the path to the .xml file!")
    else:
        data = PathFinder.get_shortest_paths(map)

        try:
            result_file = sys.argv[2]
            with open(result_file, 'w+') as res:
                res.write(str(data))
            print('Path to the results file:', os.path.abspath(result_file))
        except IndexError:
                    pass
                    print(data)


if __name__ == '__main__':
    main()
















