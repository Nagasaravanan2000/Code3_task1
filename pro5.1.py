def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d


sum=input("Enter the letter")
print(sorted(most_frequent(sum).items(),key=lambda x:x[1],reverse=True))
