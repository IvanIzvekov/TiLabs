import math


def calc_enthropy(probs):
    res = 0.0
    for prob in probs:
        res -= prob * math.log2(prob)
    return res


def sort_dict_by_values(d: dict):
    sorted_dict = {}
    for w in sorted(d, key=d.get, reverse=True):
        sorted_dict[w] = d[w]
    return sorted_dict


def get_side_of_interval(left, right, value):
    """
    В параметрах передаем левую и правую границу интервала, а так же значение.
    Функция находит, в какой половине интервала находится это значение, а также возвращает
    середину интервала.
    0 - значение в левой половине, 1 - в правой.
    """
    if value < left or value > right:
        return -1, 0
    middle = (left + right) / 2
    if value < middle:
        return 0, middle
    else:
        return 1, middle


def encode_shennon(probs: dict):
    sorted_dict = sort_dict_by_values(probs)
    encoding = {}
    q = []
    sum = 0
    for p in sorted_dict.values():
        q.append(sum)
        sum += p
    q.append(sum)
    sym_index = 0
    for sym in sorted_dict:
        prob = sorted_dict[sym]
        left = 0
        right = 1
        encoding[sym] = ""
        steps = math.ceil(-math.log2(prob))
        for i in range(steps):
            side, middle = get_side_of_interval(left, right, q[sym_index])
            if side == 0:
                encoding[sym] += "0"
                right = middle
            elif side == 1:
                encoding[sym] += "1"
                left = middle
            else:
                print("Error in encoding")
                return None
        sym_index += 1
    return encoding


def encode_huffman_recursion(probabilitys_list: list):
    return_list = []
    if len(probabilitys_list) == 2:
        char, char_probability = probabilitys_list[0]
        return_list.append((char, char_probability, "0"))
        char, char_probability = probabilitys_list[1]
        return_list.append((char, char_probability, "1"))
        return return_list

    last_2 = probabilitys_list[-2:]
    char = last_2[0][0] + last_2[1][0] # summed chars,  - never mind
    char_probability = last_2[0][1] + last_2[1][1]
    probabilitys_list = probabilitys_list[:-2]
    index = -1
    for i in range(len(probabilitys_list)):
        if probabilitys_list[i][1] < char_probability:
            probabilitys_list.insert(i, (char, char_probability))
            index = i
            break

    if index == -1:
        probabilitys_list.append((char, char_probability))
        index = len(probabilitys_list) - 1

    return_list = encode_huffman_recursion(probabilitys_list)
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


def average_code_length(probabilitys: dict, encoding: dict):
    result_length = 0
    for char in probabilitys:
        char_probability = probabilitys[char]
        encode_length = len(encoding[char])
        result_length += char_probability * encode_length
    return result_length


def encode_text_from_file(file_path):
    char_count = 0
    probabilitys = {}
    file = open(file_path)
    for line in file:
        for char in line:
            if probabilitys.get(char) is None:
                probabilitys[char] = 0
            probabilitys[char] += 1
            char_count += 1

    for char in probabilitys:
        char_probability = probabilitys[char] / char_count
        probabilitys[char] = char_probability

    encoding_shannon_dict = encode_shennon(probabilitys)
    probabilitys_list = list(zip(probabilitys.keys(), probabilitys.values()))
    encoding_huffman_dict = encode_huffman(probabilitys_list)
    entropy = calc_enthropy(probabilitys.values())
    print(f"For file {file_path}:")
    print("\tShannon:")
    print(f"\t\tEncoding: {encoding_shannon_dict}")
    avg_cwl = average_code_length(probabilitys, encoding_shannon_dict)
    print(f"\t\tAverage code word length: {round(avg_cwl, 4)}")
    print(f"\t\tEntropy = {round(entropy, 4)}")
    print(f"\t\tRedundancy = {round(avg_cwl - entropy, 4)}")
    print("\tHuffman:")
    print(f"\t\tEncoding: {encoding_huffman_dict}")
    avg_cwl = average_code_length(probabilitys, encoding_huffman_dict)
    print(f"\t\tAverage code word length: {round(avg_cwl, 4)}")
    print(f"\t\tEntropy = {round(entropy, 4)}")
    print(f"\t\tRedundancy = {round(avg_cwl - entropy, 4)}")


def run():
    encode_text_from_file("file1.txt")
    encode_text_from_file("file2.txt")
    encode_text_from_file("file3.txt")
