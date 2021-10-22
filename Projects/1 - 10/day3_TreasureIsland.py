print('''
              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
''')
print()
print("Welcome to Treasure Island.\nYou arrive just as the sun is setting and need to find the treasure before it gets dark.")

choice1 = input("Will you go left into the island or right to look on the shore? (type 'left' or 'right') ")
if choice1 == "left":
    choice2 = input("You find an abandoned shack will you go in or search outside? (type 'in' or 'outside') ")
    if choice2 == "in":
        choice3= input("You see three boxes, red, blue and yellow, which one will you open? (type 'red', 'blue' or 'yellow') ")
        if choice3 == "yellow":
            print("You find the treasure!\nYou Win!")
        elif choice3 == "red":
            print("The box explodes, you're in pieces. Game Over!")
        elif choice3 == "blue":
            print("Blue smoke starts plumming out, you can't breath. Game Over!")
    else:
        print("A wild tiger appears and attacks you. Game Over!")
else:
    print("You get attacked by a shark. Game Over!")