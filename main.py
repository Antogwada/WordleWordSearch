import string
from typing import List
import itertools


class WordProcessor:

    def read_file(self, file_path: str) -> List[str]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [word for word in file.read().splitlines() if self.is_string_valid(word)]

    def is_string_valid(self, word: str) -> bool:
        return all(char in string.ascii_lowercase for char in word)

    def get_unique_letters_count(self, words: List[str]) -> int:
        return len(set(''.join(words)))

    def find_max_unique_letters_group_of_2(self, file_path: str, group_size: int = 2) -> List[str]:
        words = self.read_file(file_path)
        max_unique_letters = 10
        best_group = []
        for group in itertools.combinations(words, group_size):
            unique_letters = self.get_unique_letters_count(group)
            if unique_letters == max_unique_letters:
                best_group.append(list(group))

        self.write_to_file_list(best_group, "words_2.txt")
        return best_group

    def find_max_unique_letters_group_of_3(self) -> List[List[str]]:
        best_group_2 = self.read_file_to_list("words_2.txt")
        max_unique_letters = 15

        first_letter_groups = {}
        for word in best_group_2:
            first_letter_groups.setdefault(word[0], []).append(word)

        best_group = set()
        for group in best_group_2:
            compatible_groups = first_letter_groups.get(group[0], [])

            for alternative in compatible_groups:
                if alternative == group:
                    continue
                candidate_group = group + [alternative[1]]
                unique_letters = self.get_unique_letters_count(candidate_group)

                if unique_letters == max_unique_letters:
                    best_group.add(tuple(candidate_group))

        best_group_list = [list(group) for group in best_group]
        self.write_to_file_list(best_group_list, "words_3.txt")
        return best_group_list

    def find_max_unique_letters_group_of_4(self) -> List[List[str]]:
        best_group_3 = self.read_file_to_list("words_3.txt")
        max_unique_letters = 20

        first_letter_groups = {}
        for group in best_group_3:
            first_letter_groups.setdefault(group[0], []).append(group)

        best_group = set()
        for group in best_group_3:
            compatible_groups = first_letter_groups.get(group[0], [])

            for alternative in compatible_groups:
                if alternative == group:
                    continue

                candidate_group = group + [alternative[1]]
                unique_letters = self.get_unique_letters_count(candidate_group)

                if unique_letters == max_unique_letters:
                    best_group.add(tuple(candidate_group))

        best_group_list = [list(group) for group in best_group]
        self.write_to_file_list(best_group_list, "words_4.txt")
        return best_group_list

    def filter_unique_letter_words(self, words: List[str], letter_count: int = 5) -> List[str]:
        return [word for word in words if len(set(word)) == letter_count]

    def write_to_file(self, data: List[str], output_path: str) -> None:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write("\n".join(data))

    def write_to_file_list(self, data: List[List[str]], output_path: str) -> None:
        with open(output_path, 'w', encoding='utf-8') as file:
            for row in data:
                file.write(','.join(row) + '\n')

    def read_file_to_list(self, file_path: str):
        word_list = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split(',')
                word_list.append(words)
        return word_list


def main():
    processor = WordProcessor()

    best_group = processor.find_max_unique_letters_group_of_4()
    print(len(best_group))
    print("Group with maximum unique letters:", best_group)


if __name__ == "__main__":
    main()
