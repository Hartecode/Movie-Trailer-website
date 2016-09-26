import random, fresh_tomatoes, media, urllib2, json

#The api is from The movie DB https://www.themoviedb.org
api_key = '9431087c3ac616334461df8fb870ccc0'

#function generates a random number
def ran_num():
    return random.randrange(2000)

#tTakes in a id and purdoces a url to query the movie info
def movie_info(movieid):
    movieurl = "http://api.themoviedb.org/3/movie/%d?api_key=%s&append_to_response=videos"
    query = movieurl%(movieid,api_key)
    return query

# Takes in the movei_info() function and generates the json dictionary of movie info
def fullquery(movieid):
    url = movie_info(movieid)
    try:
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        return data
    except urllib2.HTTPError, e:
        print movieid
        print e.code
        print e.msg
        return

#Takes in data and generates poster url.
def poster(data):
    imgurl = "https://image.tmdb.org/t/p/w500%s"
    poster_path = data["poster_path"]
    pic_url = imgurl%(poster_path)
    return pic_url

#Takes in data and generates trailer url.
def trailer(data):
    try:
        vidoekey = data["videos"]["results"][0]["key"]
        youtubeurl ="https://www.youtube.com/watch?v=%s"
        url = youtubeurl%(vidoekey)
        return url
    except:
        print "traioler error"
        return

#Takes in the movie id and then returns the title, movie details, poster url, and trailer url.
def moviedetails(movieid):
    data = fullquery(movieid)
    title = data["original_title"]
    description = data["overview"]
    poster_url = poster(data)
    trailer_url = trailer(data)
    return media.Movie(title, description, poster_url, trailer_url)



movie_1 = moviedetails(14)
movie_2 = moviedetails(505)
movie_3 = moviedetails(20)
movie_4 = moviedetails(13)
movie_5 = moviedetails(200)
movie_6 = moviedetails(168)
movie_7 = moviedetails(8)
movie_8 = moviedetails(168)
movie_9 = moviedetails(98)
movie_10 = moviedetails(16)
movie_11 = moviedetails(18)
movie_12 = moviedetails(12)
movie_13 = moviedetails(109)
movie_14 = moviedetails(55)
movie_15 = moviedetails(98)
movie_16 = moviedetails(65)
movie_17 = moviedetails(114)
movie_18 = moviedetails(82)
movie_19 = moviedetails(166)
movie_20 = moviedetails(170)
movie_21 = moviedetails(136)


movies = [movie_1, movie_2, movie_3, movie_4,movie_5,
          movie_6, movie_7, movie_8, movie_9, movie_10,
          movie_11, movie_12, movie_13, movie_14, movie_15,
          movie_16, movie_17, movie_18, movie_19,movie_20, movie_21]



fresh_tomatoes.open_movies_page(movies)
