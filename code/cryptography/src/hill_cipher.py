def decryption(matrix):
    def mod_inv(det):
            for i in range (26):
                if (det*i)%26==1: 
                    return i

    def getMatrixMinor(m,i,j):
        l=[] 
        for row in (m[:i]+m[i+1:]):
            l.append(row[:j] + row[j+1:])
        return l

    def transpose(mat):
        trans = []
        rows = len(mat)
        for i in range (rows):
            temp = []
            for j in range (rows):
                temp.append(mat[j][i])
            trans.append(temp) 
        return trans

    def smaller_matrix(matrix,row,column):
        new_matrix = [x[:] for x in matrix]
        new_matrix.remove(matrix[row])
        for i in range(len(new_matrix)):
            new_matrix[i].pop(column) 
        return new_matrix

    def determinant(A):
        num_rows=len(A)
        if len(A)==1:
            return A[0][0]
        elif len(A)==2:
            return A[0][0]*A[1][1] - A[1][0]*A[0][1]
        else:
            ans=0
            num_columns=num_rows
            for j in range(num_columns):
                ans+=(-1)**(j)*A[0][j]*determinant(smaller_matrix(A,0,j))
            return ans

    def matrix_multiplication(mat,det):
        det = mod_inv(det)
        if det==None:
            print("Modular Inverse doesn't exist, create another key")
            exit(0)
        for i in range (len(mat)):
            for j in range (len(mat)):
                mat[i][j]=(mat[i][j]*det)%26
        return mat

    def adjoint(m):
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMatrixMinor(m,r,c)
                cofactorRow.append((((-1)**(r+c)) * determinant(minor))%26)
            cofactors.append(cofactorRow)
        return transpose(cofactors)
        
    det = determinant(matrix) % 26
    print("ADJOINT: ", adjoint(matrix))
    adjoint_matrix = matrix_multiplication(adjoint(matrix),det) 
    return adjoint_matrix
        
def decode(grid,pairs,message):
    for i in pairs:
        for j in range (length):
                res = sum([i[m]*grid[j][m] for m in range (length)])%26
                message += chr(res+97)
    return message

def split_text(text, length):
    var = 0
    for i in range (0,len(text),length):
        temp = []
        for _ in range (length):
            temp.append(ord(text[var])-97)
            var+=1
        pairs.append(temp)
    
def algorithm(length, key):
    var = 0
    for i in range(length):
        temp = []
        for j in range (length):
            temp.append(ord(key[var])-97)
            var+=1
        grid.append(temp)
    
grid, pairs = [], [] 
message = ""
key = input("Enter key : ").lower().replace(' ','')
text = input("Enter cipher/plain text : ").lower().replace(' ','')
choice = input("Enter 'encrypt' for encryption and 'decrypt' for decryption : ").lower()
length = int((len(key))**0.5)
if len(key)>length**2:
    for i in range ((length+1)**2 - len(key)):
        key += chr(97+i)
    length+=1
if (len(text)%length!=0): 
    text+='z'*(length-len(text)%length)
algorithm(length, key)
split_text(text, length)
if(choice == 'decrypt'):
    grid = decryption(grid)
message = decode(grid,pairs,message)
print(choice + "ed text : " + message)    

# Encryption :
# Enter key : hill 
# Enter cipher/plain text : cryptography
# Enter 'encrypt' for encryption and 'decrypt' for decryption : encrypt
# encrypted text : ubcnlzwtqjhd

# Decryption :
# Enter key : hill
# Enter cipher/plain text : ubcnlzwtqjhd
# Enter 'encrypt' for encryption and 'decrypt' for decryption : decrypt
# ADJOINT:  [[11, 18], [15, 7]]
# decrypted text : cryptography
