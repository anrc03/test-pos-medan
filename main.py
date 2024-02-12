# Function for no.1
def count_letter(word):
    result = {}
    for i in word.lower().strip().split(" "):
        for j in i:
            result[j] = result.get(j, 0) + 1
    return result


# Function for no.2
def sort_letter(arr):
    count = {}
    for i in arr:
        i = i.strip()
        for j in i:
            count[j] = count.get(j, 0) + 1
    sorted_arr = sorted(count.items(), key=lambda x: x[1], reverse=True)
    result_arr = []
    taken = []
    for i in range(len(sorted_arr)):
        temp_arr = []
        current_letter = sorted_arr[i][0]
        if current_letter in taken:
            continue
        temp_arr.append(current_letter)
        taken.append(current_letter)
        current_count = sorted_arr[i][1]
        for j in range(i + 1, len(sorted_arr)):
            compared_count = sorted_arr[j][1]
            if current_count != compared_count:
                break
            if current_count == compared_count:
                compared_letter = sorted_arr[j][0]
                temp_arr.append(compared_letter)
                taken.append(compared_letter)
        result_arr.append(temp_arr)
    result = ""
    for i in result_arr:
        result += ''.join(sorted(i))
    return result

if __name__ == '__main__':
    # no.1
    print("Solution for question number 1:")
    input1 = "We Always Mekar"
    input2 = "coding is fun"
    print(count_letter(input1))
    print(count_letter(input2))
    print()

    print("Solution for question number 2:")
    input3 = ["Abc", "bCd"]
    input4 = ["Oke", "One"]
    input5 = ["Pendanaan", "Terproteksi", "Untuk", "Dampak", "Berarti"]
    print(sort_letter(input3))
    print(sort_letter(input4))
    print(sort_letter(input5))
