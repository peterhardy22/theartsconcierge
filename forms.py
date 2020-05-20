from wtforms import Form, StringField, SelectField, BooleanField


class ArtworkSearchForm(Form):
    choices = [('Artist Name', 'Artist Name'),
               ('Title', 'Title'),
               ('Location', 'Location')]
    select = SelectField('Search for art:', choices=choices)
    search = StringField('')


class ArtworkForm(Form):
    medium_types = [('Painting', 'Painting'),
                    ('Sculpture', 'Sculpture'),
                    ('Drawing', 'Drawing'),
                    ('Photograph', 'Photograph'),
                    ('Mixed Media', 'Mixed Media')
                    ]
    artist = StringField('Artist')
    title = StringField('Title')
    medium = StringField('Medium')
    dimensions = StringField('Dimensions')
    image = StringField('Image')
    location = StringField('Location')
    city = StringField('City')
    country = StringField('Country')
    on_view = BooleanField('On View')
