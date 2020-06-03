score = input("Enter Score:")
scoref = float(score)
if scoref > 1.0:
    print("Error: Score out of Range")
    quit()
elif scoref < 0:
    print("Error: Score out of Range")
    quit()
elif scoref >= 0.9:
    print("A")
elif scoref >= 0.8:
    print("B")
elif scoref >= 0.7:
    print("C")
elif scoref >= 0.6:
    print("D")
elif scoref < 0.6:
    print("F")
