#find s where is_path(s, A, B) and no_nodes(s, t) and total_weight(s, u) and t=C and u<D

from graph_functions import *
import csv
import sys

if(len(sys.argv) != 2):
    print('Invalid Input. Please use the following input style :\n')
    print('python', sys.argv[0], '[FILENAME].csv')
    exit()
try:
    if(sys.argv[1][-4:] != '.csv'):
        print('Invalid Filetype. Please use the following input style :\n')
        print('python', sys.argv[0], '[FILENAME].csv')
        exit()
    csv_filename = sys.argv[1]
except:
    print('Invalid Input. Please use the following input style :\n')
    print('python', sys.argv[0], '[FILENAME].csv')
    exit()

print('Find s where is_path(s, A, B), no_nodes(s, C), and total_weight(s, u) where u<D')
A = int(input('Input value for A : '))
B = int(input('Input value for B : '))
C = int(input('Input value for C : '))
D = float(input('Input value for D : '))

all_edges = []
with open(csv_filename) as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    for row in read_csv:
        all_edges.append([int(row[0]),int(row[1]),float(row[2])])
        all_edges.append([int(row[1]),int(row[0]),float(row[2])])

path_results = find_paths(all_edges, A, B, C, D)

if(len(path_results) != 0):
    path_count = 1
    for path in path_results:
        print('Path', path_count)
        for edge in path:
            print(edge[0],edge[1],sep=',')
        path_count += 1
else:
    print('No Possible Paths')
