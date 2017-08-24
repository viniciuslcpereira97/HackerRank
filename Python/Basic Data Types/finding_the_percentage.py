#!usr/bin/env python
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    student_info = student_marks[query_name]
    print "{0:.2f}".format(sum(student_info) / len(student_info))
