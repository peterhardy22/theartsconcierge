from flask_table import Table, Col, BoolCol, LinkCol


class Results(Table):
    id = Col('Id', show=False)
    artist = Col('Artist')
    title = Col('Title')
    medium = Col('Medium')
    dimensions = Col('Dimensions')
    image = Col('Image')
    location = Col('Location')
    city = Col('City')
    country = Col('Country')
    latitude = Col('Latitude')
    longitude = Col('Longitude')
    on_view = BoolCol('On View')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))
