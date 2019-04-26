from flask_table import Table, Col
 
class philMed(Table):
    id = Col('Id', show=False)
    date_posted = Col('date')
    title = Col('Artist')
    upset = Col('Title')
    anxious = Col('Release Date')
    excited = Col('Publisher')