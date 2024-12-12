import random
import os

class_names = ['Rechner', 'Kalkulator', 'Mathematik', 'Berechnung', 'ZahleRechner']
operations = ['+', '-', '*', '/', '%', '**']
var_names = ['zahl', 'nummer', 'wert', 'x', 'y']
conditions = ['!=', '>', '<', '>=', '<=', '==']

def generate_random_function():
    op = random.choice(operations)
    var1 = random.choice(var_names) + str(random.randint(1, 5))
    var2 = random.choice(var_names) + str(random.randint(1, 5))
    cond = random.choice(conditions)
    
    return f"""
    Funktion {var1}_{var2}_rechne$:TJ:
        IFFFFFFF {var1} {cond} {var2} :TJ:
            Resultat ist {var1} {op} {var2} :TJ:
            Gib Resultat zrugg :TJ:
        Elseeeeeee :TJ:
            Gib "Ungültigi Operation!" zrugg :TJ:
    $:TJ:
    """

def create_file(index):
    class_name = random.choice(class_names) + str(index)
    functions = [generate_random_function() for _ in range(random.randint(2, 5))]
    
    content = f"""Klasse {class_name}$:TJ:
    {''.join(functions)}
$:TJ:"""
    
    with open(f'generated/class_{index}.tj', 'w') as f:
        f.write(content)

# Create directory if it doesn't exist
if not os.path.exists('generated'):
    os.makedirs('generated')

# Generate 100 files
for i in range(1, 1000):
    create_file(i)