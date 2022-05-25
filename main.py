from DTO import Hat, Supplier, Order

from Repository import repo
import sys

if __name__ == '__main__':
    args = sys.argv
    repo.set_fields(args[4])
    repo.create_tables()
    file = open(args[1], 'r')
    # file = open('/home/spl211/Desktop/work4/config.txt', 'r')
    line = file.readline()
    parts = line.split(',')
    hats_size = int(parts[0])
    suppliers_size = int(parts[1])

    for i in range(hats_size):
        line = file.readline()
        parts = line.split(',')
        parts[3] = parts[3].split('\n')[0]
        repo.hats.insert(Hat(*parts))

    for i in range(suppliers_size):
        line = file.readline()
        parts = line.split(',')
        parts[1] = parts[1].split('\n')[0]
        repo.suppliers.insert(Supplier(*parts))

    file.close()
    # order_file = open('/home/spl211/Desktop/work4/orders.txt', 'r')
    order_file = open(args[2], 'r')
    output_file = open(args[3], "w")
    lines = order_file.readlines()
    order_id = 1
    for line in lines:
        parts = line.split(',')
        topping = parts[1].split('\n')[0]
        hat = repo.hats.find_by_topping(topping)
        repo.orders.insert(Order(order_id, parts[0], hat.id))
        order_id = order_id + 1
        repo.hats.update_quantity(hat.id)
        order = ""+str(topping)+","+str(repo.suppliers.find(hat.supplier).name)+","+str(parts[0])+"\n"
        output_file.write(order)


    order_file.close()





