# #Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
def city_country(city_name, country):
    information= f"{city_name}, {country}"
    return information
x = city_country("Santiago", "Chile")
y = city_country("Nairobi", "Kenya")
z= city_country("Kampala", "Uganada")

print(x)
print(y)
print(z)

# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
def make_album (album_title, artist_name):
    album = {"artist_name": artist_name,
              "Album" : album_title}
    return album

album_1 = make_album("Mask Off", "Migos")
album_2 = make_album("We Still Don't trust You", "Future")
album_3 = make_album("Damn", "Kendrick Lamar")

print (album_1)
print (album_2)
print (album_3)

# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
def make_album (artist_name, album_title,song_number= ""):
    album = {"Artist_name": artist_name,
              "Album" : album_title}
    if song_number:
        album ["number"]= song_number 
    return album
album_1 = make_album("Mask Off", "Migos", 45)
print (album_1)


