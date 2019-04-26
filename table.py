from flask_table import Table, Col, LinkCol
 
class philMed(Table):
    id = Col('Id', show=False)
    date_posted = Col('date')
    title = Col('title')
    upset = Col('Upset')
    anxious = Col('Anxious')
    excited = Col('Excited')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))