# x, y, z = input("give me numbers: ").split()
# print("x= ",x)
# print("y= ",y)
# print("z= ",z)

# subs = 2400
# likes = 200
# comment = 53

# conditions = [
#     subs > 150,
#     likes > 150,
#     comment>50
# ]

# if all(conditions):
#     print('Awesome Video')
# else:
#     print("No condition fullied")

# subs = 2400
# likes = 200
# comment = 53

# conditions = [
#     subs > 150,
#     likes > 150,
#     comment > 50
# ]

# if any(conditions):
#     print('Awesome Video')
# else:
#     print("No condition fullied")

# subs = 2400
# likes = 200

# print ( subs, likes )
# temp = subs
# subs = likes
# likes = temp
# print ( subs, likes )
# subs = 2400
# likes = 200

# print ( subs, likes )
# subs, likes = likes, subs
# print ( subs, likes )


# a = [1,2,3,4,5,6,7,5,4,3,12,2,2,5,6,7,1,1,2,4]
# print(a)
# a = list(set(a))
# print(a)

# a = [1,2,3,4,5,6,7,5,4,3,12,2,2,5,6,7,1,1,2,4]
# print(a)
# most = max(set(a), key=a.count)
# print(most)

# odd_squares = []
# for i in range(11):
#     if i % 2 == 1:
#         odd_squares.append(i**2)

# odd_squares = [i**2 for i in range(11) if i %2 == 1]
# print(odd_squares)

def sum(*a):
    result = 0
    for i in a:
        result = result + i
    return result

res = sum(2,3,5,500,800)
print(res)