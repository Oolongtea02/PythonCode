albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
           ("Bad Company", "Bad Company", 1974),
           ("Nightflight", "Budgie", 1981),
           ("More Mayhem", "Emilda May", 2011),
           ("Ride the Lightning", "Metallica", 1984),
           ]

print(len(albums))

album = ("Welcome to my Nightmare", "Alice Cooper", 1975)


# print(albums[0][0])
# print(albums[0][1])
# print(albums[0][2])
for name, artist, year in albums:
#for album in albums:
#    name, artist, year = album
   # name, artist, year = album[0], album[1], album[2]
#       #name, artist, year = album[0]
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

tp = ('1', '2', '3')
# nl = list(tp)
# for i in range(0, len(nl)):
#     nl[i] = str(int(nl[i]) + 3)
#    # nl[i] += 3
#    # nl[i] = str(nl[i])
nl=[]
for item in tp:
    nl.append(str(int(item) * 5))
    print("original number is {}".format(item))
print(nl)



# summary = 0
# for i in range(0, len(nl)):
#     #int(nl[i])
#     summary = summary + int(nl[i])
# nl.append(summary)
# print(nl)

summary = 0
for item in nl:
    #int(nl[i])
    summary += int(item)
nl.append(summary)
print(nl)

sum = 0
for i in range(1, 11):
    sum += i
print(sum)