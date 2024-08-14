#14. Longest Common Prefix
def lcp(string):
    string.sort()
    first = string[0]
    last = string[-1] 
    prefix = ''
    i = 1
    while i <= len(first):
    #I chose to use a while loop just to practice using them. This can also be done with a for statement.
        if first[i-1] == last[i-1]:
            prefix += first[i-1]
            i += 1
        else:
            break
    return prefix
