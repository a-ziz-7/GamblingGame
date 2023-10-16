import random
import math

balance = 100
price = 6
# 7     win in 0%
# 6.75  win in 17%
# 6.74  win in 25%
# 6.73  win in 37%
# 6.72  win in 47%
# 6.715 win in 50%
# 6.71  win in 55%
# 6.7   win in 62%


def generate():
    chances = {0: 20, 1: 20, 2: 20, 3: 15, 4: 10, 5: 10, 6: 5}
    array_of_chances = []
    for key in chances:
        array_of_chances.extend([key]*chances[key])
    return array_of_chances


array_of_chances = generate()


def get_lines(num):
    ans = []
    global balance
    global price
    if isinstance(num, str):
        temp = num.split(" ")
        for i in range(len(temp)):
            try:
                v = int(temp[i])
            except:
                continue
            if len(str(v)) < 4:
                for i in str(v):
                    v = int(i)
                    if ((v-1) not in ans and 0 < v < 4 and balance >= price):
                        ans.append(v-1)
                        balance -= price
        return ans
    else:
        return ans


def main():
    global balance, price
    print(
        f'''
    Welcome!!!
    There are 3 lines and 3 colums and each spot can take a value from 0 to 6.
    You bet {price}$ on the line(s) you want.
    The sum of 3 numbers in a chosen line(s) is the amount you win.
    '''
    )
    array_of_chances = generate()
    print("Balance: " + str(balance))
    ask = input(f"Play for {price}$ per line?\n")
    if ask.lower() != "no":
        response = True
        num_lines = input("What lines? (1 2 and/or 3)\n")
        lines = get_lines(num_lines.strip())

    else:
        response = False
    asking = 10

    while response and (balance >= price or len(lines) > 0):
        out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        amount_won_counter = 0
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                out[i][j] = random.choice(array_of_chances)
                print(str(out[i][j]), "| ", end="")
            print(
                "  " + str(sum(out[i])) + ("$ won" if i in lines else "") + "\n"+"-"*13)
            if i in lines:
                amount_won_counter += sum(out[i])
        print(
            f"Spent: {(price*len(lines))} Amount Won: {amount_won_counter}\n")
        balance += amount_won_counter
        print("Balance: " + str(balance)+"$")
        if asking == 0:
            ask = input(f"Play for {price}$ per line?\n")
            if ask.lower() != "no":
                response = True
            else:
                response = False
                break
            asking = 10
        num_lines = input("What lines? (1 2 and/or 3)\n")
        lines = get_lines(num_lines.strip())
        asking -= 1
    if balance < price:
        print("Not enough money")
    print("Game Over!!!")


def bot_main():
    x = 100
    global balance, price, array_of_chances
    # print("Balance: " + str(balance))
    num_lines = "1 2 3"
    lines = get_lines(num_lines.strip())
    out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while (balance >= price or len(lines) > 0) and x > 0:
        amount_won_counter = 0
        for i in range(3):
            for j in range(3):
                out[i][j] = random.choice(array_of_chances)
            if i in lines:
                amount_won_counter += sum(out[i])
        balance += amount_won_counter
        # print("Balance: " + str(int(balance)))
        num_lines = "1 2 3"
        lines = get_lines(num_lines.strip())
        x -= 1
        # time.sleep(0.01)
    # if balance < price:
    #     print("Not enough money")
    # print("Balance: " + str(int(balance)))
    # print("Game Over!!!")


f = 0
w = 0


def checker(b):
    global f, w
    if b < 100:
        f += 1
        return f"fail {b}"
    else:
        w += 1
        return f"win {b}"


if __name__ == "__main__":
    # main()
    # bot_main()
    ans = []
    for i in range(1000):
        balance = 100
        bot_main()
        ans.append((price, checker(int(balance))))
    # print(ans)
    print(f, w)
