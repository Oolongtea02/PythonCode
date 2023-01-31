# t = ("a", "b", "c")
# print(t)
#
# name = "Samuel"
# age = 18
# print((name, age, 'ucsc'))
# print(name, age, 'ucsc')

tp ="Ride the Lightning", "Metallica", 1984
print(tp)
print(tp[0])
print(tp[1])
print(tp[2])
print(len(tp))
# tp[0] = "abc"   # no item assignment allowed
# tp.append("abcd") # no append
tp1 = list(tp)
print(tp1)

tp1[0] = "Master of Justice"
tp1[1] = "Iron Man"
print(tp1)

# albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
#           ("Bad Company", "Bad Company", 1974),
#           ("Nightflight", "Budgie", 1981),
#           ("More Mayhem", "Emilda May", 2011),
#           ("Ride the Lightning", "Metallica", 1984),
#           ]
#
# print(len(albums))
#
# for name, artist, year in albums:
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(name, artist, year))
#
# for album in albums:
#     name, artist, year = album
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(name, artist, year))
#
