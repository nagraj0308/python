def rotate_right(s, d):
    s = bin(s)[2:]
    return int(s[len(s) - d:] + s[0: len(s) - d], 2)


msg = 'NAGENDRA CHAUDHARY'
w0 = 0
for ch in msg[0:8]:
    w0 = w0 * 256
    w0 = w0 + int(hex(ord(ch)), 16)
k0 = int('428A2F98D728AE22', 16)
init_digest = [int('6A09E667F3BCC908', 16), int('BB67AE8584CAA73B', 16),
               int('3C6EF372EF94F82B', 16), int('A54FE53A5F1D36F1', 16),
               int('510E527FADE682D1', 16), int('9B05688C2B3E6C1F', 16),
               int('1F83D9ABFB41BD6B', 16), int('5BE0CD19137E2179', 16)]
N = int('FFFFFFFFFFFFFFFF', 16)

# Mixer1 section
majority1 = init_digest[0] & init_digest[1]
majority2 = init_digest[1] & init_digest[2]
majority3 = init_digest[2] & init_digest[0]
majority = majority1 ^ majority2 ^ majority3
print('Majority :', hex(majority)[2:])

rot_a1 = rotate_right(init_digest[0], 28)
rot_a2 = rotate_right(init_digest[0], 34)
rot_a3 = rotate_right(init_digest[0], 39)
rot_a = rot_a1 ^ rot_a2 ^ rot_a3
print('Rotation element for A : ', hex(rot_a)[2:])

mixer1 = (majority + rot_a) % 2 ** 64
print('Mixer 1 : ', hex(mixer1)[2:])

# Mixer2 Section
conditional1 = init_digest[4] & init_digest[5]
not_e = init_digest[4] ^ N
conditional2 = not_e & init_digest[6]
conditional = conditional1 ^ conditional2
print('Conditional element : ', hex(conditional)[2:])

rot_e1 = rotate_right(init_digest[4], 28)
rot_e2 = rotate_right(init_digest[4], 34)
rot_e3 = rotate_right(init_digest[4], 39)
rot_e = rot_e1 ^ rot_e2 ^ rot_e3
print('Rotation E : ', hex(rot_e)[2:])

mixer2 = (conditional + rot_e + init_digest[7] + w0 + k0) % 2 ** 64
print('Mixer 2 : ', hex(mixer2)[2:])

# Final Section
x = (mixer1 + mixer2) % 2 ** 64
y = (mixer2 + init_digest[3]) % 2 ** 64
print('Message digest after initial round of SHA-512 is : ')
output_digest = [x, init_digest[0], init_digest[1], init_digest[2], y, init_digest[4], init_digest[5],
                 init_digest[6]]

i = 0
for item in output_digest:
    print(chr(ord('A') + i), '1 : ', hex(item)[2:])
    i = i + 1
