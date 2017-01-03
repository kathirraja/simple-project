class Theater(object):

    def __init__(self):
        self.seat = [[1,2,3,4,5],[[6,7,8,9,10],[11,12,13,14,15]]]
        self.total_avail = 15
        self.fc_avail = 5
        self.sc_avail = 10
        self.sc_row_status = [5,5]

    def get_total_avail(self):
        return self.total_avail

    def get_fc_avail(self):
        return self.fc_avail

    def set_fc_avail(self,nos):
        self.fc_avail -= nos
        self.total_avail -= nos

    def get_sc_avail(self):
        return self.sc_avail

    def set_sc_avail(self,nos):
        self.sc_avail -= nos
        self.total_avail -= nos

    def get_sc_row_status(self):
        return self.sc_row_status
    
    def get_seat_status(self):
        return self.seat

class Booking(object):
    def __init__(self):
        self.id = 1
        self.total_money = 0
        self.booking_history = {0:'Sorry insufficient seats'}
        self.cancel_history = {}
        self.discount = {'d10':.1,'d20':.2,'d30':.3,'D10':.1,'D20':.2,'D30':.3,'n':0,'N':0}
    def get_seat(self,screen):
        return screen.get_seat_status()
    def get_b_dict(self):
    	return self.booking_history
    def get_c_dict(self):
    	return self.cancel_history
    def get_history(self,bid):
        return self.booking_history[bid]
    def book_seat_fc(self,nos,screen,sn):
        if nos > screen.get_fc_avail():
            #screen.sc_avail -=1
            return 0
            #print 'seats not enough'
        else :
            ns =nos
            dis = raw_input('Entet Discount Id [d10,d20,d30,n] : ')
            ss = screen.get_seat_status()
            booked_seat_list = []
            booking_details = {}
            fc = ss[0]
            print nos
            while nos > 0:
                for i in range(len(fc)):
                    if fc[i] > 0:
                        booked_seat_list.append(fc[i])
                        fc[i] = -fc[i]
                        nos -= 1
                        screen.fc_avail -= 1
                        #print nos
                    if nos <= 0:
                        break            
            print booked_seat_list
            booking_details['price'] = ns * 110
            booking_details['booked_seats'] = booked_seat_list
            booking_details['Discount'] = float(ns)*110.0*self.discount[dis]
            booking_details['total amount'] = booking_details['price'] - booking_details['Discount']
            self.total_money += booking_details['total amount']
            booking_details['nos'] = ns
            booking_details['scr_no']=sn
            self.booking_history[self.id] = booking_details
            self.id += 1
            '''print screen.get_seat_status()
            for key in self.booking_history.keys():
                print key,self.booking_history[key]
            #print self.booking_history'''
            return self.id-1

        
    def book_seat_sc(self,nos,screen,sn):
        if nos > screen.get_sc_avail():
            print screen.get_sc_avail()
            return 0
        else :
            ns =nos
            dis = raw_input('Entet Discount Id [d10,d20,d30,n] : ')
            ss = screen.get_seat_status()
            booked_seat_list = []
            booking_details = {}
            scr = ss[1]
            r1 = scr[0]
            r2 = scr[1]
            print 'nos ',nos
            print 'sc_avail',screen.get_sc_avail()
            seats_avail = screen.get_sc_row_status()
            if nos <= seats_avail [0]:
                print 'if --- nos,',nos,seats_avail[0]                
                seats_avail[0] -= nos
                while nos > 0:
                    for i in range(len(r1)):
                        if r1[i] > 0:
                            booked_seat_list.append(r1[i])
                            r1[i] = -r1[i]
                            nos -= 1
                            #print nos
                        if nos <= 0:
                            break
            
            
            elif nos <= seats_avail [1]:
                print 'elif --- ',nos,seats_avail[1]
                seats_avail[1] -= nos
                while nos > 0:
                    for i in range(len(r2)):
                        if r2[i] > 0:
                            booked_seat_list.append(r2[i])
                            r2[i] = -r2[i]
                            nos -= 1
                            #print nos
                        if nos <= 0:
                            break
            
            else:
                print 'else --- ',nos,seats_avail
                while nos > 0:
                    for i in range(len(r1)):
                        if r1[i] > 0:
                            seats_avail[0] -= 1
                            screen.sc_avail -=1
                            booked_seat_list.append(r1[i])
                            r1[i] = -r1[i]
                            nos -= 1
                            #print nos
                        if nos <= 0:
                            break
                    for i in range(len(r2)):
                        if r2[i] > 0:
                            seats_avail[1] -= 1
                            booked_seat_list.append(r2[i])
                            r2[i] = -r2[i]
                            nos -= 1
                            #print nos
                        if nos <= 0:
                            break
                    #print 'seats booked ',booked_seat_list
            screen.sc_avail = seats_avail[0]+seats_avail[1] 
            #print booked_seat_list
            booking_details['price'] = ns * 100
            booking_details['booked_seats'] = booked_seat_list
            booking_details['Discount'] = float(ns)*100.0*self.discount[dis]
            booking_details['total amount'] = booking_details['price'] - booking_details['Discount']
            self.total_money += booking_details['total amount']
            booking_details['nos'] = ns
            booking_details['scr_no']=sn
            self.booking_history[self.id] = booking_details
            self.id += 1
            '''for key in self.booking_history.keys():
                print key,self.booking_history[key]
            print 'seat status ',screen.get_seat_status()
            print 'sc_avail    ',screen.get_sc_avail()
            print 'sc_row_avail',screen.get_sc_row_status()
            print 'total_avail ',screen.total_avail
            print 'cbid        ',self.id'''
            return self.id-1

    def cancel(self,bid,screen):
        bd = self.booking_history[bid]
        bl = bd['booked_seats']
        ns = bd['nos']
        seat = screen.seat
        fc = seat[0]
        sc = seat[1]
        r1 = sc [0]
        r2 = sc [1]
        scrs = screen.sc_row_status
        for i in range(len(fc)):
            #print fc[i]
            if -fc[i] in bl:
                fc[i] = -fc[i]
                screen.total_avail += 1
                screen.fc_avail += 1
                ns -= 1
            if ns <=0:
                break
        for i in range(len(r1)):
            #print r1[i]
            if -r1[i] in bl:
                r1[i] = -r1[i]
                ns -= 1
                screen.total_avail += 1
                screen.sc_avail += 1
                scrs[0] += 1
            if ns <=0:
                break
            
        for i in range(len(r2)):
            #print r2[i]
            if -r2[i] in bl:
                r2[i] = -r2[i]
                ns -= 1
                screen.total_avail += 1
                screen.sc_avail += 1
                scrs[1] += 1
            if ns <=0:
                break
        self.cancel_history[bid] = self.booking_history[bid]
        del self.booking_history[bid]
        self.total_money -= self.cancel_history[bid]['total amount']*.9
                         
book = Booking()
screen = []
n = int(raw_input('Enter no of screen : '))
for i in range(n):
    screen.append(Theater())

while True :
    print '\n+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+'
    print '\nTotal = Rs.',book.total_money,'/-\n'
    for i in range(n):
        print '\tScreen',i+1,'\tFirst class\t(',screen[i].fc_avail,')\t',screen[i].get_seat_status()[0]
        print '\tScreen',i+1,'\tSecond class\t(',screen[i].sc_avail,')\t',screen[i].get_seat_status()[1]
    #print '\tScreen 2 First class  (',screen[1].fc_avail,')'#,screen[1].get_seat_status()[0]
    #print '\tScreen 2 Second class (',screen[1].sc_avail,')'#,screen[1].get_seat_status()[1]
    print '\tBooked ID ',book.get_b_dict().keys()[1:]
    print '1. Book'
    print '2. Cancel'
    print '3. Booking History'
    print '4. Cancel History'
    ch = int(raw_input('\tselect Option : '))
    if ch == 1:
        scr = int(raw_input('\tSelect screen  : '))
        cls = int(raw_input('\t1. First Calss \n\t2. Second Class \n\tselect class : '))
        nos = int(raw_input('Enter number of seats : '))
        if cls == 1:
            print book.get_history(book.book_seat_fc(nos,screen[scr-1],scr))
        elif cls == 2:
            print book.get_history(book.book_seat_sc(nos,screen[scr-1],scr))#book.book_seat_sc(nos,screen[scr-1],scr)
    elif ch == 2:
        bid = int(raw_input('Enter booking id :'))
        if bid not in book.get_b_dict.keys()[1:]:
            print '/t',bid,'is invalid booking id'
        else:
            print 'history ',book.get_history(bid)
            #b = book.get_history(bid)
            book.cancel(bid,screen[book.get_history(bid)['scr_no']-1])
    elif ch == 3:
        print '\n\n\tID\tSCREEN\tNOS\tPRICE\tDISCOUNT\tTOTAL\tSEATS BOOKED'
        for key in book.get_b_dict().keys()[1:]:
            d = book.booking_history[key]
            print '\t',key,'\t',d['scr_no'],'\t',d['nos'],'\t',d['price'],'\t',d['Discount'],'\t\t',d['total amount'],'\t',d['booked_seats'],'\t'
    elif ch == 4:
        print '\n\n\tID\tSCREEN\tNOS\tPRICE\tDISCOUNT\tTOTAL\tSEATS BOOKED'
        for key in book.get_b_dict().keys():
            d = book.cancel_history[key]
            print '\t',key,'\t',d['scr_no'],'\t',d['nos'],'\t',d['price'],'\t',d['Discount'],'\t\t',d['total amount'],'\t',d['booked_seats'],'\t'
