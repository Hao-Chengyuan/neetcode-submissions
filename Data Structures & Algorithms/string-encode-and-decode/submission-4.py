class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for str_item in strs:

            if len(str_item) < 10:
                
                s = s + "00" + str(len(str_item)) + str_item

            elif 10 <= len(str_item) < 100:

                s = s + "0" + str(len(str_item)) + str_item

            else:

                s = s + str(len(str_item)) + str_item

        return s


    def decode(self, s: str) -> List[str]:

        strs = []

        while len(s) != 0:

            if s[0] == "0" and s[1] == "0":

                str_item = ""

                for j in range(3, int(s[2])+3):
                    str_item += s[j]

                s = s[(int(s[2])+3):]

            elif s[0] == "0" and s[1] != "0":

                str_item = ""

                for j in range(3, (int(s[1])*10+int(s[2]))+3):

                    str_item += s[j]

                s = s[(int(s[1])*10+int(s[2]))+3:]
            
            else:

                str_item = ""

                for j in range(3, (int(s[0])*100+int(s[1])*10+int(s[2]))+3):

                    str_item += s[j]

                s = s[(int(s[0])*100+int(s[1])*10+int(s[2]))+3:]
            strs.append(str_item)

        return strs



        
