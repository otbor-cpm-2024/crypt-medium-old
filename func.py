# medium_crypt
def medium_crypt(text, key):
  if len(text) % 2 == 0:
    key += 'ilovecrypt'
  text = ''.join('{:0>8b}'.format(ord(x)) for x in text)
  key = ''.join('{:0>8b}'.format(ord(x)) for x in key)
  crypt_text = ''
  for i in range(len(text)):
    crypt_text += str(int(text[i]) ^ int(key[i % len(key)]))
  for i in range(0, len(crypt_text), 8):
    print(hex(int(crypt_text[i:i+8], 2)), end='')
