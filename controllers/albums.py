from flask import *

albums = Blueprint('albums', __name__, template_folder='templates')

@albums.route('/albums/edit')
def albums_edit_route():
	options = {
		"edit": True
	}
	return render_template("albums.html", **options)
	# return redirect(url_for('album.album_edit_route', username=spacejunkie'))


@albums.route('/albums')
def albums_route(username=None):
	options = {
		"username": "vvhgtyg",
	}
	# return render_template("albums.html", **options)
	return render_template("albums.html", username)
