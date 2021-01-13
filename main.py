from dto import *
import sys
from repository import repo

global total_inventory, total_demand, total_received, total_sent
total_inventory = 0
total_demand = 0
total_received = 0
total_sent = 0

def send_order(split):
    amount = int(split[1])
    clinic = repo.clinics.find(location=split[0])[0]
    repo.clinics.update({"demand":clinic.demand-amount}, {"id":clinic.id})
    Vaccines_by_date =  repo.vaccines.find_all_by_date()
    global total_sent
    total_sent += amount
    global total_inventory
    total_inventory -= amount
    global total_demand
    total_demand -= amount
    
    logistic = repo.logistics.find(id=clinic.logistic)[0]
    repo.logistics.update({'count_sent': logistic.count_sent+amount}, {'id': logistic.id})
    ind = 0
    while amount>0:
        if Vaccines_by_date[ind].quantity <= amount:
            repo.vaccines.delete(id=Vaccines_by_date[ind].id)
        else:
            repo.vaccines.update({'quantity':Vaccines_by_date[ind].quantity-amount}, {'id':Vaccines_by_date[ind].id})
        amount-=Vaccines_by_date[ind].quantity
        ind += 1


def receive_order(split):
    amount = int(split[1])
    Supp = repo.suppliers.find(name=split[0])[0]
    count_received = repo.logistics.find(id=Supp.logistic)[0].count_received
    repo.logistics.update({'count_received':count_received+amount},{'id':Supp.logistic})
    repo.vaccines.insert(Vaccine(0, split[2], Supp.id, amount))
    global total_received
    total_received += amount
    global total_inventory
    total_inventory += amount
    
def write_to_file(path):
    with open(path, 'a') as file:
        file.write(str(total_inventory) + "," + 
            str(total_demand) + "," + str(total_received) + "," + str(total_sent) + "\n")


def get_orders(path, out_path):
    with open(path) as file:
        data = file.readlines()
    for line in data:
        split = line.split(",")
        if len(split) == 2:
            send_order(split)
        else:
            receive_order(split)
        write_to_file(out_path)

def insert(path):
    with open(path) as file:
        data = file.readlines()
    amount_of_entries = [int(a) for a in data[0].split(",")]
    data = data[-1:0:-1]
    amount_of_entries = amount_of_entries[::-1]
    sumEntries = []
    sumEntries.append(amount_of_entries[0])
    for i in range(1, len(amount_of_entries)):
        sumEntries.append(sumEntries[i-1]+ amount_of_entries[i])
    
    for i in range (amount_of_entries[0]):
        repo.logistics.insert(Logistic(*data[i].split(",")))
    for i in range (sumEntries[0], sumEntries[1]):
        clinic = Clinic(*data[i].split(","))
        global total_demand
        total_demand += clinic.demand
        repo.clinics.insert(clinic)
    for i in range (sumEntries[1], sumEntries[2]):
        repo.suppliers.insert(Supplier(*data[i].split(",")))
    for i in range (sumEntries[2], sumEntries[3]):
        vaccine = Vaccine(*data[i].split(","))
        global total_inventory
        total_inventory += vaccine.quantity
        repo.vaccines.insert(vaccine)
    

def main():
    open(sys.argv[3], 'w').close()
    repo.create_tables()
    insert(sys.argv[1])
    get_orders(sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
