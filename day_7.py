def word_frequency_dict(filename: str) -> dict:
    with open(filename, "r") as file:
        list1 = file.read().split()
        list2=[]
        for item in list1:
            if item.isalnum():
                list2.append(item)
        dict1 = {}
        for i in list2:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] +=1
        return dict1

if __name__ == "__main__":
    print(word_frequency_dict("day_7_random_text.txt"))