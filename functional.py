
# Part 1: Initialization
Men = ['Mike', 'Harvey', 'Louis', 'Logan']
Women = ['Rachel', 'Donna', 'Katrina', 'Sheila']

# Part 3: Preferences
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
