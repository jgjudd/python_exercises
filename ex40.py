class Song(object):

	def _init_(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy bday to you","i dont want to get sued","so i'll stop you right there."])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()