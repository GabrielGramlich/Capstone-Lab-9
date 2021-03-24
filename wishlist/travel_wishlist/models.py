from django.db import models

class Place(models.Model):
	name = models.CharField(max_length=111)	#Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu, Hawke's Bay, New Zealand is 111 characters. Shouldn't ever need more characters than that.
	visited = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.name}, visited? {self.visited}'
