import os

camel = r"""
Switching on the camera to Collin's habitat...

 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
           
Look at that! Our little camel is sunbathing!
"""

lion = r"""
Switching on the camera to Lincoln's habitat...

                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
        
Lincoln the Lion is roaring!
"""

deer = r"""
Switching on the camera to Daniela's habitat...

   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
          
Our 'Bambi' looks hungry. Let's go to feed it!
"""

goose = r"""
Switching on the camera to Gustavo's habitat...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
    
Gustavo is staring intently at you... Maybe it's time to change the channel?
"""

bat = r"""
Switching on the camera to Beethoven's habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
                   
Beethoven looks like it's doing fine.
"""

rabbit = r"""
Switching on the camera to Rilley's habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )

It looks like we will soon have more rabbits!
"""


animals = [camel, lion, deer, goose, bat, rabbit]

# write your code here

print("\033[32mWelcome to the Zoo!\n\033[0m")

print("Enter \033[31mexit\033[0m to logoff system\n\033[34m")

print(r"""+-----------------------------------------------+
| Collin the Camel = 1    Gustavo the Goose = 4 |
| Lincoln the Lion = 2    Beethoven the Bat = 5 |
| Daniela the Deer = 3    Rilley the Rabbit = 6 |
+-----------------------------------------------+
""", "\033[0m")


print("\033[32mEnter the animal's number you'd like to view:\n\033[0m")

while True:
    user_input = input()
    if user_input != "exit":
      user_input = int(user_input) - 1
      if int(user_input) > 5 or int(user_input) == -1 :
        print("\033[31m")
        print(user_input + 1, "is not a valid number!\n\033[0m")
        
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[32mWelcome to the Zoo!\n\033[0m")
        print("Enter \033[31mexit\033[0m to logoff system\033[34m")
        print("\033[34m")
        print(r"""+-----------------------------------------------+
| Collin the Camel = 1    Gustavo the Goose = 4 |
| Lincoln the Lion = 2    Beethoven the Bat = 5 |
| Daniela the Deer = 3    Rilley the Rabbit = 6 |
+-----------------------------------------------+
""", "\033[0m")
        print("\033[32mEnter the animal's number you'd like to view:\n\033[0m")
        print(animals[int(user_input)])
        
    else:
      print("\033[31m\nSee you later!\n")
      break
