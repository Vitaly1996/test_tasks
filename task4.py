class Employee:
    def __init__(self, id, language):
        self.id = id
        self.language = language
        self.subordinates = []


class Organization:
    def __init__(self):
        self.employees = {0: Employee(0, 'AB')}
        self.language_barriers = {}

    def add_employee(self, id, language):
        self.employees[id] = Employee(id, language)

    def add_subordinate(self, manager_id, subordinate_id):
        self.employees[manager_id].subordinates.append(self.employees[subordinate_id])

    def calculate_language_barrier(self):

        self._traverse_hierarchy(0, None)

    def _traverse_hierarchy(self, employee_id, manager_language):
        employee = self.employees[employee_id]
        if employee_id != 0:
            if manager_language == employee.language or manager_language == 'AB':
                self.language_barriers[employee_id] = 0
            else:
                self.language_barriers[employee_id] = self.language_barriers.get(employee_id, 0) + 1
        for subordinate in employee.subordinates:
            self._traverse_hierarchy(subordinate.id, employee.language)


def main():
    N = int(input())
    languages = input().split()
    hierarchy = list(map(int, input().split()))

    org = Organization()

    for i in range(1, N + 1):
        org.add_employee(i, languages[i-1])

    stack = []
    for id in hierarchy:
        if not stack or stack[-1] != id:
            if stack:
                org.add_subordinate(stack[-1], id)
            stack.append(id)
        else:
            stack.pop()

    org.calculate_language_barrier()

    barriers = [org.language_barriers[i] for i in range(1, N + 1)]
    print(' '.join(map(str, barriers)))


if __name__ == "__main__":
    main()
