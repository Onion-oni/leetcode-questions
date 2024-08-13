#Solution to 135. Candy
#Each child must have a candy and childre with higher ratings gtet more candies than their neighbors
def candy(ratings):
    k = len(ratings)
    c = len(ratings)
    
    for i in range(1,k):
        if ratings[i] > ratings[i-1]:
            c += 1
    for i in range(k-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            c += 1
    return c
