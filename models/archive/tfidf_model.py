from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDFModel:
    def __init__(self, vendor_names):
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(vendor_names)

    def transform_query(self, query):
        return self.vectorizer.transform([query])