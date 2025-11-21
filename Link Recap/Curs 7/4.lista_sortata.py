def sorting(*valori):
    sorted_list=[]
    for word in valori:
        if not sorted_list:
            sorted_list.append(word)
        else:
            for existed_word in sorted_list:
                if word < existed_word:
                    sorted_list.insert(sorted_list.index(existed_word), word)
                    break
            else:
                sorted_list.append(word)
    return sorted_list

print(sorting("verde", "negru", "alb", "gri", "fucshia"))