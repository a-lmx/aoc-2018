# https://adventofcode.com/2018/day/7

import sys

class Step:
    def __init__(self, label):
        self.label = label
        self.deps = set()
        self.required_by = set()
    
    def __str__(self):
        return f'Step {self.label} requires {self.deps}, is required by {self.required_by}'
    
    def __repr__(self):
        return f'deps: {self.deps}, required_by: {self.required_by}'

class InstructionSet:
    def __init__(self):
        self.steps = {}
        self.available = set()
        self.step_order = []
    
    def __str__(self):
        return f'Steps: {self.steps}'

    def build_dep_tree(self, filename):
        lines = open(filename).readlines()
        for line in lines:
            words = line.split(' ')
            dep = words[1]
            step = words[7]
            if step in self.steps:
                self.steps[step].deps.add(dep)
            else:
                new_step = Step(step)
                new_step.deps.add(dep)
                self.steps[step] = new_step
            if dep in self.steps:
                self.steps[dep].required_by.add(step)
            else:
                new_dep = Step(dep)
                new_dep.required_by.add(step)
                self.steps[dep] = new_dep


def main(filename):
    instructions = InstructionSet()
    instructions.build_dep_tree(filename)
    print(instructions)


main(sys.argv[1])
