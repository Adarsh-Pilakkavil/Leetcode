class Solution:
    def intToRoman(self, num: int) -> str:
        t=""
        t+="M"*(num//1000)
        num=num%1000
        if num>=900:
            t+="CM"
            num-=900
        if num>=500:
            t+="D"
            num-=500
        if num>=400:
            t+="CD"
            num-=400
        if num>=100:
            t+="C"*(num//100)
            num=num%100
        if num>=90:
            t+="XC"
            num-=90
        if num>=50:
            t+="L"
            num-=50
        if num>=40:
            t+="XL"
            num-=40
        if num>=10:
            t+="X"*(num//10)
            num=num%10
        if num==9:
            t+="IX"
            num-=9
        if num>=5:
            t+="V"
            num-=5
        if num==4:
            t+="IV"
            num-=4
        if num>=1:
            t+="I"*num
        return t