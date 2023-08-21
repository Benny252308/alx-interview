def validUTF8(data):
    num_bytes_to_follow = 0

    for num in data:
        if num_bytes_to_follow == 0:
            if num >> 7 == 0b0:
                # 1-byte character
                continue
            elif num >> 5 == 0b110:
                # 2-byte character
                num_bytes_to_follow = 1
            elif num >> 4 == 0b1110:
                # 3-byte character
                num_bytes_to_follow = 2
            elif num >> 3 == 0b11110:
                # 4-byte character
                num_bytes_to_follow = 3
            else:
                # Invalid leading byte
                return False
        else:
            if num >> 6 == 0b10:
                # Byte following a multi-byte character
                num_bytes_to_follow -= 1
            else:
                # Invalid byte following
                return False

    return num_bytes_to_follow == 0

# Test cases
data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Output: False

