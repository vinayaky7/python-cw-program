# input the cost price and selling price, and determine made profit or loss and calulate it how much it is or loss he incured.
# SP > CP = Profit, Profit = SP - CP
# SP < CP = Loss, Loss = CP - SP

Cost_Price = int(input("Enter a cost price:"))
Selling_Price = int(input("Enter a selling price:"))

if Selling_Price > Cost_Price :
    profit = Selling_Price - Cost_Price
    print("We have made the profit of:", profit)

elif Selling_Price < Cost_Price :
    loss = Selling_Price - Cost_Price
    print("We have incured loss of: ", loss)

else:
    print("We have made no profit and no loss") 


