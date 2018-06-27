import spacy
nlp = spacy.load('en')

videos = {
    "beach" : {
        "file_name": "beach.mpg",
        "desc"     : "Gentle waves rolling up a sandy beach while sea birds fly in the sky"
    },

    "ocean" : {
        "file_name" : "ocean.mpg",
        "desc"      : "Tropical fishes swimming in the coral with sunlight shimmering in the ocean water"
    }
}

def similarity (phrase):
    highest_weight = 0

    # look through the videos dict and find highest similarity
    for video in videos:
        doc1 = nlp(phrase)
        doc2 = nlp(videos[video]["desc"])
        similarity_weight = doc1.similarity(doc2)
        if similarity_weight > highest_weight:
            highest_weight = similarity_weight
            return_video = videos[video]["file_name"]

    print('highest similarity is', highest_weight, 'play', return_video)
    return return_video