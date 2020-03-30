import json
import time

import settings
from scripts.load_synonyms_antonyms import get_thesaurus_data


def load_thesaurus():
    words = ["somewhat", "very",
             "extremely",
             "quite",
             "fairly",
             "indeed",
             "highly",
             "slightly",
             "sort_of", ]

    for word in words:
        data = get_thesaurus_data(word)
        dir = settings.BASE_DIR + '/' + settings.STATIC_DIR + '/thesaurus'

        output = open(f"{dir}/{word}.json", "w")
        json.dump(data, output)
        output.close()

        print(f"{word} done")
        time.sleep(1)


def main(args):
    if len(args) > 1 and args[1] == 'thesaurus':
        load_thesaurus()
        return


if __name__ == '__main__':
    import sys

    main(sys.argv)