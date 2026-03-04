'''
   0 1 2 3 4
  
0  0 1 2 3 4
1  0 1 2 3 4
2  0 1 2 3 4
3  0 1 2 3 4
4  0 1 2 3 4
'''
'''n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(col,end=' ')
    print()'''

'''
   0 1 2 3 4
  
0  0 0 0 0 0
1  1 1 1 1 1 
2  2 2 2 2 2
3  3 3 3 3 3
4  4 4 4 4 4
'''

'''n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(row,end=' ')
    print()'''

'''
   0 1 2 3 4
   
0  1 2 3 4 5
1  6 7 8 9 10
2  11 12 13 14 15
3  16 17 18 19 20
4  21 22 23 24 25
'''
'''n=int(input("Enter size:"))
num=1
for i in range(n):
    for j in range(n):
        print(num,end=' ')
        num+=1
    print()'''

'''
   0 1 2 3 4
   
0  0 1 2 3 4
1  1 2 3 4 5
2  2 3 4 5 6
3  3 4 5 6 7
4  4 5 6 7 8
'''
'''n=int(input("Enter size:"))
num=0
for i in range(n):
    for j in range(n):
        print(i+j,end=' ')
        num+=1
    print()'''

'''
   0 1 2 3 4
   
0  0 X 0 X 0
1  X 0 X 0 X
2  0 X 0 X 0
3  X 0 X 0 X
4  0 X 0 X 0'''

'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(0,end=' ')
        else:
            print('X',end=' ')
    print()'''

'''
    0 1 2 3 4
     
0   *
1   * *
2   * * *
3   * * * *
4   * * * * *
'''

'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()'''

'''
  0 1 2 3 4
0 * * * * *
1 * * * *
2 * * *
3 * *
4 *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()'''

'''
  0 1 2 3 4
0         *
1       * *
2     * * *
3   * * * *
4 * * * * *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for spc in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()'''

'''
  0 1 2 3 4
0 * * * * *
1   * * * *
2     * * *
3       * *
4         *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for spc in range(i+1):
        print(' ',end=' ')
    for j in range(n-i-1+1):
        print('*',end=' ')
    print()'''

'''
  0 1 2 3 4
0 *
1 * *
2 * * *
3 * * * *
4 * * * * *
5 * * * *
6 * * *
7 * *
8 *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print('*',end=' ')
    print()'''

'''
  0 1 2 3 4
0 * * * * *
1 *       *
2 *       *
3 *       *
4 * * * * *
'''

'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
   0 1 2 3 4 

0  * * * * * 
1  *   *   * 
2  * * * * *
3  *   *   *
4  * * * * *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''



'''

  0 1 2 3 4
0 * * * * *
1       *
2    *
3  *
4 * * * * *
    
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
  0 1 2 3 4
  
0 *       *
1   *   *
2     *
3   *   *
4 *       *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
   0 1 2 3 4 
  
0  *       *
1  *       *
2  * * * * *
3  *       *  
4  *       *
'''
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''

   0 1 2 3 4
   
0  *
1  *
2  *
3  * 
4  * * * * *
            '''

'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
   0 1 2 3 4
   
0  * * * * *
1  *
2  * * * * *
3          *
4  * * * * *
'''

'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n//2 or i+j==1 or i+j==7:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''

   0 1 2 3 4 5

0  * * * * * *
1  *       *
2  *     *
3  *   * 
4  * *
5  *
'''
n=int(input("Enter size:"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
        for spc in range(i*j==3 or i*j==2 or i*j==1 or i*j==4 or i*j==3):
            print(' ',end=' ')
    print()
        

'''
   0 1 2 3 4 5 6 7 8 
0          *
1        * * *
2      * * * * *
3    * * * * * * *
4  * * * * * * * * *
'''

'''n=int(input("Enter size:"))
for i in range(1,n+1):
    print(' ' * (n-i)+'*'*(2*i-1))'''
        