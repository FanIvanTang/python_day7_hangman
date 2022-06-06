from main import pick_a_word, is_in_word, initial_display, update_display
from hangman_words import word_list


def test_case_1_pick_a_word():
    #word_list = ["aardvark", "baboon", "camel"]
    assert (pick_a_word() in word_list) == True


def test_case_2_initial_display():
    assert initial_display("aardvark") == ["_", "_", "_", "_", "_", "_", "_", "_"]


def test_case_2_update_display():
    assert update_display(
        "a", "aardvark", ["_", "_", "_", "_", "_", "_", "_", "_"]
    ) == ["a", "a", "_", "_", "_", "a", "_", "_"]


def test_case_3_is_in_word():

    assert is_in_word("a", "aardvark") == True


def test_case_4_is_in_word():

    assert is_in_word("b", "aardvark") == False
