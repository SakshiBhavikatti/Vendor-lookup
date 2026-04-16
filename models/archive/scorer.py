from sklearn.metrics.pairwise import cosine_similarity

def get_top_candidates(query_vector, matrix, top_n=50):
    scores = cosine_similarity(query_vector, matrix).flatten()
    indices = scores.argsort()[-top_n:][::-1]
    return indices, scores