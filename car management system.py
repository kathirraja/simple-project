class Places(object):
    def __init__(self, pname , n = None, p = None,avail_car = None):
        self.place_name = pname
        self.next_p = n
        self.prev_p = p
        self.available_car = avail_car
    def get_next_p(self):    return self.next_p
    def set_next_p(self, n): self.next_p = n
    def get_prev_p(self):    return self.prev_p
    def set_prev_p(self, p): self.prev_p = p
    def get_place( self):    return self.place_name    
    def set_place(self, pname): self.place_name = pname
    def set_avail_car(self, set_avail_car) : self.available_car = avail_car

class Route(Places):
    def __init__(self, r = None, e = None ):
        self.root = r
        self.end = e
    def append_place(self,pname):
        if self.root == None:
            this_p = Places(pname)
            self.root = this_p
        else :
            this_p = self.root
            while this_p.get_next_p() != None:
                this_p = this_p.get_next_p()
            new_p = Places(pname,None,this_p)
            this_p.set_next_p(new_p)
            self.end = new_p
    def display_p(self):
        this_p = self.root
        while this_p:
            print this_p.get_place(),'->',
            this_p = this_p.get_next_p()
        print 'reverse'
        this_p = self.end
        while this_p != None:
            print this_p.get_place(),'<-',
            this_p = this_p.get_prev_p()

class Cars(Places):
    def __init__(self,cname,tearn = 0,n = None):
        self.car_name = cname
        self.car_total_earning = tearn
        self.next_c = n
    def get_next_car(self): return self.next_c
    def set_next_car(self,n): self.next_c = n
    def get_car_name(self): return self.car_name
    def set_car_name(self,cname): self.car_name = cname
    def get_te(self) : return self.car_total_earning

class Clist(Cars):
    def __init__(self, r = None):
        self.rootc = r
    def append_car(self,cname):
        if self.rootc == None:
            newcar = Cars(cname)
            self.rootc = newcar
        else:
            thiscar = self.rootc
            while thiscar.get_next_car()!= None:
                thiscar = thiscar.get_next_car()
            newcar = Cars(cname,0,None)
            thiscar.set_next_car(newcar)
    def display_c(self):
        thiscar = self.rootc
        while thiscar:
            print thiscar.get_car_name(),thiscar.get_te(),'->',
            thiscar = thiscar.get_next_car()


