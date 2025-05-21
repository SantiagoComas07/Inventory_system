'''Exercise of python -- 4 week --Santiago Andrés Comas Durán'''
# This function show the menu of the system
def menu():
    print("\n")
    print("---------------  Inventory system  --------------")
    print("- Add product                                 (1)")
    print("- search product                              (2)")
    print("- Update cost of the product                  (3)")
    print("- delete product of inventary                 (4)")
    print("- Calculate the general cost of the inventary (5)")
    print("- Exit                                        (6)")
    print("------------------------------------------------")
    print("\n")
# This is the function for add products in the main list
def add_product():
    global products, names_list
    Auxiliary_dic={}
    try: 
        name =input("What is the name of product? ")
        cost=float(input("What is the cost of it? "))
        cantidad=int(input("How many is it? "))
    except ValueError:
     print("Value Error...")
     for component in products:
         for element in component.values():
             names_list.append(list(map(str,element)))
    if name is not names_list:
         Auxiliary_dic['name']= name
         Auxiliary_dic['cost']= cost
         Auxiliary_dic['cantidad']= cantidad
         products.append(Auxiliary_dic)
    else:
        print("product is in inventary")  
#This is the function for search products in the main list 
def search_product(item):
    flag_search= False
    global products
    for component in products:
        for element in component.values():
            if element == item:
                flag_search=True
                print("\n")
                print(component)
                print("\n")
                break 
    if flag_search:
        pass
    else:
        print("The product is not in inventary")
#This is the function for update the cost of the product in the main list
def update_cost(item_2, NewCost):
    global products
    noExiste=True
    for component in products:
      for element in component.values():
        if element == item_2:
            noExiste=False
            if NewCost > 0:
                component['cost']=NewCost
                print(component)
                print("\n")
                print("cost updated...")
            else:
                print("Error... Negative number")
        break
    if noExiste:
        print(f"There is not a product called {item_2} in the inventary") 
# This function delete products of the inventary
def delete_product(item_delete):
    global products
    flag_delete=False
    for component in products:
      for element in component.values():
        if element == item_delete:
            flag_delete=True
            products.remove(component)
            print(f"product deleted...{component}")
        break 
    if flag_delete:
        pass
    else:
        print("The product is not in inventary")
#Calculate the full-value of the inventary
def calculate():
    global products
    cost_component=0
    cantidad_component=0
    sum=0
    for component in products:
        cost_component=component['cost']
        cantidad_component=component['cantidad']
        sum+= (cost_component*cantidad_component)
    print(f"The total cost of products of the inventary is: {sum:.02f}")
products=[]
names_list=[]
while True:
    menu()
    op=input("Get an option: ")
    if op =='1':
            add_product()
    elif op =='2':
        if len(products)>=5:
            try:
                product_search=input("What is the product that you want to search? ")
                search_product(product_search)
            except ValueError:
                print("Incorrect information, the information must be a string")
        else:
            print("You must add 5 products to use the other function of the system")
    elif op=='3':
        if len(products)>=5:
            product_search_2=input("What is the product that you want to search?: ")
            cost_update=float(input("add the new cost: "))
            update_cost(product_search_2, cost_update)
        else:
            print("You must add 5 products to use the other function of the system")
    elif op=='4':
        if len(products)>=5:
            delete=input("What is the name of the product to delete? ")
            delete_product(delete)
        else:
            print("You must add 5 products to use the other function of the system")
    elif op=='5':
        if len(products)>=5:
            calculate()
        else:
            print("You must add 5 products to use the other function of the system")
    elif op=='6':
        break
    else:
        print("Invalid option")