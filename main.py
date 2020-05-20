from geopy.geocoders import Nominatim

from app import app
from db_setup import init_db, db_session
from forms import ArtworkSearchForm, ArtworkForm
from flask import flash, render_template, request, redirect, jsonify
from models import Artwork, Artist, csv_importer
from tables import Results


init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = ArtworkSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search_string:
        if search.data['select'] == 'Artist Name':
            qry = db_session.query(Artwork, Artist).filter(
                Artist.id == Artwork.artist_id).filter(
                    Artist.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Title':
            qry = db_session.query(Artwork).filter(
                Artwork.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Location':
            qry = db_session.query(Artwork).filter(
                Artwork.location.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Artwork)
            results = qry.all()
    else:
        qry = db_session.query(Artwork)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_artwork', methods=['GET', 'POST'])
def new_artwork():
    form = ArtworkForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        artworks = Artwork()
        save_changes(artworks, form, new=True)
        flash('Artwork created successfully!')
        return redirect('/')

    return render_template('new_artwork.html', form=form)


def save_changes(artworks, form, new=False):
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    artist = Artist()
    artist.name = form.artist.data

    artworks.artist = artist
    artworks.title = form.title.data
    artworks.medium = form.medium.data
    artworks.dimensions = form.dimensions.data
    artworks.image = form.image.data
    artworks.location = form.location.data
    artworks.city = form.city.data
    artworks.country = form.country.data

    geolocator = Nominatim()
    location = geolocator.geocode(str(form.location.data))

    artworks.latitude = location.latitude
    artworks.longitude = location.longitude
    artworks.on_view = form.on_view.data
    if new:
        # Add the new album to the database
        db_session.add(artworks)
    # commit the data to the database
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Artwork).filter(
                Artwork.id == id)
    album = qry.first()
    if album:
        form = ArtworkForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(album, form)
            flash('Artwork updated successfully!')
            return redirect('/')
        return render_template('edit_artwork.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Artwork).filter(
        Artwork.id == id)
    album = qry.first()
    if album:
        form = ArtworkForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(album)
            db_session.commit()
            flash('Artwork deleted successfully!')
            return redirect('/')
        return render_template('delete_artwork.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


# Route for main page of bay area tracker exhibit carousels
@app.route('/bayareatracker')
def bayareatracker():
    exhibits = csv_importer()
    return render_template("bayareatracker.html", exhibits=exhibits)


# Route for Exhibits API
@app.route('/bayareatracker/api/v1/exhibits', methods=['GET'])
def get_exhibits():
    exhibits = csv_importer()
    return jsonify({'exhibits': exhibits})


if __name__ == '__main__':
    app.run()

