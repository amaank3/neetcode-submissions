from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # BRUTE FORCE SOLUTION 

        # Circular sandwiches -> 0
        # Square sandwiches -> 1

        # Student prefers sandwich on top -> remove from stack
        # Student doesnt prefer sandwich -> dequeue and then enqueue

        # students_queue = deque(students)

        # rejected = 0

        # while students_queue and sandwiches:

        #     if students_queue[0] == sandwiches[0]:
        #         students_queue.popleft()
        #         sandwiches.pop(0)

        #         # Someone ate, so reset rejection count
        #         rejected = 0

        #     else:
        #         student_preference = students_queue.popleft()
        #         students_queue.append(student_preference)

        #         rejected += 1

        #         # Everyone remaining rejected this sandwich
        #         if rejected == len(students_queue):
        #             break

        # return len(students_queue)


        # OPTIMAL SOLUTION

        num_students = len(students)
        preferences = Counter(students)

        for sandwich in sandwiches:
            if preferences[sandwich] > 0:
                num_students -= 1
                preferences[sandwich] -= 1

            else:
                return num_students

        return num_students
                


        