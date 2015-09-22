import media
import python_to_html

three_idiots = media.Movie("3 Idiots",
                        "A story of a boy and his toys that come to life",
                        "http://www.media.glamsham.com/download/poster/images/3_idiots/3-idiots-02.jpg",
                        "http://www.youtube.com/watch?v=K0eDlFX9GMc")
kick = media.Movie("Kick",
                   "A movie that shows helping others gives the bigest joy in life",
                   "http://kickmoviedownload.com/wp-content/uploads/2014/07/salman-Kick-movie-poster.jpg",
                   "http://www.youtube.com/watch?v=JJnG3yW-M-M")


ghajini= media.Movie("Ghajini",
                   "Romantic Action Movie",
                   "http://upload.wikimedia.org/wikipedia/en/9/97/Ghajini_Hindi.jpg",
                   "http://www.youtube.com/watch?v=M9rtexMuYVc")

ek_tha_tiger = media.Movie("Ek Tha Tiger",
                           "Romantic Action Movie",
                           "http://www.imuae.com/vb/imgcache2/342089.gif",
                           "http://www.youtube.com/watch?v=x1thrb5MFjI")

taree_zammen_par = media.Movie("Tarre Zammen Par",
                               "A movie about a normal kid and his teacher",
                               "http://upload.wikimedia.org/wikipedia/en/b/bd/TaareZameenPar.jpg",
                               "http://www.youtube.com/watch?v=F-PAI2HnQUo")


ready = media.Movie("Ready",
                    "Comedy Action Movie",
                    "http://up.downloadoh.ir/up/downloadoh/Pictures/21333.jpg",
                    "http://www.youtube.com/watch?v=6ib1KUNMZAw")


movies = [three_idiots,kick,ghajini,ek_tha_tiger, taree_zammen_par,ready]
python_to_html.open_movies_page(movies)
