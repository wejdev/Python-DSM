def caesar_cipher(s, k):
    result = []

    for char in s:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_char = chr(((ord(char) - shift + k) % 26) + shift)
            result.append(encrypted_char)
        else:
            result.append(char)

    return ''.join(result)


"""
Caeser Cipher

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Example
s = There’s-a-starman-waiting-in-the-sky
k = 3

The alphabet is rotated by 3, matching the mapping above. The encrypted string is wkhuh’v-d-vwdupdq-zdlwlqj-lq-wkh-vnb.

Note: The cipher only encrypts letters; symbols, such as '-', remain unencrypted.

Function Description
Complete the caesarCipher function in the editor below.
caesarCipher has the following parameter(s):
string s: cleartext
int k: the alphabet rotation factor

Returns
string: the encrypted string

Input Format
The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.

Constraints
1 ≤ n ≤ 100
0 ≤ k ≤ 100
s is a valid ASCII string without any spaces.

Sample Input
middle-Outz

Sample Output
okffng-Qwvb

Explanation

Original alphabet: abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2: cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
- -> -
O -> Q
u -> w
t -> v
z -> b

This example illustrates how each letter in the word "middle-Outz" is shifted by two places, with "m" becoming "o", "i" becoming "k", and so on. The hyphen "-" remains unchanged because the cipher only encrypts letters, not symbols or punctuation. The letter "O" is shifted to "Q", maintaining its uppercase form in the encrypted output.
"""
