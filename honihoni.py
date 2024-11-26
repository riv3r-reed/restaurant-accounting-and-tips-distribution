"""import csv
from datetime import datetime, date"""

TAX = 1.14975

class Staff():
    
    def __init__(self,name,tip = 0):
        self.name = name
        self.tip = tip
    
    def __str__(self):
        return self.name + ": " + str(self.tip)
    
    def __repr__(self):
        return self.__str__()
        
class HoniHoni():
    k_staffs = []
    w_staffs = []
    def __init__(self,k_staffs,w_staffs):
        HoniHoni.k_staffs = k_staffs
        HoniHoni.w_staffs = w_staffs


    def create_tip_profile(staff_type):
        staff_num = 0
        deja_staff = []
        for staff in HoniHoni.k_staffs:
            deja_staff.append(staff.name)
        for staff in HoniHoni.w_staffs:
            deja_staff.append(staff.name)
            
        shift_staff = []
        while True:
            staff_name = input("{} (enter 0 to end): ".format(staff_type))
            if staff_name == "0":
                break
            if staff_name not in deja_staff:
                if staff_type == "kitchen staff":
                    HoniHoni.k_staffs.append(Staff(staff_name,0))
                if staff_type == "waiters":
                    HoniHoni.w_staffs.append(Staff(staff_name,0))
                    
            shift_staff.append(staff_name)
            staff_num += 1
        
        return shift_staff,staff_num

    def tips_per_person(tips_now,tips_before):
        tips = tips_now-tips_before
        
        k_shift_staff, k_staff_num = HoniHoni.create_tip_profile("kitchen staff")
        w_shift_staff, w_staff_num = HoniHoni.create_tip_profile("waiters")
        
        for staff in HoniHoni.k_staffs:
            if staff.name in k_shift_staff:
                staff.tip += round(tips*0.2/k_staff_num,2)
        
        for staff in HoniHoni.w_staffs:
            if staff.name in w_shift_staff:
                staff.tip += round(tips*0.8/w_staff_num,2)

    @staticmethod
    def delivery(platform):
        if platform not in ["door", "skip", "uber", "tm"]:
            raise NameError("Platform name not found.")
        if platform == "door" or platform == "skip":
            subtotal = 0
            while True:
                order = float(input("order total (enter 0 to end): "))
                if order == 0.0:
                    print(platform,": ",subtotal)
                    break
                subtotal += order
            return subtotal
            
        if platform == "uber" or platform == "tm":
            subtotal = 0
            while True:
                order = float(input("order total (enter 0 to end): "))
                if order == 0.0:
                    print(platform,": ",subtotal)
                    break
                tips = float(input("order tips: "))
                subtotal += (order-tips)/TAX
            return subtotal     
    
    @staticmethod
    def balance(start,end,card,deposit,payout,delivery,kitchen_tips,card_tips,TM_tips):
        return (start+end)-(card+deposit+payout+delivery+kitchen_tips)+card_tips+TM_tips-kitchen_tips

def create_staff_profile():
    with open('tips.csv', 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Tips'])
        for staff in HoniHoni.k_staffs:
            writer.writerow([staff.name, staff.tip])
        for staff in HoniHoni.w_staffs:
            writer.writerow([staff.name, staff.tip])

def main():
    while True:
        task = input("Delivery - 1, Tips - 2, Balance - 3, End - 0: ")
        if task == "1":
            delivery_sum = 0
            i = 0
            while i < 4:
                try:
                    platform = input("delivery platform: ")
                except TypeError:
                    print("Plz enter a valid platform name.")
                try:
                    delivery_sum += HoniHoni.delivery(platform)
                    i += 1
                except NameError:
                    print("Plz enter a valid platform name.")
            print("Delivery: ",round(delivery_sum,2))
        
        if task == "2":
            card_tips = float(input("Current card tip: "))
            tm_tips = float(input("Current TM tips: "))
            tips_now = card_tips + tm_tips
            tips_before = float(input("Tips at last shift: "))
            HoniHoni.tips_per_person(tips_now,tips_before)
            for staff in HoniHoni.k_staffs:
                print(staff)
            for staff in HoniHoni.w_staffs:
                print(staff)
            
        if task == "3":
            start = float(input("start: "))
            end = float(input("end: "))
            card = float(input("card: "))
            delivery_sum = float(input("delivery: "))
            deposit = float(input("deposit: "))
            payout = float(input("payout: "))
            card_tips = float(input("Card tips: "))
            TM_tips = float(input("TM tips: "))
            kitchen_tips = 0
            for k_staff in HoniHoni.k_staffs:
                kitchen_tips += k_staff.tip
            balance_sum = HoniHoni.balance(start,end,card,deposit,payout,delivery_sum,kitchen_tips,card_tips,TM_tips)
            print("Balance: ",round(balance_sum,2))
        
        if task == "0":
            break

if __name__ == "__main__":
    main()