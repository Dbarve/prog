#Devansh Barve
def encoder(nums):
    out = []
    for i in range(len(nums)):
        if nums[i] >= 7:
            out.append(nums[i] - 7)
        else:
            out.append(nums[i] + 3)
    return out

def main():
    option = 0
    while option != 3:
        input("Menu\n-------------\n1.Encode\n2. Decode\n3. Quit")
        if option == 1:
            nums = input("Please enter your password to encode:")
            encoder(nums)
            print("Your password has been encoded and stored!")
        if option == 2:
            decoder(nums)
            print("Your password has been encoded and stored!")

if __name__ == "__main__":
    main()
