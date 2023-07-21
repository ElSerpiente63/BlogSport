import ast

# Chemin vers le fichier à analyser
fichier = 'C:/Users/33769/AppData/Local/Programs/Python/Python310/lib/site-packages/flet/colors.py'

# Analyse du code source du fichier
with open(fichier, 'r') as file:
    tree = ast.parse(file.read())

# Récupération des noms des variables
variables = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)]

print(variables.index("RED"))
# Affichage des noms des variables
print(variables)