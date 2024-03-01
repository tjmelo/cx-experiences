sequenceString = 'abcdefghijlmno'
print("Original sequence: {}".format(sequenceString))

print(len(sequenceString))

slicingSequence1 = sequenceString[3:10]
print('Sequence 1: {}' .format(slicingSequence1))

slicingSequence2 = sequenceString[0:5]
print('Sequence 2: {}' .format(slicingSequence2))

slicingSequence3 = sequenceString[:4]
print('Sequence 3: {}' .format(slicingSequence3))

slicingSequence4 = sequenceString[10:]
print('Sequence 4: {}' .format(slicingSequence4))
