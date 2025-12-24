class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        l=date.split()
        print(l)
        if len(l[0])==3:
            l[0]="0"+l[0]
        return l[-1]+"-"+months[l[1]]+"-"+l[0][:2]
                
                
