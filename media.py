
import webbrowser

class Movie():
	''' 
	behavior: This class provides a way to store movie related information
	input: self, movie title, storyline, poster image, youtube trailer, ratings, and director
	output: any of the stored inputs if called.
	 '''
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_ratings, directed_by):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.ratings = movie_ratings
		self.director = directed_by


	def show_trailer(self):
		'''
		behavior: this function is used to open a webbrowser and view a trailer
		input: takes in self
		output: opens youtube trailer url 
		'''
		webbrowser.open(self.trailer_youtube_url)