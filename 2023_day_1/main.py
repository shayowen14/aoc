import re

integer_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def part_1():
    with open('input.txt', 'r') as f:
        running_sum = 0
        for line in f.readlines():
            nums=re.findall(r'\d', line)
            number=nums[0]+nums[-1]
            running_sum += int(number)     
        return running_sum
    

def part_2():
    with open('input.txt', 'r') as f:
        running_sum = 0
        for line in f.readlines():
            matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            nums = [match.group(1) for match in matches]

            if nums[0] in integer_mapping:
                num1 = integer_mapping[nums[0]]
            else:
                num1 = nums[0]

            if nums[-1] in integer_mapping:
                num2 = integer_mapping[nums[-1]]
            else:
                num2 = nums[-1]

            number = num1 + num2
            running_sum += int(number)     
        return running_sum
    

def main():
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")


if __name__ == "__main__":
    main()
