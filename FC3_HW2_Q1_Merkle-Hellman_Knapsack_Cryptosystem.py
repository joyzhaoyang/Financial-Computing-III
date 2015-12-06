"""
This file: FC3HW2Prob1.py
Programmer: Joy Zhao (yangzhao@tepper.cmu.edu)
Course/Section: 46-903
Assignment: Homework2, Problem1
Description: Merkle-Hellman Knapsack Cryptosystem
Performing key generation, encryption and decryption and using Python lists.
Methods: http://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem
Last Modified: 04/08/15
Known Bugs: fixed keys as suggested in Discussion Board
"""

"""
Comments:
The best case and worst case computational complexity
of both the encryption and decryption process is O(n), 
where n is the size of text. 
I write a very simple program here. Encryption is performed 
character by character of the string, and the results are stored
in a list of integers, each integer is the code for a character. 
Similarly, decryption is also performance character by character. 
"""


""" Get input string """
str_input = raw_input('Enter a string and I will encrypt it as single large integer.')

while len(str_input) >= 80: # if string is too long, try again
    str_input = raw_input('Enter a string of fewer than 80 characters in length, try again')

""" Initiate keys, source: wikipedia """
w = [2,7,11,21,42,89,180,354] # basis for private key
q = 881 # modulus
r = 588 # multiplier
b = [] # public key

# generate public key
for i in range(len(w)):
    b.append(w[i]*r%q) # public key
    
""" Encryption """
codes = [] # list of intergers, each representing encryption of each character

for c in str_input:
    bin_str = format(ord(c), 'b')
    if len(bin_str)==7: # eight digits binary code of character
        bin_str = "0"+format(ord(c), 'b')  
    elif len(bin_str)==6:
        bin_str = "00"+format(ord(c), 'b')
    # print(bin_str)
    code = 0
    for i in range(len(bin_str)):
        code = code + int(bin_str[i])*b[i]
    codes.append(code)

""" Print results of Encryption"""
print "Clear text:"
print str_input
print "Number of clear text bytes = ", len(str_input)
print str_input, "is encrypted as "
print ''.join(map(str, codes))

""" Modular inverse """
# source: http://rosettacode.org/wiki/Modular_inverse#Python
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
    
""" Decryption """
s = modinv(r, q);
str_output = ""
for i in range(len(codes)):
    c = codes[i]*s%q
    bin_out = ""
    for j in range(len(w)):
        if c-w[len(w)-j-1]>=0:
            c = c-w[len(w)-j-1]
            bin_out = "1" + bin_out
        else: 
            bin_out = "0" + bin_out
    str_output = str_output+chr(int(bin_out, 2)) # convert to character
    
""" Print results of Decryption """
print "Result of decryption: ", str_output

""" The fix """
raw_input("Press enter to exit")
