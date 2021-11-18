# t = "a", "b", "c"
# print(t)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)

for album in albums:
    name, artist, year = album
    print("album: {}, artist: {}, year: {}".format(name, artist, year))

for name, year, album in albums:
    print("album: {}, artist: {}, year: {}".format(name, artist, year))