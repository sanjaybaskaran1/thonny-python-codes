print("made  with ❤️ ")
print('''           

             __        __        __        __
 .*.        /~ .~\    /~  ~\    /~ .~\    /~  ~\
 ***       '      `\/'      *  '      `\/'      *
  V       (                .*)(               . *)
/\|/\      \     LOVE  . *./  \   CALCULATOR   */
  |         `\ .      . .*/'    `\ .      . .*/'       .*.
  |           `\ * .*. */' _    _ `\ * .*. */'         ***
                `\ * */'  ( `\/'*)  `\ * */'          /\V
                  `\/'     \   */'    `\/'              |/\
                            `\/'                        |
                            LOVES



          ''')
your_name = input("ENTER YOUR NAME? ").lower()
their_name = input("ENTER THERE NAME? ").lower()

combined_name = your_name + their_name

t = combined_name.count("n")  # count no.of 't' in the combined name
r = combined_name.count("a")  # count no.of 'r' in the combined name
u = combined_name.count("v")  # count no.of 'u' in the combined name
e = combined_name.count("e")  # count no.of 'e' in the combined name

true = t + r + u + e  # it will add how many ['t' 'r' 'u' 'e'] in the combined name written as number

l = combined_name.count("h")  # count no.of 'l' in the combined name
o = combined_name.count("e")  # count no.of 'o' in the combined name
v = combined_name.count("r")  # count no.of 'v' in the combined name
e = combined_name.count("s")  # count no.of 'e' in the combined name

love = l + o + v + e  # it will add how many ['l' 'o' 'v' 'e'] in the combined name written as number

true_love = int(str(true) + str(love))
if true_love >= 1 and true_love <= 10:
    print("please try to understand each other")
    print('''     
     8      /```|     .@@@@@,     8
     8     |  66|_    @@@@@@@@,   8 (\/)
     8     C     _)   aa`@@@@@@   8  \/
     8(\/)  \ ._|    (_   ?@@@@   8
    |8:\/:~:~) /:~:~: =' @@@@~:~:~8
    |8::::::/\\/`\;_:::\ (__::::::8
    |8:::::| \ '|___/` \\// `\):::8
    |8::::|| | '|::/ /  ^^  \ \:::8
    |8::::|| | ' \:| \__/\__/ |:::8
    |8o:::|\ \  ' |:\_\    /_/::::8o
    |"8o:::=\ \===::/`\`%%`/'\::::"8o
    |\"8o~|  \_\  \|   `""`   |:~:~\8o
    \ \"8o\   )))  \           \::::"8o
     \ \"8o\`.  \   \           \::::"8o
      \|~~~~~| -|| -|mmmmmmmmmmmm~~~~~|
       `~~~~~|  ||  |~~|  |~|  |~~~~~~
     jgs     |  ||  |  |__| |__|
             |  ||  |  \  | \  |
             |__||__|  (~~^\(~~^\
             (   \   \  `-._)`-._)
              `-._)-._)

                 ''')


elif true_love > 10 and true_love <= 20:
    print(f"your love score is {75} your love is like a snake and frog")
    print('''                    /  \  /  \  /  \  /  \
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \  \____
                   |/   \_/   \_/   \_/   \    o \
                                           \_____/--<            _ _
          (oTo)
       _.-( _ )-._
      `/`( '-' )`\`
         /'---'\
       __\     /__
  jgs  \_/     \_/

               ''')

elif true_love <= 60:
    print(f"your love score is {90} you and your partner are like moon and the  stars")
    print('''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@,""""""@@@@@@@@@@@@
          @@@@@@@@@@@@"-    "@@@@@@@@@@       "@@@@@@@@@@@
          @@@@@@@@@@@(   ^^^ )@@@@@@@@@      ' @@@@@@@@@@@
          @@@@@@@@@@@(  (    0@@@@@@@@@,      (@@@@@@@@@@@
          @@@@@@@@@@@)  )  _/@@@@@@@@@@@m       "@@@@@@@@@
          @@@@@@@@@@(__/  (@@@@@@@@@@@@@'         @@@@@@@@
          @@@@@@@@@@"       )@@@@@@@@@@'          @@@@@@@@
          @@@@@@@@@'         \@@@@@@@@'           @@@@@@@@
          @@@@@@@@@'          )@@@@@@'   A        @@@@@@@@
          @@@@@@@@@         ,@@@@@@@"  /@@        @@@@@@@@
          @@@@@@@@@,        @_____"  =,           @@@@@@@@
          @@@@@@@@@@               :',@@@@        `@@@@@@@
          @@@@@@@@@'       @@@@@@@@@@@@@@@         M@@@@@@
          @@@@@@@@'        `@@@@@@@@@@@@@"        ,@@@@@@@
          @@@@@@@@          @@@@@@@@@@@@"      /  @@@@@@@@
          @@@@@@@@          @@@@@@@@@@@"          @@@@@@@@
          @@@@@@@@|         @@@@@@@@@@"      /    @@@@@@@@
          @@@@@@@@|         @@@@@@@@@"     ,"    .@@@@@@@@
          @@@@@@@@|         @@@@@@@@'    .@@     `@@@@@@@@
          @@@@@@@@|         @@@@@@@@m    `@@@,    @@@@@@@@
          @@@@@@@@|        :@@@@@@@@@m    )@@.   )@@@@@@@@

                ''')


else:
    print(f"YOUR LOVE  🫶   SCORE IS {true_love} YOU MADE FOR EACHOTHER")
    print('''

           ////
          |6 6|
          \ - /
   .@@@. __) (__
   @6 6@/  \./  \
   @ = @ :  :  : \
   _) (_'|  :  |) )
 /' \./ '\  :  |_/
/ /\ _ /\ \=o==|)
\ \ )  (/ /%|%%'
 '7/    \7%%|%%'
   |    |`%%|%%'
   |    |`%%|%%'
   |    | %%|%%
   |_.._| /_|_\
             ''')





