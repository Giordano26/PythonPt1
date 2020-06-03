def computepay (hours,rate):
    if h > 40:
        payment = (rate*40)+(((hours-40)*rate)*1.5)
        return payment
    else:
        payment = rate * hours
        return payment

hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rate:")
r = float(rt)

p = computepay(h,r)
print("Pay", p)