from rapidfuzz import fuzz

class FuzzyModel:
    @staticmethod
    def score(query, candidate):
        token = fuzz.token_sort_ratio(query, candidate)
        partial = fuzz.partial_ratio(query, candidate)
        wratio = fuzz.WRatio(query, candidate)

        final_score = (token * 0.3) + (partial * 0.2) + (wratio * 0.5)
        return round(final_score, 2)