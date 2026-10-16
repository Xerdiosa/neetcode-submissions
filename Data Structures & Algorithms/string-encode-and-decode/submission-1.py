class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = []
        for i in strs:
            builder.append(f"{len(i)}:{i}")
        print("".join(builder))
        return "".join(builder)

    def decode(self, s: str) -> List[str]:
        ret = list()
        tmp = list()
        reader = 0
        chunk = 0

        for i in list(s):
            # print(i)
            if reader == 0 and i != ":": #headermode
                chunk = chunk * 10 + int(i)
                # print(f"chunkis {chunk}")
            elif reader == 0 and i == ':': # start building string
                reader = chunk
                chunk = 0
                if reader == 0:
                    ret.append("")
                # print("startwriting")
            else:   #print
                reader = reader - 1
                tmp.append(i)
                if reader == 0 and len(tmp)>0:
                    ret.append("".join(tmp))
                    tmp = list()
            # print()
        return ret
