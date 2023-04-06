 # Python Cube Solver

class Cube:
     front = ['R','R','R','R','R','R','R','R']
     back = ['O','O','O','O','O','O','O','O']
     right = ['B','B','B','B','B','B','B','B']
     left = ['G','G','G','G','G','G','G','G']
     up = ['Y','Y','Y','Y','Y','Y','Y','Y']
     down = ['W','W','W','W','W','W','W','W']
     
     solved = True
     
     def __init__(self,front=['R','R','R','R','R','R','R','R'],back=['O','O','O','O','O','O','O','O'],right=['B','B','B','B','B','B','B','B'],left=['G','G','G','G','G','G','G','G'],up=['Y','Y','Y','Y','Y','Y','Y','Y'],down=['W','W','W','W','W','W','W','W']):
         self.front = front
         self.back = back
         self.right = right
         self.left = left
         self.up = up
         self.down = down
     
     def isSolved(self):
         if self.front != ['R','R','R','R','R','R','R','R'] or self.back != ['O','O','O','O','O','O','O','O'] or self.right != ['B','B','B','B','B','B','B','B'] or self.left != ['G','G','G','G','G','G','G','G'] or self.up != ['Y','Y','Y','Y','Y','Y','Y','Y'] or self.down != ['W','W','W','W','W','W','W','W']:
             solved = False
             return False
         solved = True
         return True
         
     def input(self):
         print("Enter the colours on Cube:")
         print("Enter only the first letter of colour in capital.")
         print("Enter colour of each face like this :\n1   2   3\n4       5\n6   7   8")
         print("Enter colours for Red center(yellow top) :")
         for i in range(0,8):
             self.front[i] = input(i+1).capitalize()
         print("Enter colours for Orange center(yellow top) :")
         for i in range(0,8):
             self.back[i] = input(i+1).capitalize()
         print("Enter colours for blue center(yellow top) :")
         for i in range(0,8):
             self.left[i] = input(i+1).capitalize()
         print("Enter colours for green center(yellow top) :")   
         for i in range(0,8):
             self.right[i] = input(i+1).capitalize()
         print("Enter colours for yellow center(orange top) :")
         for i in range(0,8):
             self.up[i] = input(i+1).capitalize()
         print("Enter colours for White center(red top) :")
         for i in range(0,8):
             self.down[i] = input(i+1).capitalize()
         if self.isSolved():
             print("Cube Already Solved")
             exit()
         
     def turn(self, turn):
         turns = ["R","R`","R2","L","L`","L2", "U","U`" ,"U2", "D","D`","D2","F","F`","F2","B","B`","B2"]
         if not turn in turns:
             print("Wrong Input Error") 
             exit()
         if turn == "U":
             temp1 = self.front[0]
             temp2 = self.front[1]
             temp3 = self.front[2]
             self.front[0] = self.left[0]
             self.front[1] = self.left[1]
             self.front[2] = self.left[2]
             self.left[0] = self.back[0]
             self.left[1] = self.back[1]
             self.left[2] = self.back[2]
             self.back[0] = self.right[0]
             self.back[1] = self.right[1]
             self.back[2] = self.right[2]
             self.right[0] = temp1
             self.right[1] = temp2
             self.right[2] = temp3
             temp4 = self.up[0]
             temp5 = self.up[1]
             self.up[0] = self.up[5]
             self.up[5] = self.up[7]
             self.up[7] = self.up[2]
             self.up[2] = temp4
             self.up[1] = self.up[3]
             self.up[3] = self.up[6]
             self.up[6] = self.up[4]
             self.up[4] = temp5
         if turn == "U`":
             temp1 = self.front[0]
             temp2 = self.front[1]
             temp3 = self.front[2]
             self.front[0] = self.right[0]
             self.front[1] = self.right[1]
             self.front[2] = self.right[2]
             self.right[0] = self.back[0]
             self.right[1] = self.back[1]
             self.right[2] = self.back[2]
             self.back[0] = self.left[0]
             self.back[1] = self.left[1]
             self.back[2] = self.left[2]
             self.left[0] = temp1
             self.left[1] = temp2
             self.left[2] = temp3
             temp4 = self.up[0]
             temp5 = self.up[1]
             self.up[0] = self.up[2]
             self.up[2] = self.up[7]
             self.up[7] = self.up[5]
             self.up[5] = temp4
             self.up[1] = self.up[4]
             self.up[4] = self.up[6]
             self.up[6] = self.up[3]
             self.up[3] = temp5
         if turn == "R2":
             self.turn("U")
             self.turn("U")
         if turn == "D":
             temp1 = self.front[5]
             temp2 = self.front[6]
             temp3 = self.front[7]
             self.front[5] = self.right[5]
             self.front[6] = self.right[6]
             self.front[7] = self.right[7]
             self.right[5] = self.back[5]
             self.right[6] = self.back[6]
             self.right[7] = self.back[7]
             self.back[5] = self.left[5]
             self.back[6] = self.left[6]
             self.back[7] = self.left[7]
             self.left[5] = temp1
             self.left[6] = temp2
             self.left[7] = temp3
             temp4 = self.down[0]
             temp5 = self.down[1]
             self.down[0] = self.down[5]
             self.down[5] = self.down[7]
             self.down[7] = self.down[2]
             self.down[2] = temp4
             self.down[1] = self.down[3]
             self.down[3] = self.down[6]
             self.down[6] = self.down[4]
             self.down[4] = temp5
         if turn == "D`":
             temp1 = self.front[5]
             temp2 = self.front[6]
             temp3 = self.front[7]
             self.front[5] = self.left[5]
             self.front[6] = self.left[6]
             self.front[7] = self.left[7]
             self.left[5] = self.back[5]
             self.left[6] = self.back[6]
             self.left[7] = self.back[7]
             self.back[5] = self.right[5]
             self.back[6] = self.right[6]
             self.back[7] = self.right[7]
             self.right[5] = temp1
             self.right[6] = temp2
             self.right[7] = temp3
             temp4 = self.down[0]
             temp5 = self.down[1]
             self.down[0] = self.down[2]
             self.down[2] = self.down[7]
             self.down[7] = self.down[5]
             self.down[5] = temp4
             self.down[1] = self.down[4]
             self.down[4] = self.down[6]
             self.down[6] = self.down[3]
             self.down[3] = temp5
         elif turn == "D2":
             self.turn("D")
             self.turn("D")
         
         elif turn == "R":
             temp1 = self.front[2]
             temp2 = self.front[4]
             temp3 = self.front[7]
             self.front[2] = self.down[2]
             self.front[4] = self.down[4]
             self.front[7] = self.down[7]
             self.down[2] = self.back[5]
             self.down[4] = self.back[3]
             self.down[7] = self.back[0]
             self.back[5] = self.up[2]
             self.back[3] = self.up[4]
             self.back[0] = self.up[7]
             self.up[2] = temp1
             self.up[4] = temp2
             self.up[7] = temp3
             temp4 = self.left[0]
             temp5 = self.left[1]
             self.left[0] = self.left[5]
             self.left[5] = self.left[7]
             self.left[7] = self.left[2]
             self.left[2] = temp4
             self.left[1] = self.left[3]
             self.left[3] = self.left[6]
             self.left[6] = self.left[4]
             self.left[4] = temp5
         elif turn == "R`":
             temp1 = self.front[2]
             temp2 = self.front[4]
             temp3 = self.front[7]
             self.front[2] = self.up[2]
             self.front[4] = self.up[4]
             self.front[7] = self.up[7]
             self.up[2] = self.back[5]
             self.up[4] = self.back[3]
             self.up[7] = self.back[0]
             self.back[5] = self.down[2]
             self.back[3] = self.down[4]
             self.back[0] = self.down[7]
             self.down[2] = temp1
             self.down[4] = temp2
             self.down[7] = temp3
             temp4 = self.left[0]
             temp5 = self.left[1]
             self.left[0] = self.left[2]
             self.left[2] = self.left[7]
             self.left[7] = self.left[5]
             self.left[5] = temp4
             self.left[1] = self.left[4]
             self.left[4] = self.left[6]
             self.left[6] = self.left[3]
             self.left[3] = temp5
         elif type == "R2":
             self.turn("R")
             self.turn("R")
                 
         elif turn == "L":
             temp1 = self.front[0]
             temp2 = self.front[3]
             temp3 = self.front[5]
             self.front[0] = self.up[0]
             self.front[3] = self.up[3]
             self.front[5] = self.up[5]
             self.up[0] = self.back[7]
             self.up[3] = self.back[4]
             self.up[5] = self.back[2]
             self.back[7] = self.down[0]
             self.back[4] = self.down[3]
             self.back[2] = self.down[5]
             self.down[0] = temp1
             self.down[3] = temp2
             self.down[5] = temp3
             temp4 = self.right[0]
             temp5 = self.right[1]
             self.right[0] = self.right[5]
             self.right[5] = self.right[7]
             self.right[7] = self.right[2]
             self.right[2] = temp4
             self.right[1] = self.right[3]
             self.right[3] = self.right[6]
             self.right[6] = self.right[4]
             self.right[4] = temp5
         elif turn == "L`":
             temp1 = self.front[0]
             temp2 = self.front[3]
             temp3 = self.front[5]
             self.front[0] = self.down[0]
             self.front[3] = self.down[3]
             self.front[5] = self.down[5]
             self.down[0] = self.back[7]
             self.down[3] = self.back[4]
             self.down[5] = self.back[2]
             self.back[7] = self.up[0]
             self.back[4] = self.up[3]
             self.back[2] = self.up[5]
             self.up[0] = temp1
             self.up[3] = temp2
             self.up[5] = temp3
             temp4 = self.right[0]
             temp5 = self.right[1]
             self.right[0] = self.right[2]
             self.right[7] = self.right[5]
             self.right[7] = self.right[5]
             self.right[5] = temp4
             self.right[1] = self.right[4]
             self.right[4] = self.right[6]
             self.right[6] = self.right[3]
             self.right[3] = temp5
         elif type == "L2":
             self.turn("L")
             self.turn("L")
              
         if turn == "F":
             temp1 = self.up[5]
             temp2 = self.up[6]
             temp3 = self.up[7]
             self.up[5] = self.right[7]
             self.up[6] = self.right[4]
             self.up[7] = self.right[2]
             self.right[7] = self.down[2]
             self.right[4] = self.down[1]
             self.right[2] = self.down[0]
             self.down[2] = self.left[0]
             self.down[1] = self.left[3]
             self.down[0] = self.left[5]
             self.left[0] = temp1
             self.left[3] = temp2
             self.left[5] = temp3
             temp4 = self.front[0]
             temp5 = self.front[1]
             self.front[0] = self.front[5]
             self.front[5] = self.front[7]
             self.front[7] = self.front[2]
             self.front[2] = temp4
             self.front[1] = self.front[3]
             self.front[3] = self.front[6]
             self.front[6] = self.front[4]
             self.front[4] = temp5
         elif turn == "F`":
             temp1 = self.up[5]
             temp2 = self.up[6]
             temp3 = self.up[7]
             self.up[5] = self.left[0]
             self.up[6] = self.left[3]
             self.up[7] = self.left[5]
             self.left[0] = self.down[2]
             self.left[3] = self.down[1]
             self.left[5] = self.down[0]
             self.down[2] = self.right[7]
             self.down[1] = self.right[4]
             self.down[0] = self.right[2]
             self.right[7] = temp1
             self.right[4] = temp2
             self.right[2] = temp3
             temp4 = self.front[0]
             temp5 = self.front[1]
             self.front[0] = self.front[2]
             self.front[2] = self.front[7]
             self.front[7] = self.front[5]
             self.front[5] = temp4
             self.front[1] = self.front[4]
             self.front[4] = self.front[6]
             self.front[6] = self.front[3]
             self.front[3] = temp5
         elif type == "F2":
             self.turn("F")
             self.turn("F")
                 
         if turn == "B":
             temp1 = self.up[0]
             temp2 = self.up[1]
             temp3 = self.up[2]
             self.up[0] = self.left[2]
             self.up[1] = self.left[4]
             self.up[2] = self.left[7]
             self.left[2] = self.down[7]
             self.left[4] = self.down[6]
             self.left[7] = self.down[5]
             self.down[7] = self.right[5]
             self.down[6] = self.right[3]
             self.down[5] = self.right[0]
             self.right[5] = temp1
             self.right[3] = temp2
             self.right[0] = temp3
             temp4 = self.back[0]
             temp5 = self.back[1]
             self.back[0] = self.back[5]
             self.back[5] = self.back[7]
             self.back[7] = self.back[2]
             self.back[2] = temp4
             self.back[1] = self.back[3]
             self.back[3] = self.back[6]
             self.back[6] = self.back[4]
             self.back[4] = temp5
         elif turn == "B`":
             temp1 = self.up[2]
             temp2 = self.up[1]
             temp3 = self.up[0]
             self.up[2] = self.right[0]
             self.up[1] = self.right[3]
             self.up[0] = self.right[5]
             self.right[0] = self.down[5]
             self.right[3] = self.down[6]
             self.right[5] = self.down[7]
             self.down[5] = self.left[7]
             self.down[6] = self.left[4]
             self.down[7] = self.left[2]
             self.left[7] = temp1
             self.left[4] = temp2
             self.left[2] = temp3
             temp4 = self.back[0]
             temp5 = self.back[1]
             self.back[0] = self.back[2]
             self.back[2] = self.back[7]
             self.back[7] = self.back[5]
             self.back[5] = temp4
             self.back[1] = self.back[4]
             self.back[4] = self.back[6]
             self.back[6] = self.back[3]
             self.back[3] = temp5
         elif type == "B2":
             self.turn("B")
             self.turn("B")
        
     def solve(self):
         count = 1
         turns = ["U","U`","U2","D","D`","D2","L","L`","L2","R","R`","R2","F","F`","F2","B","B`","B2"]
         for a in turns:
             cube1 = self
             cube1.turn(a)
             if cube1.isSolved():
                 print(f"Sol: {a}")
                 exit()
             for b in turns:
                 if b[0] in a:
                     continue
                 cube2 = cube1
                 cube2.turn(b)
                 if cube2.isSolved():
                     print(f"Sol: {a} {b}")
                     exit()
                 for c in turns:
                     if c[0] in b:
                         continue
                     cube3 = cube2
                     cube3.turn(c)
                     if cube3.isSolved():
                         print(f"Sol: {a} {b} {c}")
                         exit()
                     for d in turns:
                         if d[0] in c:
                            continue
                         cube4 = cube3
                         cube4.turn(d)
                         if cube4.isSolved():
                             print(f"Sol: {a} {b} {c} {d}")
                             exit()    
                         for e in turns:
                             if e[0] in d:
                                 continue
                             cube5 = cube4
                             cube5.turn(e)
                             if cube5.isSolved():
                                 print(f"Sol: {a} {b} {c} {d} {e}")
                                 exit()
                             for f in turns:
                                 if f[0] in e:
                                     continue
                                 cube6 = cube5
                                 cube6.turn(f)
                                 if cube6.isSolved():
                                     print(f"Sol: {a} {b} {c} {d} {e} {f}")
                                     exit()
                                 for g in turns:
                                     if g[0] in f:
                                         continue
                                     cube7 = cube6
                                     cube7.turn(g)
                                     if cube7.isSolved():
                                         print(f"Sol: {a} {b} {c} {d} {e} {f} {g}")
                                         exit()    
                                     for h in turns:
                                         if h[0] in g:
                                             continue
                                         cube8 = cube7
                                         cube8.turn(h)
                                         if cube8.isSolved():
                                             print(f"Sol: {a} {b} {c} {d} {e} {f} {g} {h}")
                                             exit()
                                         for i in turns:
                                             if i[0] in h:
                                                 continue
                                             cube9 = cube8
                                             cube9.turn(i)
                                             if cube9.isSolved():
                                                 print(f"Sol: {a} {b} {c} {d} {e} {f} {g} {h} {i}")
                                                 exit()
                                             for j in turns:
                                                 if j[0] in i:
                                                     continue
                                                 cube10 = cube9
                                                 cube10.turn(j)
                                                 if cube10.isSolved():
                                                     print(f"Sol: {a} {b} {c} {d} {e} {f} {g} {h} {i} {j}")
                                                     exit()    
                                                 for k in turns:
                                                     if k[0] in j:
                                                         continue
                                                     cube11 = cube10
                                                     cube11.turn(k)
                                                     if cube11.isSolved():
                                                         print(f"Sol: {a} {b} {c} {d} {e} {f} {g} {h} {i} {j} {k}")
                                                         exit()
                                                     for l in turns:
                                                         if l[0] in k:
                                                             continue
                                                         cube12 = cube11
                                                         cube12.turn(l)
                                                         print(f"Searching {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}....")
                                                         count += 1
                                                         if cube12.isSolved():
                                                             print(f"Sol: {a} {b} {c} {d} {e} {f} {g} {h} {i} {j} {k} {l}")
                                                             exit()
                                                             
         print("No Solutions Found")
         
     def print_cube(self):
         print(f"Front :\n {self.front[0]}   {self.front[1]}   {self.front[2]}\n {self.front[3]}   R   {self.front[4]}\n {self.front[5]}   {self.front[6]}   {self.front[7]}")
         print(f"Back :\n {self.back[0]}   {self.back[1]}   {self.back[2]}\n {self.back[3]}   O   {self.back[4]}\n {self.back[5]}   {self.back[6]}   {self.back[7]}")
         print(f"Left :\n {self.left[0]}   {self.left[1]}   {self.left[2]}\n {self.left[3]}   G   {self.left[4]}\n {self.left[5]}   {self.left[6]}   {self.left[7]}")
         print(f"Right :\n {self.right[0]}   {self.right[1]}   {self.right[2]}\n {self.right[3]}   B   {self.right[4]}\n {self.right[5]}   {self.right[6]}   {self.right[7]}")
         print(f"Up :\n {self.up[0]}   {self.up[1]}   {self.up[2]}\n {self.up[3]}   Y   {self.up[4]}\n {self.up[5]}   {self.up[6]}   {self.up[7]}")
         print(f"Down :\n {self.down[0]}   {self.down[1]}   {self.down[2]}\n {self.down[3]}   W   {self.down[4]}\n {self.down[5]}   {self.down[6]}   {self.down[7]}")
  
new = Cube(["G","G","W","R","W","B","B","O"],["R","B","B","Y","O","Y","G","G"],["R","G","Y","R","O","W","G","O"],["R","R","W","B","B","Y","O","O"],["Y","Y","G","Y","W","R","R","B"],["W","W","G","W","Y","O","O","B"])
#new = Cube(['O','O','O','R','R','R','R','R'],['R','R','R','O','O','O','O','O'],['G','G','G','B','B','B','B','B'],['B','B','B','G','G','G','G','G'],['Y','Y','Y','Y','Y','Y','Y','Y'],['W','W','W','W','W','W','W','W'])
#new.input()
new.print_cube()
'''
print("\nAfter Solving \n")
new.turn("R", "`")
new.turn("U", "`")
new.turn("D", "`")
new.turn("R", "`")
new.print_cube()'''
new.solve()
new.print_cube()
#new.print_solutions()
     