import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment

@pytest.mark.parametrize(
    "text, good_words, bad_words, expected",
    [
        pytest.param("This is a neutral tweet.", 
                     {"happy", "positive"}, {"sad", "negative"}, 
                     None, id='return_none_when_neutral_sentiment'),
        pytest.param("I love this product, it's amazing!", 
                     {"love", "amazing", "positive"}, {"hate", "terrible", "negative"}, 
                     "GOOD", id='positive_sentiment'),
        pytest.param("I hate waiting in long lines, it's terrible!", 
                     {"love", "amazing", "positive"}, {"hate", "terrible", "negative"}, 
                     "BAD", id='negative_sentiment'),
        pytest.param("This is a mixed review, both positive and negative aspects.", 
                     {"love", "amazing", "positive"}, {"hate", "terrible", "negative"}, 
                     None, id='return_none_when_equal_positive_negative_words'),
        pytest.param("I LOVE this product, it's AMAZING!", {"love", "amazing", "positive"}, {"hate", "terrible", "negative"}, 
                     "GOOD", id='case_insensitive_matching'),
        pytest.param("", {"happy", "positive"}, {"sad", "negative"}, 
                     None, id='return_none_when_empty_input'),
    ]
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected):
    result = check_tweet_sentiment(text, good_words, bad_words)
    assert result == expected
