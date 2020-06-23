from string import ascii_letters
from text_to_sentence import split_into_sentences


def count_letters(text):
    return len([i for i in text if i in ascii_letters])


def count_words(text):
    return len(text.split())


def count_sentences(text):
    return len(split_into_sentences(text))


def grade(text):
    """
    Coleman_liau_index = 0.0588 * L - 0.296 * S - 15.8
    Here, L is the average number of letters per 100 words in the text,
    and S is the average number of sentences per 100 words in the text.
    """
    result = {}
    result["Word"] = count_words(text)
    result["Sentence"] = count_sentences(text)
    result["Letter"] = count_letters(text)

    L = (result["Letter"] * 100) / result["Word"]
    S = (result["Sentence"] * 100) / result["Word"]

    result["Grade"] = round(0.0588 * L - 0.296 * S - 15.8)

    if result["Grade"] > 16:
        result["Grade"] = "16+"
    elif result["Grade"] < 1:
        result["Grade"] = "0-1"

    return result


if __name__ == "__main__":
    Test_texts = [
        "One fish. Two fish. Red fish. Blue fish.",
        "Would you like them here or there? I would not like them here or there.I would not like them anywhere.",
        "Congratulations! Today is your day. You're off to Great Places! You're off and away!",
        "In my younger and more vulnerable years my father gave me some advice that\
        I've been turning over in my mind ever since.",
        "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.",
        "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays\
        of integers, finite families of finite sets, boolean formulas and elements of other countable domains."]

    text = input("Enter or paste your text to evaluate: ")
    if text:
        result = grade(text)
        print("This text has {} letter(s), {} word(s) and {} sentence(s). Its recommended for grade {}.".format(
              result["Letter"], result["Word"], result["Sentence"], result["Grade"]))
    else:
        print("You have entered nothing.")
