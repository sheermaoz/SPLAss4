from dao import Clinic, Dao, Logistic, Vaccine, Supplier
import sys
from repository import repo

def send_order():
    pass

def receive_order():
    pass

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
        repo.clinics.insert(Clinic(*data[i].split(",")))
    for i in range (sumEntries[1], sumEntries[2]):
        repo.suppliers.insert(Supplier(*data[i].split(",")))
    for i in range (sumEntries[2], sumEntries[3]):
        repo.vaccines.insert(Vaccine(*data[i].split(",")))
    

def main():
    repo.create_tables()
    insert(sys.argv[1])

if __name__ == "__main__":
    main()