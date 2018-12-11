region_dick = {}
import get_number_agk_on_bb

with open('reg.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        try:
            region_dick[int(i.split()[0])] = i.split()[1]
        #print(i.split()[1])
        except:
            region_dick[i.split()[0]] = i.split()[1]
#print(region_dick)

def find_region(bb):
    agk = get_number_agk_on_bb.number_agk_get(bb)[-4:]

    region = "Неизвестно"

    try:
        if int(agk) in region_dick.keys():

            region = region_dick[int(agk)]
    except:
        try:
            region = region_dick[agk[1:]]
        except:
            region = 'Неизвестно'
    return region

