#!usr/bin/env python
#-*- coding: utf-8 -*-

students = list()

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])

scores = sorted( list( set( [x[1] for x in students] ) ) )
students.sort(key=lambda x: x[1])
second_lower_grade = scores[1]
output_students = filter(lambda x: x[1] == second_lower_grade, students)
output_students.sort(key=lambda x: x[0])
for x in output_students:
    print x[0]