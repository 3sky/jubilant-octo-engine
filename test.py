#!/usr/bin/python3

import requests
from tabulate import tabulate
import threading

URL: str = "https://google.com"
REQUREST_NUMBER: int = 1000
THREAD_NUMBER: int = 10


def task(request_number: int, url: str, list: list):
    n1, n2, n3, n4 = 0, 0, 0, 0
    for i in range(request_number):
        r = requests.get(url)
        header = r.headers['X-ANODEID']
        match header:
            case 'node1':
                n1 += 1
            case 'node2':
                n2 += 1
            case 'node3':
                n3 += 1
            case 'node4':
                n4 += 1

    list.append([n1, n2, n3, n4])


result = []
threads = []

intro = [['Request Number', 'Threads'], [REQUREST_NUMBER, THREAD_NUMBER]]
print(tabulate(intro, headers='firstrow', tablefmt='fancy_grid'))

for i in range(THREAD_NUMBER):
    t = threading.Thread(target=task, args=[int(REQUREST_NUMBER/THREAD_NUMBER), URL, result])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

res = [sum([row[i] for row in result]) for i in range(0, len(result[0]))]

table = [['Node 1', 'Node 2', 'Node 3', 'Node 4'], res]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
