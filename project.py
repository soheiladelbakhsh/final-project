def main():
    while True:
        print('defcription: wellcome to Movie Assistance. \nIn every step shows that how treat\nin each step for going 1 step back press B and for quit Press Q.')
        display_items()
        user_choice = User_choice('which section would you choose')
        if user_choice == '1':
            show_time_preiod()
            random_movie = Random_movie()
        elif user_choice == '2':
            explore = Explore()
        elif user_choice == '3':
            relative_favorite = Relative_favorite()
        elif user_choice == '4':
            find_via_cast = Find_via_cast()
        elif user_choice == '5':
            watchList = WatchList()
        else:
            quit_proccess()


def display_items():
    '''
    show the first 5 item:
    1. Show Random Movies
    2. Explore:
          Popular Film OF THis week
    3. Show Fim that relative to favorite movie of user
    4. find film via cast can be 1 cast or more
    5. WatchList
    6. quit
    '''
    ...


def User_choice(item):
    '''
    get the user choise of which 5 first itenm was selected 
    return 1 to 6
    '''
    return input(item)


def show_time_preiod():
    print('for skip press enter')
    start_date = input('release date(print year):')
    end_date = input('end date(print year):')
    return start_date, end_date


def Random_movie():
    ...



def Explore():
    ...


def Relative_favorite():
    ...


def Find_via_cast():
    ...


def WatchList():
    ...


def quit_proccess():
    ...


main()