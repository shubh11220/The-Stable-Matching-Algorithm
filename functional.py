Men_Pref = {  # indicates the preferences of the men
    'Mike':   ['Rachel', 'Katrina', 'Donna', 'Sheila'],
    'Harvey': ['Donna', 'Katrina', 'Rachel', 'Sheila'],
    'Louis':  ['Sheila', 'Donna', 'Katrina', 'Rachel'],
    'Logan':  ['Rachel', 'Katrina', 'Donna', 'Sheila']
}
Women_Pref = {  # indicates the preferences of the women
    'Rachel':  ['Mike', 'Logan', 'Harvey', 'Louis'],
    'Donna':   ['Harvey', 'Louis', 'Mike', 'Logan'],
    'Katrina': ['Mike', 'Harvey', 'Louis', 'Logan'],
    'Sheila':  ['Louis', 'Logan', 'Harvey', 'Mike']
}
l1 = list(Men_Pref.keys())
l2 = list(Women_Pref.keys())
Men_Free = l1
Women_Free = l2


def matches(list_1):
    matches = {}
    for i in list_1:
        matches[i] = ''
    return matches


Matches = matches(l1)
key_list = list(Matches.keys())

def start_match():
    while len(Men_Free) > 0:
        for i in key_list:
            match_algo(i)

def match_algo(man):
    for woman in Men_Pref[man]:
        if woman not in list(Matches.values()):
            Matches[man] = woman
            Men_Free.remove(man)
            print('{} is no longer a free man and is tentatively engaged to {} !'.format(man, woman))
            break
        elif woman in list(Matches.values()):
            current_suitor = list(Matches.keys())[list(Matches.values()).index(woman)]
            w_list = Women_Pref.get(woman)
            if w_list.index(man) < w_list.index(current_suitor):
                Matches[man] = woman
                Men_Free.remove(man)
                Matches[current_suitor] = ''
                Men_Free.append(current_suitor)
                print('{} was earlier engaged to {} but now is engaged to {}! '.format(woman, current_suitor, man))
                return


print('\n \n \n ')
print('Stable Matching Finished ! Happy engagement !')
for man in Matches.keys():
    print('{} is engaged to {} !'.format(man, Matches[man]))
