import fresh_tomatoes
import media

toy_story = media.Movie(
	"Toy Story",
 	"Imagination runs rampant when toys become mobile when not watched. \
   Two toys, Woody and Buzz Lightyear despise each other like no other. \
   But, when the toys are separated from their home, a truce is formed \
   between them all in an effort to journey home.",
	"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4",
	"Rated G",
	"Directed by: John Lasseter"
)

avatar = media.Movie(
	"Avatar",
	"In the future, Jake, a paraplegic war veteran, is brought to a moon, \
   Pandora, which is inhabited by the Na'vi, a humanoid race with their own \
   language and culture. Those from Earth find themselves at odds with each \
   other and the local culture.",
	"https://www.movieposter.com/posters/archive/main/98/MPW-49246",
	"http://www.youtube.com/watch?v=-9ceBgWV8io",
	"Rated PG 13",
	"Directed by: James Cameron"
)

fear_and_loathing = media.Movie(
	"Fear and Loathing",
	"An adaptation of Hunter S. Thompson's novel of the same name. fueled by \
   the massive amount of drugs they purchased with an advance from a magazine \
   to cover a sporting event in Vegas; they set out in a red convertable.\
   Encountering police, reporters, gamblers, racers, and hitchhikers; \
   they search for some undefinable thing know only as the \"American Dream\" \
   and find fear, loathing and hilarious adventures into the dementia\
   of the modern American West.",
	"http://www.impawards.com/1998/posters/fear_and_loathing_in_las_vegas.jpg",
	"https://www.youtube.com/watch?v=8m662obIvhY",
	"Rated R",
	"Directed by: Terry Gilliam"
)

minions = media.Movie(
	"Minions",
	"Evolving from single-celled yellow organisms at the dawn of time, \
   Minions live to serve, but find themselves working for a continual \
   series of unsuccessful masters, from T. Rex to Napoleon. Without a master\
   to grovel for, the Minions fall into a deep depression. But one minion, \
   Kevin, has a plan; accompanied by his pals Stuart and Bob, Kevin sets \
   forth to find a new evil boss for his brethren to follow. Their search \
   leads them to Scarlet Overkill, the world's first-ever super-villainess.",
	"http://www.impawards.com/2015/posters/minions.jpg",
    "https://www.youtube.com/watch?v=eisKxhjBnZ0",
	"Rated PG",
	"Directed by: Pierre Coffin and Kyle Balda"
)

good_fellas = media.Movie(
	"Goodfellas",
    "A young man grows up in the mob and works very hard to advance himself\
   through the ranks. He enjoys his life of money and luxury, \
   but is oblivious to the horror that he causes. \
   A drug addiction and a few mistakes ultimately unravel his\
   climb to the top. Based on the book \"Wiseguy\" by Nicholas Pileggi",
	"https://images-na.ssl-images-amazon.com/images/I/51rOnIjLqzL.jpg",
	"https://www.youtube.com/watch?v=2ilzidi_J8Q",
	"Rated R",
	"Directed by: Martin Scorsese"
)

fight_club = media.Movie(
	"Fight Club",
	"A depressed man (Edward Norton) suffering from insomnia meets a\
   strange soap salesman named Tyler Durden (Brad Pitt) and soon finds \
   himself living in his squalid house after his perfect apartment is\
   destroyed. The two bored men form an underground club with strict \
   rules and fight other men who are fed up with their mundane lives.\
   Their perfect partnership frays when Marla (Helena Bonham Carter),\
   a fellow support group crasher, attracts Tyler's attention",
	"http://www.posterbobs.com/images/fight_club3.jpg",
	"https://www.youtube.com/watch?v=_XgQA9Ab0Gw",
	"Rated R",
	"Directed by: David Fincher"
)


movies = [toy_story, avatar, fear_and_loathing, minions, good_fellas, fight_club]  
fresh_tomatoes.open_movies_page(movies) 