import os

if __name__ == "__main__":
    # get all files in directory
    files = os.listdir('./hadoop_data/')
    
    # store all lines across all files
    all_lines = []

    # for each file
    for file_a in files:
        file_a = './hadoop_data/' + file_a
        # read every line in file
        with open(file_a, "r") as file_a:
            lines = file_a.readlines()
            all_lines.extend(lines)
        

    # seperate word and count
    for i, line in enumerate(all_lines):
        temp = line.split()
        cur_line = []
        cur_line.append(temp[0] + " " + temp[1])
        cur_line.append(temp[2])
        all_lines[i] = cur_line

    # sort by word column
    all_lines.sort()

    total_count = 0
    # swap the two columns to count, word
    all_lines_count = []
    for i, line in enumerate(all_lines):
        temp = []
        num = int(line[1])
        bigram = line[0]
        temp.append(num)
        temp.append(bigram)
        all_lines_count.append(temp)
        
        total_count += num

    # sort by count column
    all_lines_count.sort()

    print("PROBLEM 1")
    # print metrics
    # number of unique bigrams
    print("Number of unique bigrams : [" + str(len(all_lines)) + "]")

    # three example bigrams
    print("Three Examples (indices when using list sorted alphabetically):")
    print("\tIndex 50: [" + str(all_lines[50][0]) + "]")
    print("\tIndex 150: [" + str(all_lines[150][0]) + "]")
    print("\tIndex 250: [" + str(all_lines[250][0]) + "]")

    print()
    print("PROBLEM 2")
    count = 0
    # find most frequent words
    print("Top Ten Most Frequent bigrams:")
    print("\tBIGRAM : COUNT")
    # loop through top ten
    for i in range(10):
        index = -(i+1)
        print("\t[" + str(all_lines_count[index][1]) + "] : [" +
              str(all_lines_count[index][0]) + "]")
        # get sum of most frequent counts
        count+= all_lines_count[index][0]

    print()
    print("PROBLEM 3")
    print("Cumulative Count of Top Ten Bigrams: [" + str(count)  +"]")
    print("Fraction of the counts of Top Ten Bigrams: [" + str(count)
          + "/" + str(total_count)  +"]")
    print("Cumulative Percentage of Top Ten Bigrams: "
          + str((count / total_count)*100)  +"%")

    # get counts for single and three examples of singles
    example_single = []
    single_count = 0
    
    # loop through all bigrams
    for i,(bigram,num) in enumerate(all_lines):
        # if the count is one, it is a single
        if(int(num) == 1):
            single_count += 1

            # track its index
            example_single.append([bigram, i])

    print()
    print("PROBLEM 4")
    print("Number of Bigrams only appearing once: [" + str(single_count) + "]")
    print("Three Examples (indices when using list sorted alphabetically):")

    # print 3 examples
    for i in range(3):
        print("\tIndex " + str(example_single[i*50][1]) + ": " + example_single[i*50][0])

    print()
    print("PROBLEM 5")
    # dictionary of words that follow light
    light_dict = {}
    # loop through our bigrams
    for count, line in all_lines_count:
        word1, word2 = line.split()
        # check if the first word is light
        if(word1 == "light"):
            # track the word with count
            temp = [word1, word2, count]

            # initialize the key with an empty list if we have not seen this word
            if not word2 in light_dict:
                light_dict[word2] = []

            # add the bigram to our dictionary
            light_dict[word2].append(temp)

    word_list = []
    # aggregate the word counts
    for word_base, bigram_list in zip(light_dict.keys(), light_dict.values()):
        cumulative_count = 0
        for word1, word2, count in bigram_list:
            cumulative_count += count

        # track the word with its count
        word_list.append([count, word_base])

    # sort in descending order
    word_list = reversed(sorted(word_list))
    
    print("All bigrams start with light occur exactly once, therefore all have the same frequency.")
    print("Additionally, all words that follow light are unique, therefore there count is still one:")
    print("\tWORD : COUNT : FRACTION")    
    # loop through list of bigrams that start with light
    # these are sorted in descending order from the previous loop above
    for count, word in word_list:
        # display the word
        print("\t[" + word + "] : [" + str(count) + "] : [" + str(count)
          + "/" + str(total_count)  +"]")
