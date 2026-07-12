class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:

        sh, sm, ss = map(int, startTime.split(":"))
        eh, em, es = map(int, endTime.split(":"))

        start = sh * 3600 + sm * 60 + ss
        end = eh * 3600 + em * 60 + es

        return end - start
            