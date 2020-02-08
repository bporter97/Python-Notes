# Python provides a mechanism for the serialization of objects called pickle
# When an object is 'pickeled' its written to a file in a format that contains the object's
# data together with significant information that allows the object to be recreated
# when loaded back in.

import pickle
import webbrowser


imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the rug'),
           (2, 'Pyscho'),
           (3, 'Mayhem'),
           (4, "kentish Town Waltz")))

with open("imelda.pickle", 'wb') as pickle_file:  # writing to file
    pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as imelda_pickled:   # reading file back in to program
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)               # Printing  out data

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)



# Pickles must be read back into the program in the same order they were
# introduced in

webbrowser.open('https://docs.python.org/3/library/pickle.html')