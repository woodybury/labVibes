import spacy
nlp = spacy.load('en')
# test woods branch
videos = {
    "beach" : {
        "file_name": "beach.mp4",
        "desc"     : "Gentle waves rolling up a sandy beach while sea birds fly in the sky"
    },

    "ocean" : {
        "file_name" : "ocean.mp4",
        "desc"      : "Tropical fishes swimming in the coral with sunlight shimmering in the ocean water"
    },

    "fire" : {
        "file_name" : "fire.mp4",
        "desc"      : "Crackling campfire at dusk in the snowy mountains with river and wind"

    },
    "Symphony" : {
        "file_name" : "Symphony.mp4",
        "desc"      : "Live symphony insturmental performance Pachelbel's canon with violins, cellos and other musical insturments"
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
