sesipagi = {"andi", "budi","cici",}
sesisiang = {"budi","deni","eka"}

sesihariini = sesipagi | sesisiang
print(sesipagi & sesisiang)
print(sesipagi.symmetric_difference(sesisiang))
print(sesihariini)
