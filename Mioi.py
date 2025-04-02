notes = int(input())
allNotes = [input()[::-1] for _ in range(notes)]
allNotes.reverse()
print("".join(allNotes))