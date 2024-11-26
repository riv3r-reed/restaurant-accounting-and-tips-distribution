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
            subtotal += (order-tips)/1.14975
        return subtotal        
def balance(start,end,card,deposit,payout,delivery,kitchen_tips,card_tips):
    return (start+end)-(card+deposit+payout+delivery+kitchen_tips)+card_tips
def create_tip_profile(staff_type):
    staff_tips = {}
    staff_num = 0
    while True:
        staff_name = input("{}: ".format(staff_type))
        if staff_name == "0":
            break
        staff_tips[staff_name] = 0
        staff_num += 1
    return staff_tips,staff_num
def tips_per_person(tips_now,tips_before):
    tips = tips_now-tips_before
    
    k_staff_tips, k_staff_num = create_tip_profile("kitchen staff")
    w_staff_tips, w_staff_num = create_tip_profile("waitors")
    
    for staff in k_staff_tips:
        k_staff_tips[staff] = round(tips*0.2/k_staff_num,2)
    
    for staff in w_staff_tips:
        w_staff_tips[staff] = round(tips*0.8/w_staff_num,2)
    
    return k_staff_tips,w_staff_tips
def main():
    delivery_completion = int(input("Is delivery already calculated? (yes - 1, no - 0): "))
    if delivery_completion == 1:
        delivery_sum = float(input("Enter delivery: "))
    else:
        delivery_sum = 0
        i = 0
        while i < 4:
            try:
                platform = input("delivery platform: ")
            except TypeError:
                print("Plz enter a valid platform name.")
            try:
                delivery_sum += delivery(platform)
                i += 1
            except NameError:
                print("Plz enter a valid platform name.")

    start = float(input("start: "))
    end = float(input("end: "))
    card = float(input("card: "))
    deposit = float(input("deposit: "))
    payout = float(input("payout: "))
    card_tips = float(input("tips: "))
    num_kitchen = int(input("Num of kitchen staffs: "))
    num_waitor = int(input("Num of waitors: "))
    tips_assignment = tips_per_person(card_tips, num_kitchen, num_waitor)
    kitchen_tips = tips_assignment["kitchen"]*num_kitchen
    balance_sum = balance(start,end,card,deposit,payout,delivery_sum,kitchen_tips,card_tips)
    
    print("Delivery: ",round(delivery_sum,2))
    print("Balance: ",round(balance_sum,2))
    print("Tips for each kitchen staff: ", tips_assignment["kitchen"])
    print("Tips for each waitor: ", tips_assignment["waitor"])
main()