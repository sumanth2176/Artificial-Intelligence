print("Map Colouring")
class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
    def is_consistent(self, variable, assignment):
        for constraint in self.constraints.get(variable, []):
            if constraint[0] in assignment and assignment[variable] == constraint[1]:
                return False
        return True
    def solve(self):
        return self.backtrack({})
    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        unassigned_vars = [var for var in self.variables if var not in assignment]
        current_var = unassigned_vars[0]
        for value in self.domains[current_var]:
            if self.is_consistent(current_var, {**assignment, **{current_var: value}}):
                assignment[current_var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[current_var]
        return None
if __name__ == "__main__":
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue'],
        'Q': ['red', 'green', 'blue'],
        'NSW': ['red', 'green', 'blue'],
        'V': ['red', 'green', 'blue'],
        'T': ['red', 'green', 'blue']
    }
    constraints = {
        'WA': [('NT', '!=')],
        'NT': [('WA', '!='), ('SA', '!=')],
        'SA': [('NT', '!='), ('WA', '!='), ('Q', '!=')],
        'Q': [('SA', '!='), ('NSW', '!=')],
        'NSW': [('Q', '!='), ('SA', '!='), ('V', '!=')],
        'V': [('NSW', '!='), ('SA', '!=')],
    }
    csp = MapColoringCSP(variables, domains, constraints)
    solution = csp.solve()
    if solution is not None:
        print("Solution found:")
        for var, color in solution.items():
            print(f"{var}: {color}")
    else:
        print("No solution found.")