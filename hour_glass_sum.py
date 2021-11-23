# Maximum sum of hour glass in matrix
arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]
max_sum = 0
ans = []

for index1 in range ( 1 , len ( arr [ 0 ] ) -1 ) :
    for index2 in range ( 1 , len ( arr [ 0 ] ) -1 ) :
        temp1 = arr [ index1 ] [ index2 ]
        temp2 = arr [ index1 - 1 ] [ index2 - 1 : index2 + 2 ]
        temp3 = arr [ index1 + 1 ] [ index2 - 1 : index2 + 2 ]
        temp = temp1 + sum ( temp2 ) + sum ( temp3 )
        if temp > max_sum :
            max_sum = temp
            ans = []
            ans.append ( temp2 )
            ans.append ( temp1 )
            ans.append ( temp3 )

print ( ans , max_sum )