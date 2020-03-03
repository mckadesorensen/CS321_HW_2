import word_frequency as wf


def test_open_file() -> None:
    assert type(wf.open_file("../test.txt")) == str


def test_break_up_words() -> None:
    words_string = "Hello\nThere"
    words = wf.break_up_words(words_string)
    assert words == ["Hello", "There"]


def test_get_word_frequency() -> None:
    words = ["Hello", "Hello", "There"]
    words_stats_template = {
        "hello": 2,
        "there": 1
    }

    words_stats = wf.get_word_frequency(words)
    assert words_stats == words_stats_template


def test_count_of_highest_used_word() -> None:
    words_template = {
        "Bye":   5,
        "hello": 3,
        "there": 2
    }
    highest_used_word = wf.count_of_highest_used_word(words_template)

    assert highest_used_word[1] == 5
    assert type(highest_used_word) == tuple
    assert type(highest_used_word[0]) == str
    assert type(highest_used_word[1]) == int


def test_count_of_lowest_used_word() -> None:
    words_template = {
        "Bye":   5,
        "hello": 3,
        "there": 2
    }
    lowest_used_word = wf.count_of_lowest_used_word(words_template)

    assert lowest_used_word[1] == 2
    assert type(lowest_used_word) == tuple
    assert type(lowest_used_word[0]) == str
    assert type(lowest_used_word[1]) == int


def test_find_high_low_values() -> None:
    words_template = {
        "Bye":   5,
        "hello": 3,
        "there": 2
    }
    high_low_values_template = {
        "lowest":  2,
        "highest": 5
    }
    high_low_values = wf.find_high_low_values(words_template)
    assert high_low_values == high_low_values_template
    assert type(high_low_values["highest"]) == int


def test_set_frequency_levels() -> None:
    levels_test = {
        "low":    {
            "low_bound":  1,
            "high_bound": 2
        },
        "medium": {
            "low_bound":  3,
            "high_bound": 4
        },
        "high":   {
            "low_bound":  5,
            "high_bound": 6
        }
    }
    high_low_levels = {
        "lowest":  1,
        "highest": 6
    }

    levels = wf.set_frequency_levels(high_low_levels)
    assert levels == levels_test
