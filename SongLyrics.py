class Song(object):

    def __init__(self, lyrics, title, artist, producer, feature):
        self.lyrics = lyrics
        self.title = title
        self.artist = artist
        self.producer = producer
        self.feature = feature

    def sing_me_a_song(self):
        print self.title + " By " + self.artist
        print "Produced By " + self.producer
        for line in self.lyrics:
            print line
        # for line in self.title:
        #     print line
        # for line in self.artist:
        #     print line
# happy_bday = Song(["Happy birthday to you",
#                    "These lyrics are copywrighted",
#                    "So I'll stop here"])

hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah",], "Hotline Bling", "Drake") #add the producer
# This is your daily reminder that Drake is Canadian
#
# two_phones= Song (["Think I need two more, "
#                    "line bumpin' I'm ring, ring, ringin" ])

# happy_bday.sing_me_a_song()
hotline_bling.sing_me_a_song()
