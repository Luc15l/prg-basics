# class definition
class Song:
   def __init__(self,wykonawca,tytul,album,rok):
      self.wykonawca = wykonawca
      self.tytul = tytul
      self.album = album
      self.rok = rok
   def __str__(self):
      return f'{self.wykonawca} {self.tytul} {self.album} {self.rok}'

# object creation
song1 = Song('Republika', 'Odchodząc', 'masakra', 1998)

song2 = Song('Myslovitz', 'Maj', 'Myslovitz', 1995)

## object usage

print(song1)
print(song2)