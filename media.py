import webbrowser  #Necessary to open the movie trailer

class Movie():
    """ This class provides a way to store movie related information

    Attributes:
        movie_title(str): Title of the movie
        story_line(str): Basic movie synopsis
        poster_image_url(str): URL for movie poster or box art
        trailer_youtube_url(str): URL for movie trailer on youtube
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        
    def show_trailer(self):  #This function is what will play the trailers
        webbrowser.open(self.trailer_youtube_url)

