{
    'name': 'Todo List',
    'version': '1.0',
    'summary': 'Todo List Management for Internal Users',
    'category': 'Productivity',
    'author': 'QKS',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/tags_data.xml',
        'views/todo_list_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}