from graphviz import Digraph

# Створення графу
dialog_diagram = Digraph('Dialog Diagram', format='png')
dialog_diagram.attr(rankdir='LR')  # Горизонтальне розташування

# Додавання вузлів
dialog_diagram.node('Seller', 'Продавець', shape='box', style='rounded,filled', fillcolor='lightblue')
dialog_diagram.node('System', 'Система аукціону', shape='ellipse', style='filled', fillcolor='lightgreen')
dialog_diagram.node('Buyer', 'Покупець', shape='box', style='rounded,filled', fillcolor='lightyellow')

# Зв’язки між вузлами
dialog_diagram.edge('Seller', 'System', 'Запит на створення лоту')
dialog_diagram.edge('Buyer', 'System', 'Ставка')
dialog_diagram.edge('System', 'Buyer', 'Підтвердження ставки')
dialog_diagram.edge('System', 'Seller', 'Результати аукціону')

# Рендеринг
dialog_diagram.render('dialog_diagram')
print("Діаграма діалогів створена!")
