from typing import Any

import math


def calc_enthropy(probabilities):
    result = 0.0
    for probability in probabilities:
        result -= probability * math.log2(probability)
    return result


def sort_dict_by_values(probabilities: dict):
    sorted_dict = {}
    for key in sorted(probabilities, key=probabilities.get, reverse=True):
        sorted_dict[key] = probabilities[key]
    return sorted_dict


def get_side_of_interval(left, right, value):
    if value < left or value > right:
        return -1, 0
    middle = (left + right) / 2
    if value < middle:
        return 0, middle
    else:
        return 1, middle


def encode_shennon(probabilities: dict):
    sorted_dict = sort_dict_by_values(probabilities)
    encoding = {}
    sum_of_probabilities = []
    sum = 0
    for val in sorted_dict.values():
        sum_of_probabilities.append(sum)
        sum += val
    sum_of_probabilities.append(sum)
    char_index = 0
    for char in sorted_dict:
        probability = sorted_dict[char]
        left = 0
        right = 1
        encoding[char] = ""
        steps = math.ceil(-math.log2(probability))
        for i in range(steps):
            side, middle = get_side_of_interval(left, right, sum_of_probabilities[char_index])
            if side == 0:
                encoding[char] += "0"
                right = middle
            elif side == 1:
                encoding[char] += "1"
                left = middle
            else:
                print("Error")
                return None
        char_index += 1
    return encoding


def encode_huffman_recursion(probabilities_list: list):
    return_list = []
    if len(probabilities_list) == 2:
        char, char_probability = probabilities_list[0]
        return_list.append((char, char_probability, "0"))
        char, char_probability = probabilities_list[1]
        return_list.append((char, char_probability, "1"))
        return return_list

    last_2 = probabilities_list[-2:]
    char = last_2[0][0] + last_2[1][0]  # summed chars,  - never mind
    char_probability = last_2[0][1] + last_2[1][1]
    probabilities_list = probabilities_list[:-2]
    index = -1
    for i in range(len(probabilities_list)):
        if probabilities_list[i][1] < char_probability:
            probabilities_list.insert(i, (char, char_probability))
            index = i
            break

    if index == -1:
        probabilities_list.append((char, char_probability))
        index = len(probabilities_list) - 1

    return_list = encode_huffman_recursion(probabilities_list)
    combined = return_list[index]
    return_list.remove(combined)
    return_list.append((last_2[0][0], last_2[0][1], combined[2] + '0'))
    return_list.append((last_2[1][0], last_2[1][1], combined[2] + '1'))
    return return_list


def encode_huffman(probabilitys_list: list):
    return_list = encode_huffman_recursion(probabilitys_list)
    return_dict = {}
    for element in return_list:
        return_dict[element[0]] = element[2]
    return return_dict


def average_code_length(probabilities: dict, encoding: dict):
    result_length = 0
    for char in probabilities:
        char_probability = probabilities[char]
        encode_length = len(encoding[char])
        result_length += char_probability * encode_length
    return result_length


def encode_text_from_file(file_path):
    char_count = 0
    probabilities = {}
    file = open(file_path)
    for line in file:
        for char in line:
            if probabilities.get(char) is None:
                probabilities[char] = 0
            probabilities[char] += 1
            char_count += 1

    for char in probabilities:
        char_probability = probabilities[char] / char_count
        probabilities[char] = char_probability

    encoding_shannon_dict = encode_shennon(probabilities)
    probabilities_list = list(zip(probabilities.keys(), probabilities.values()))
    encoding_huffman_dict = encode_huffman(probabilities_list)
    entropy = calc_enthropy(probabilities.values())
    print(f"For file {file_path}:")
    print("\tShannon:")
    print(f"\t\tEncoding: {encoding_shannon_dict}")
    avg_cwl = average_code_length(probabilities, encoding_shannon_dict)
    print(f"\t\tAverage code word length: {round(avg_cwl, 4)}")
    print(f"\t\tEntropy = {round(entropy, 4)}")
    print(f"\t\tRedundancy = {round(avg_cwl - entropy, 4)}")
    print("\tHuffman:")
    print(f"\t\tEncoding: {encoding_huffman_dict}")
    avg_cwl = average_code_length(probabilities, encoding_huffman_dict)
    print(f"\t\tAverage code word length: {round(avg_cwl, 4)}")
    print(f"\t\tEntropy = {round(entropy, 4)}")
    print(f"\t\tRedundancy = {round(avg_cwl - entropy, 4)}")


def run():
    encode_text_from_file("file1.txt")
    encode_text_from_file("file2.txt")
    encode_text_from_file("file3.txt")
