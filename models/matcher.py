from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz
from preprocess import normalize_text


class VendorMatcher:
    def __init__(self, vendor_data):
        self.vendor_data = vendor_data
        self.vendor_names = [v["vendor_name"] for v in vendor_data]

        # exact lookup cache
        self.name_map = {v["vendor_name"]: v for v in vendor_data}

        # better typo handling than plain word tf-idf
        self.vectorizer = TfidfVectorizer(
            analyzer="char_wb",
            ngram_range=(2, 4)
        )
        self.matrix = self.vectorizer.fit_transform(self.vendor_names)

    def search(self, query, top_n=5):
        query = normalize_text(query)

        # Stage 1: Exact match
        if query in self.name_map:
            vendor = self.name_map[query]
            return {
                "status": "AUTO_MATCH",
                "matches": [{
                    "vendor_code": vendor["vendor_code"],
                    "vendor_name": vendor["vendor_name"],
                    "confidence": 100.0
                }]
            }

        # Stage 2: TF-IDF shortlist
        qv = self.vectorizer.transform([query])
        sims = cosine_similarity(qv, self.matrix).flatten()

        top_idx = sims.argsort()[-20:][::-1]

        results = []

        for i in top_idx:
            vendor = self.vendor_data[i]
            name = vendor["vendor_name"]

            cosine_score = sims[i] * 100
            wratio = fuzz.WRatio(query, name)
            token_score = fuzz.token_sort_ratio(query, name)
            partial_score = fuzz.partial_ratio(query, name)

            final_score = (
                0.35 * cosine_score +
                0.35 * wratio +
                0.20 * token_score +
                0.10 * partial_score
            )

            results.append({
                "vendor_code": vendor["vendor_code"],
                "vendor_name": name,
                "confidence": round(final_score, 2)
            })

        results.sort(key=lambda x: x["confidence"], reverse=True)
        results = results[:top_n]

        # Stage 3: Ambiguity check
        if not results:
            return {
                "status": "NO_MATCH",
                "matches": []
            }

        top1 = results[0]["confidence"]
        top2 = results[1]["confidence"] if len(results) > 1 else 0

        gap = top1 - top2

        if top1 >= 90 and gap >= 5:
            status = "AUTO_MATCH"
        elif top1 >= 75 and gap >= 3:
            status = "REVIEW"
        elif top1 < 60:
            status = "NO_MATCH"
        else:
            status = "USER_SELECTION_REQUIRED"

        return {
            "status": status,
            "matches": results
        }