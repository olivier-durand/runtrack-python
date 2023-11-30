def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)
        elif (note % 5) >= 3:
            notes_arrondies.append((note // 5 + 1) * 5)
        else:
            notes_arrondies.append(note)

    return notes_arrondies

notes_eleves = [11, 43, 74, 91, 89]
notes_arrondies = arrondir_notes(notes_eleves)
print(notes_arrondies)


    