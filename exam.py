'''
import turtle


def staircase(t, num, tread, riser):
    for i in range(num):
        stair(t, tread, riser)
    return


def stair(t, tread, riser):
    t.down()
    t.forward(tread)
    t.right(90)
    t.forward(riser)
    t.left(90)
    return

s = turtle.screen()
t = turtle.Turtle()
staircase()


def first_last(string_list):
    returnList = []
    for string in string_list:
        if string != '' and string[0] == string[-1]:
            returnList.append(string)
    return returnList




def vowel_tracker(words):
    init_vowel = 0
    ending_vowel = 0
    vowel_lst = 'aeiouAEIOU'
    for i in words:
        if i[0] in vowel_lst:
            init_vowel += 1
        if i[-1] in vowel_lst:
            ending_vowel += 1
    return [init_vowel, ending_vowel]





# review this
def number_luck(lucky, unlucky):
    num = int(input('give me a number between 2 and 12'))
    int_loop=[]
    int_loop.append(lucky)
    int_loop.append(unlucky)
    for i in int_loop:
        if i in lucky:
            if i == num:
                print('number is lucky')
        elif i in unlucky:
            if i == num:
                print('number is unlucky')
        else:
            print('your number is boring')
    return

l = [3,4,5]
u = [6,7,8]



def month_info(medium_lenght):
    month = str(input('What month is it?'))
    days = int(input('How many days in a month'))
    if days < medium_lenght:
        print('month is short')
    elif days == medium_lenght:
        print('month is medium')
    else :
        print('month is long')
    return month

print(month_info(30))

'''

#exam 2

#remenmber the .readline() command, it will read a whole line of a text file and store it in a list


