from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set()
        self.negatives = set()
        with open(positives) as lines:
            for line in lines:
                line = line.strip('\n').strip(' ')
                if line.startswith(";") != True:
                    self.positives.add(line)
        with open(negatives) as lines:
            for line in lines:
                line = line.strip('\n').strip(' ')
                if line.startswith(";") != True:
                    self.negatives.add(line)
        self.tokenizer = TweetTokenizer()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            if token in self.positives:
                score += 1
            if token in self.negatives:
                score -= 1
        return score
