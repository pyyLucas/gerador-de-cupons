import random
import string
import csv

def generate_coupon(length=8):
    # gerando uma sequencia aleatória de caracteres
    letters_and_digits = string.ascii_letters + string.digits
    coupon = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return coupon

def save_to_csv(coupons):
    with new_func() as file:
        writer = csv.writer(file)
        writer.writerow(["Cupom"])
        for coupon in coupons:
            writer.writerow([coupon])
    print("Cupons salvos com sucesso!")

def new_func():
    return open('coupons.csv', 'w', newline='')

# gerando 100 cupons
coupons = [generate_coupon() for i in range(100)]
save_to_csv(coupons)
