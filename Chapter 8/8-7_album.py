def make_album(album_title,author_name,song_no=None):
    if song_no:
        album = {"author's name" : author_name.title(),
             'album title' : album_title.title(),
             'number of songs' : song_no 
            }
    else:
        album = {"author's name" : author_name.title(),
                'album title' : album_title.title()  
            }
    return album
print(make_album('aashiqui 2','irshad kamil'))
print(make_album('ae dil hai mushkil', 'amitabh bhattacharya'))
print(make_album('dilwale', 'amitabh bhattacharya'))
print(make_album('kal ho na ho', 'javed akhtar', 20))