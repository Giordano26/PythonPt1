largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numc = int (num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = numc
    if smallest is None:
        smallest = numc
    if numc >= smallest:
        smallest = smallest
    if numc < smallest:
        smallest = numc
    if numc <= largest:
        largest = largest
    if numc > largest:
        largest = numc
 
print("Maximum is", largest)
print("Minimum is", smallest)
