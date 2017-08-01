import media  #This file contains the class Movie
import fresh_tomatoes  #File provided by Udacity.

"""
This file contains objects of Class Movie from the media file

Each instance contains the title, summary, poster image, and trailer
URL for each movie. They are then added to a list to be used on the
webpage. Webpage information is within the fresh_tomatoes file
provided by Udacity during the course
"""

princess_bride = media.Movie("The Princess Bride",
                             "A farmhand rescues his true love",
                             "http://www.princessbridetweasure.com/images/products/detail/PB1208.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=mtj_Ix5IUo8")

spirited_away = media.Movie("Spirited Away",
                            ("Young girl wanders into a world of spirits "
                            "during her family's vacation"),
                            "http://img.moviepostershop.com/spirited-away-movie-poster-2002-1010407965.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=gOSP8sm_NoQ")

dark_knight = media.Movie("The Dark Knight",
                          "Batman defends Gotham from the Joker",
                          "https://www.movieposter.com/posters/archive/main/69/MPW-34756",  # NOQA
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

how_to_train_your_dragon = media.Movie("How to Train Your Dragon",
                                       ("A young viking teaches others to "
                                       "train dragons rather than fight them"),
                                       "https://fanart.tv/fanart/movies/10191/movieposter/how-to-train-your-dragon-52e51aa59235b.jpg",  #NOQA
                                       "https://www.youtube.com/watch?v=oKiYuIsPxYk")  # NOQA

wreck_it_ralph = media.Movie("Wreck it Ralph",
                             ("A video game villain decides he no longer wants "
                             "to be the bad guy"),
                             "http://www.comicconfamily.com/wp-content/uploads/2012/09/WIR_Ralph_BS_v5.0_Online1.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=87E6N7ToCxs")

scott_pilgrim = media.Movie("Scott Pilgrim Vs. the World",
                            ("To win Ramona's love, Scott Pilgrim must face "
                            "her seven evil exes"),
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwNTczNTMyOF5BMl5BanBnXkFtZTcwNzUxOTUyMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=7wd5KEaOtm4")


#movies is the list of movies we want to appear on our website
movies = [princess_bride, spirited_away, dark_knight, how_to_train_your_dragon,
          wreck_it_ralph, scott_pilgrim]
#fresh_tomatoes contains the html necessary for creating the webpage
fresh_tomatoes.open_movies_page(movies)
