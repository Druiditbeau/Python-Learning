weight = 2
cost_groundshipping = 0
cost_groundshipping_premium = 125 #Ground Shipping Premium IS STATIC
cost_droneshipping = 0

#Ground Shipping (pricing table)
 
if weight <= 2:
  cost_groundshipping = weight*1.5+20
elif weight <= 6 and weight > 2:
  cost_groundshipping = weight*3+20
elif weight <=10 and weight > 6:
  cost_groundshipping = weight*4+20
elif weight > 10:
  cost_groundshipping = weight*4.75+20

print("If you choose Ground shipping the cost will be: " + str(cost_groundshipping) + "€")
 
#Ground Shipping Premium (Pricing Table)

print("If you choose Ground shipping Premium the cost will be: " + str(cost_groundshipping_premium) + "€")

#Drone Shipping (Pricing Table)

if weight <= 2:
  cost_droneshipping = weight*4.5
elif weight > 2 and weight <= 6:
  cost_droneshipping = weight*9
elif weight > 6 and weight <= 10:
  cost_droneshipping = weight*12
elif weight > 10:
  cost_droneshipping = weight*14.25

print("If you choose Drone shipping the cost will be: " + str(cost_droneshipping) + "€")

#Cheapest option selector

if cost_groundshipping < cost_droneshipping and cost_groundshipping < cost_groundshipping_premium:
  print("Based on the weight of your products your best solution is...")
  print("Ground Shipping for: " + str(cost_groundshipping) + "€")
elif cost_groundshipping_premium < cost_droneshipping and cost_groundshipping_premium < cost_groundshipping:
  print("Based on the weight of your products your best solution is...")
  print("Ground Shipping Premium for: " + str(cost_groundshipping_premium) + "€")
elif cost_droneshipping < cost_groundshipping_premium and cost_droneshipping < cost_groundshipping:
  print("Based on the weight of your products your best solution is...")
  print("Drone Shipping for: " + str(cost_droneshipping) + "€")
