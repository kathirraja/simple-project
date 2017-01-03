class Bank(object):

    def __init__(self, cid, acc_no, name, balance, pwd ,n = None):
        self.cid = cid
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.pwd = pwd
        self.next = n

    def get_data(self):
        return self.cid,self.acc_no,self.name,self.balance,self.pwd

    def get_cid(self):
        return self.cid
    
    def get_pwd(self):
        return self.pwd
    
    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def set_cid(self,cid):
        self.cid = cid

    def set_acc_no(self,acc_no):
        self.acc_no = acc_no

    def set_name(self, name):
        self.name = name

    def set_balance(self, balance):
        self.balance = balance

    def set_pwd(self, pwd):
        self.pwd = pwd
        
    def encrypte(self, pwd):
        d = ''
        for l in pwd:
            d += chr(ord(l)+5)
        return d
    
class List(Bank):

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add (self, cid, acc_no, name, balance, pwd):
        new_customer = Bank(cid, acc_no, name, balance, pwd, self.root)
        self.root = new_customer
        self.size += 1

    def display(self):
        this = self.root
        print '\nCID\tACCOUNT_NO\tNAME\tBALANCE\t\tPassword'
        while this:
            cid,acc_no,name,balance,pwd=this.get_data()
            print cid,'\t',acc_no,'\t\t',name,'\t',balance,'\t\t',pwd
            this = this.get_next()

    def remove(self, cid):
        this = self.root
        prev = None
        while this:
            if this.get_cid() == cid :
                #print this.get_cid(),cid
                if prev:
                    prev.set_next(this.get_next())
                else:
                    self.root = this.get_next()
                return True
            else:
                prev = this
                this = this.get_next()
        return False 

    def  modify(self,cid):
        this = self.root
        while this:
            if this.get_cid() == cid:
                print '\n\t1.Change Name\n\t2.Change Account no\n\t3.change balance\n\t4.change Password'
                ch = int(raw_input('Select your option : '))
                if ch == 1:
                    this.set_name(raw_input('Enter Name : '))
                elif ch == 2:
                    this.set_acc_no(raw_input('Enter Account No : '))
                elif ch == 3:
                    this.set_balance(int(raw_input('Enter Balance : ')))
                elif ch == 4:
                    pwd = raw_input('Enter old password : ')
                    #print this.encrypte(pwd),this.get_pwd()
                    if this.encrypte(pwd) == this.get_pwd():
                        this.set_pwd(this.encrypte(raw_input('Enter New Password : ')))
                        print 'Password has been reset'
                return True
            else :
                this = this.get_next()
        return False

    def moneyWithdraw(self,cid):
        this = self.root
        while this:
            if this.get_cid() == cid:
                amount = float(raw_input('Enter Amount : '))
                if this.get_balance() >= amount:
                    this.set_balance(this.get_balance()-amount)
                    print 'Monney Withdrawrn '
                    return True
                else:
                    print 'Insufficient Balance'
        print 'Invalid Customer id'


record = List()
record.add(11,11011,'Madhu',1000,record.encrypte('kathir'))
record.add(12,11012,'giri',30000,record.encrypte('kathir'))
record.add(13,11013,'karthi',103200,record.encrypte('kathir'))
record.add(14,11014,'kumar',120000,record.encrypte('kathir'))
record.add(15,11015,'kishor',1000460,record.encrypte('kathir'))
record.add(16,11016,'bala',780000,record.encrypte('kathir'))
record.display()

print '\t modify'
record.modify(12)
record.display()
record.remove(11)
record.display()
record.remove(123)
record.display()
record.remove(15)
record.display()
print  '+++++++'
#print record.get_data()
