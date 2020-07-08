
# Part 1: Initialization
Men = ['Mike', 'Harvey', 'Louis', 'Logan']
Women = ['Rachel', 'Donna', 'Katrina', 'Sheila']

# Part 3: Preferences
Men_Pref = {  # indicates the preferences of the men
    'Mike':   ['Rachel', 'Katrina', 'Donna', 'Sheila'],
    'Harvey': ['Rachel', 'Donna', 'Katrina', 'Sheila'],
    'Louis':  ['Katrina', 'Sheila', 'Donna', 'Rachel'],
    'Logan':  ['Donna', 'Katrina', 'Rachel', 'Sheila'],

}
Women_Pref = {  # indicates the preferences of the women
    'Rachel':  ['Mike', 'Logan', 'Harvey', 'Louis'],
    'Donna':   ['Harvey', 'Louis', 'Mike', 'Logan'],
    'Katrina': ['Harvey', 'Mike', 'Louis', 'Logan'],
    'Sheila':  ['Louis', 'Logan', 'Harvey', 'Mike']
}

Men_Free = list(Men)
Women_Free = list(Women)

# Part 3: Proposal
Matches = {
    'Mike':  '',
    'Harvey': '',
    'Louis': '',
    'Logan': ''
    }
key_list = list(Matches.keys())
while len(Men_Free) > 0:
    for man in key_list:
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

print('\n \n \n ')
print('Stable Matching Finished ! Happy engagement !')
for man in Matches.keys():
    print('{} is engaged to {} !'.format(man, Matches[man]))
