# A program to use NLP and NER on garden path sentences. 

# Importing spacy
import spacy 

# Loadiing english language model
nlp = spacy.load('en_core_web_sm')

gardenpathsentences = ["The complex houses married and single soliders in thier families", 
                       "The horse raced past the barn fell",
                       "Mary gave the child a Band-Aid",
                       "That Jill is never here hurts",
                       "The cotton clothing is made of grows in Mississippi"]


# Assigning each sentence to docs and putting as NLP with a loop through gardenpathsentences
docs = [nlp(sentences) for sentences in gardenpathsentences]

# Looping through the list now known as docs, using the orth funtions to tokenise
for doc in docs:
    print([token.orth_ for token in doc])

# Same process as before but with a different name for NER
nlp_gardenpathsentences = [nlp(paths) for paths in gardenpathsentences]

# Looping through the list to perform NER on each sentence
for path in nlp_gardenpathsentences:
    print([(i, i.label_, i.label) for i in path.ents])

# printing explanations for entities found
print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))


# A) The first entity I looked up was GPE, which by printing the explanation I can see that it identifies
# countries, cities and states. GPE stands for geopolitical entity.
# B) When you google what GPE stands for, geopolitical entity makes sense when associated with Mississippi
# as it is a state.

# A) The second entity that appeared in my case was PERSON which means people, including fictional.
# B) The entity makes sense in terms of the words assoiated with it as 'Jill' and 'Mary' are human names, 
# meaning people.