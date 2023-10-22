def make_album(artist_name, album_title, songs=None):
    album = {'name': artist_name, 'album': album_title}
    if songs:
        album['number of tracks'] = songs
    return album


albumdb01 = {}
albumdb02 = {}
albumdb03 = {}

albumdb01 = make_album('machine head', 'the blackening')
albumdb02 = make_album('black sabbath', 'heaven and hell', '15')
albumdb03 = make_album('born of osiris', 'angel or alien')

print(albumdb01)
print(albumdb02)
print(albumdb03)

##################################################################################
# Answer:

# def make_album(artist, title, tracks=0):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#         }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict

# album = make_album('metallica', 'ride the lightning')
# print(album)

# album = make_album('beethoven', 'ninth symphony')
# print(album)

# album = make_album('willie nelson', 'red-headed stranger')
# print(album)

# album = make_album('iron maiden', 'piece of mind', tracks=8)
# print(album)
