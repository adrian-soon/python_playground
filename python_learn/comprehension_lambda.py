threes_and_fives = [x%5 == 0 or x%3==0 for x in range(1,16)]
squares = [x for x in range(1,11) if x%2==0]
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x!="X", garbled)
print message