# Saam Beam
# 9/28/2024
# The program calculates a certain amount of bottles

# Variables used in the program
total_bottles = 0
counter = 0
today_bottles = 0
total_payout = 0
keep_going = "y"


# Function to display a certain amount of bottles sold a day and add them up after each day
while keep_going == "y":
# Get the number of bottles sold today
  today_bottles = int(input("How many bottles sold today? "))
  
# Add the number of bottles sold today to the total number of bottles sold in total
  total_bottles = today_bottles + total_bottles
  
# Each bottle cost $0.10 so multiply the number of bottles sold today by 0.10 to get the    total payout for the day
  total_payout = (today_bottles * 0.1) + total_payout

# Count the day
  counter = counter + 1
  print("\nDay #:",counter)

# Display all bottles sold so far and total cash earned so far
  print(("Total bottles sold:"), total_bottles, ("\nTotal cash earned:"), total_payout)

# Ask if the user wants to do another day
  keep_going = input("\nDo you want to enter another weeks data? y or n \n")