
def valid_card(number):

    total = 0
    for i in number[::2]:
        x = int(i) * 2

        if x > 9:
            for j in str(i):
               total += int(j)
        else:
            total += int(i)

    for i in number[1::2]:
        total += int(i)

    return total



def main():
    number = input('Please enter your credit card number: ')

    if valid_card(number) % 10 == 0:
        print('The card is valid.') 
    else:
        print('It is not a valid card.')

main()