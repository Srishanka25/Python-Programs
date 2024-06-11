class Solution:
    def countStudents(self, students, sandwiches):
        stdcount = len(students)
        while  sandwiches and students and students[0] in students:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
                stdcount -= 1
        return  stdcount

