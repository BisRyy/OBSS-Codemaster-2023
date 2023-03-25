import base64
from Crypto.Cipher import AES

# define the encryption key and file path
encryption_key = b'pBaGQuYvArwCIbTiqgVJaavtvlDfDACf'
file_path = 'sample_input_encrypted.txt'

# read the file content
with open(file_path, 'rb') as f:
    encrypted_data = f.read()

# print(encrypted_data)
# decode the Base64-encoded data
decoded_data = base64.b64decode(encrypted_data)

# print(decoded_data)
# initialize the AES cipher in CBC mode with PKCS7 padding
cipher = AES.new(encryption_key, AES.MODE_CBC, b'\x00' * 16)

# decrypt the data
decrypted_data = cipher.decrypt(decoded_data)

import re

def extract_numbers(decrypted_data):
    pages = decrypted_data.split(b'~@~')
    lines = [page.split(b'\n') for page in pages]
    extracted_numbers = []
    for i, page in enumerate(lines, start=1):
        for j, line in enumerate(page, start=1):
            # check if the line is not blank after trimming
            if line.strip():
                line = b'FaabDAWsqqI12N~@D 5x3'
                # search for the FIND token
                find_regex = re.compile(b'F[A-Za-z]+I\d+N[A-Za-z]*I\d+[^\w]{0,5}D')
                match = find_regex.search(line)
                print(match)
                if match:
                    token = match.group().strip()
                    # extract the page and line numbers from the token
                    page_line_regex = re.compile(rb'(\d+)X(\d+)')
                    page_line_match = page_line_regex.search(token)
                    if page_line_match:
                        page_num, line_num = map(int, page_line_match.groups())
                        # extract only the numbers from the line
                        line_numbers = [int(c) for c in line if c.isdigit()]
                        extracted_numbers.append((page_num, line_num, line_numbers))
    return extracted_numbers

print(extract_numbers(decrypted_data))