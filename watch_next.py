# A program to see which movie is most similar using spacy

import spacy


# Creating function with fitting name
def movie_recommendation():
    nlp = spacy.load("en_core_web_md")

# Opening the file and reading as a list
    with open("movies.txt","r") as movie_list:
        movies = movie_list.readlines()
    
# The movie we want to compare
    planet_hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
                the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the
                hulk can live in peace. Unfortunatley Hulk lands on the planet Sakaar where he is sold
                into slaverey and trained as a gladiator.'''

# Converting movie to be able to use nlp
    hulk_score = nlp(planet_hulk)

# Creating empty list to record the different scores - looping through the list to find and compare with
# Planet Hulk
    similarity_scores = []
    for i in movies: 
        similarity = nlp(i).similarity(hulk_score)
        similarity_scores.append(similarity)
   
    
# Finding the highest score along with the first two words of the item in the list 
    highest_score = max(similarity_scores)
    top_scorer = similarity_scores.index(highest_score)
    rec_movie = movies[top_scorer].strip()
    movie_title = ' '.join(rec_movie.split()[:2]) 
    return movie_title


# Calling back on the function and printing a prompt along with the answer needed.

recommended = movie_recommendation()

print("Because you liked 'Planet Hulk', we recommend: " + recommended)







