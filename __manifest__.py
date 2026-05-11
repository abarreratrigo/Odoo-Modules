{
    'name': 'Rother',
    'version': '18.0-20250930',
    'category':'Inventory',
    'summary':'Módulo de productos de Rother',
    'author':'Rother Industries & Technologies',
    'depends':['product', 'stock', 'purchase', 'sale'],
    'data':[
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'report/report.xml',
        'report/report_template.xml'
    ],
    'installable': True,
    'application': True
}