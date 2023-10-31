#Devansh Barve
def encoder(nums):
    out = []
    for i in range(len(nums)):
        if nums[i] >= 7:
            out.append(nums[i] - 7)
        else:
            out.append(nums[i] + 3)
    return out

def decoder(encoded_nums):
    decoded_password = ''
    for i in encoded_nums:
        digit = int(i)
        if digit < 3:
            decoded_password += str(digit + 7)
        else:
            decoded_password += str(digit - 3)
    return decoded_password


def main():
    encoded_password = None  # To store the encoded password for decoding later
    while True:
        print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit")
        option = int(input("Please enter your choice: "))
        if option == 1:
            nums = input("Please enter your password to encode (only numbers): ")
            encoded_password = encoder(nums)
            print(f"Your password has been encoded: {encoded_password}")
        elif option == 2:
            if encoded_password:
                decoded = decoder(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded}.")
            else:
                print("There's no encoded password to decode.")
        elif option == 3:
            break

if __name__ == "__main__":
    main()
