def make_album(artist_name, album_title, songs=None):
    album = {'name': artist_name, 'album': album_title}
    if songs:
        album['number of tracks'] = songs
    return album


while True:
    art_name = input("\nArtist name: ")
    if art_name == 'q':
        break
    alb_title = input("\nAlbum name: ")
    if alb_title == 'q':
        break

    album = {}

    album = make_album(art_name, alb_title)
    print(album)

#########################################################################
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

# # Prepare the prompts.
# title_prompt = "\nWhat album are you thinking of? "
# artist_prompt = "Who's the artist? "

# # Let the user know how to quit.
# print("Enter 'quit' at any time to stop.")

# while True:
#     title = input(title_prompt)
#     if title == 'quit':
#         break

#     artist = input(artist_prompt)
#     if artist == 'quit':
#         break

#     album = make_album(artist, title)
#     print(album)

# print("\nThanks for responding!")
