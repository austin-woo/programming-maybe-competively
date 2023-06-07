class SATSolver:
    def __init__(self):
        self.clauses = []
        self.assignment = []

    def load_cnf_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('c'):
                    continue
                elif line.startswith('p'):
                    _, _, num_vars, _ = line.split()
                    self.assignment = [None] * int(num_vars)
                else:
                    clause = [int(x) for x in line.split() if int(x) != 0]
                    self.clauses.append(clause)

    def solve(self):
        return self._backtrack(0)

    def _backtrack(self, index):
        if index == len(self.assignment):
            return True

        self.assignment[index] = True
        if self._is_consistent(index) and self._backtrack(index + 1):
            return True

        self.assignment[index] = False
        if self._is_consistent(index) and self._backtrack(index + 1):
            return True

        return False

    def _is_consistent(self, index):
        for clause in self.clauses:
            clause_satisfied = False
            for literal in clause:
                var = abs(literal) - 1
                value = self.assignment[var]
                if (literal < 0 and not value) or (literal > 0 and value):
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                return False
        return True

solver = SATSolver()
solver.load_cnf_file('example.cnf')
if solver.solve():
    output_filename = 'output.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write("Satisfiable\n")
        for i, value in enumerate(solver.assignment):
            output_file.write(f"Variable {i + 1}: {value}\n")
else:
    print("Unsatisfiable")
