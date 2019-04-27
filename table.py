from flask_table import Table, Col
 
class philMed(Table):
    id = Col('Id', show=False)
    date_posted = Col('Date and Time')
    title = Col('Title')
    anxious = Col('Anxious')
    upset = Col('Upset')
    excited = Col('Excited')



    