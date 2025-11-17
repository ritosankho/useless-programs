import random
import sys

def inputList():
    number_of_numbers = int(input("Enter the number of numbers you want to enter"))
    inputtedList = list()
    for x in range(number_of_numbers):
        element = input("Enter the numbers, press enter after each number to enter it into the list of numbers.")
        try:
            inputtedList.append(float(element))
        except:
            inputtedList.append(element)
    #print(inputtedList)
    return inputtedList

def dynamicInsultGeneration(anyList):
    commonLine = "Enter numbers, you "
    insult = ["blitering idiot", "fool of a took", "dumb broccoli", "2017 Suzuki WagonR", "Boka manush"]
    whichInsultToDisplay = random.randrange(5)
    for checkedElement in anyList:
        
        if type(checkedElement) is not int and type(checkedElement) is not float:
            return commonLine + insult[whichInsultToDisplay]

        else:
            continue
    return "You have more IQ than an average person. You know what numbers are"

class checkList:
    def __init__(self, anyNumericList):
        self.list = anyNumericList

    def max(self):
        max_num = self.list[0]
        for num in self.list:
            if num > max_num:
                max_num = num
        return max_num
        

    def min(self):
        min_num = self.list[0]
        for num in self.list:
            if num < min_num:
                min_num = num
        
        return min_num

def main():
    listOfNumbers = inputList()
    generatedInsult  = dynamicInsultGeneration(listOfNumbers)
    print(generatedInsult)
    if "Enter numbers, you" in generatedInsult:
        sys.exit()
    listObject = checkList(listOfNumbers)
    
    print(f"The maximum number is {listObject.max()} and the minimum number is {listObject.min()}")

    return 0

if __name__ == "__main__":
    main()








    