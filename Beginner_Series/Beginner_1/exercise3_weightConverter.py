weight = int(input("Weight: "))
type = input("(K)g or (L)bs: ")

if type == "l" or type == "L":
    weight_k = weight * 0.45
    print("Weight in Kg: ",weight_k)
elif type == "k" or type == "K":
    weight_l = weight / 0.45
    print("Weight in Lbs: ",weight_l)