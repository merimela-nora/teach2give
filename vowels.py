def countVowels(input_string):
    vowels = "AEIOUaeiou"
    return sum(1 for char in input_string if char in vowels)

input_string = "maya is my cat"
vowels = countVowels(input_string)

print(f"{vowels}")
