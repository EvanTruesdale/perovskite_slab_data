import numpy as np
import regex

record = False
lines = []
energy = 0
with open('example', 'r') as f:
    for line in f:
        if '!' in line:
            energy = [float(s) for s in regex.findall(r'-?\d+\.?\d*', line)][0]
        if 'Begin final coordinates' in line:
            record = True
        elif 'End final coordinates' in line:
            record = False

        if record == True:
            lines.append(line.rstrip())
cell_parameters = '\n'.join([line.replace('\t', ' ') for line in lines[5:8]])
atom_positions = lines[10:]
temp_atom_positions = []
atoms = dict()
for line in atom_positions:
    line = line.split()
    atoms[line[0]] = atoms.get(line[0], 0) + 1
    line = [line[1], line[2], line[3], line[0]]
    temp_atom_positions.append(' '.join(line))
atom_positions = '\n'.join(temp_atom_positions)
atom_types = ' '.join(list(atoms.keys()))
atom_numbers = ' '.join([str(int) for int in list(atoms.values())])
text = """Ba1 Ti1 O3
1.0
{_cell_parameters}
{_atom_types}
{_atom_numbers}
direct
{_atom_positions}""".format(_cell_parameters=cell_parameters, _atom_types=atom_types, _atom_numbers=atom_numbers, _atom_positions=atom_positions)
print(text)
