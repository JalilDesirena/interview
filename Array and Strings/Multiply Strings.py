"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.



"""
num1 = "123"
num2 = "6"

firstNumber=num1[::-1]
secondNumber=num2[::-1]
for i,n2 in enumerate(secondNumber):
    result=[]
    carry=0
    for j,n1 in enumerate(firstNumber):
        rd= int(n2)*int(n1)
        if rd >= 10:         
            rd= (r1 % 10) + carry
            carry = r1 // 10
            print(i,j)
        result.append(rd)