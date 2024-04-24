class Star_Cinema:
    hall_list=[]

    @classmethod
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
        self._seats={}
        self._show_list=[]
        Star_Cinema.entry_hall(self)
        super().__init__()

    def entry_show(self,id,movie_name,time):
        show_details=(id,movie_name,time)
        self._show_list.append(show_details)
        self._seats[id]=[["F" for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self,show_id,seat_tuples):
        if show_id not in self._seats:
            raise ValueError("You have given an invalid show ID")
        for row, col in seat_tuples:
            if row<0 or row>=self._rows or col<0 or col>=self._cols:
                raise ValueError('You have choosen an invalid seat')
            if self._seats[show_id][row][col]!='F':
                raise ValueError("This seat is already Booked")
            self._seats[show_id][row][col]="B"
    
    def view_show_list(self):
        return  self._show_list
    
    def view_available_seats(self,show_id):
        if show_id not in self._seats:
            raise ValueError("You have given an invalid show ID")
        return self._seats[show_id]
    


cinema_hall=Star_Cinema()
hall1=Hall(5,5,111)
hall1.entry_show('1','Jawan','11:00')
hall1.entry_show('2','Invictus','15:00')
hall1.entry_show('3','Netri The Leader','18:00')

# hall2=Hall(5,4,112)
# hall1.entry_show('04','Jawan','11:00')
# hall1.entry_show('05','Invictus','15:00')
# hall1.entry_show('06','Netri The Leader','18:00')



while(True):
    print('\nWelcome to XYZ Cinema Hall -_-\n')
    num=int(input('1.View All show Today \n2.View Available Seats\n3.Book Ticket\n4.Exit\n\nEnter Option: '))
    if num==1:
        print(hall1.view_show_list())
    elif num==2:
        show = input('Please Provide the Show ID(1-3): ')
        if show not in ['1', '2', '3']:
            print("Invalid Show")
        else:
            print(hall1.view_available_seats(show))
    elif num==3:
        print('Please enter the show id and seats (row,col row,col ..) number.\nEx: Show Id = 05 and Seat Numbers = 0,0, 0,1')
        show_id = input('Show ID: ')
        if show_id not in ['1', '2', '3']:
            print("Invalid Show")
            continue
        seats_num = input("Seat Numbers: ")
        seats_num = [tuple(map(int, seat.split(','))) for seat in seats_num.split()]
        hall1.book_seats(show_id, seats_num)
        print('Your tickets are booked, Thank You')
    elif num==4:
        print("Thank you for visiting XYZ Cinema")
        break
    else:
        print('Invalid Input')