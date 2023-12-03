from functions.level_2.four_sentiment import check_tweet_sentiment

def test__check_tweet_sentiment__neutral_sentiment():
    text = "This is a neutral tweet."
    good_words = {"happy", "positive"}
    bad_words = {"sad", "negative"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None

def test__check_tweet_sentiment__positive_sentiment():
    text = "I love this product, it's amazing!"
    good_words = {"love", "amazing", "positive"}
    bad_words = {"hate", "terrible", "negative"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "GOOD"

def test__check_tweet_sentiment__negative_sentiment():
    text = "I hate waiting in long lines, it's terrible!"
    good_words = {"love", "amazing", "positive"}
    bad_words = {"hate", "terrible", "negative"}

    result = check_tweet_sentiment(text, good_words, bad_words)
    
    assert result == "BAD"

def test__check_tweet_sentiment__equal_positive_negative_words():
    text = "This is a mixed review, both positive and negative aspects."
    good_words = {"love", "amazing", "positive"}
    bad_words = {"hate", "terrible", "negative"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None

def test__check_tweet_sentiment__case_insensitive_matching():
    text = "I LOVE this product, it's AMAZING!"
    good_words = {"love", "amazing", "positive"}
    bad_words = {"hate", "terrible", "negative"}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "GOOD"

def test__check_tweet_sentiment__empty_input():
    text = ""
    good_words = {"happy", "positive"}
    bad_words = {"sad", "negative"}

    result = check_tweet_sentiment(text, good_words, bad_words)
    
    assert result is None

