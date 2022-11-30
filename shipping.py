#Ground Shipping
def ground_shipping(weight):
  cost_ground = 0.00
  if weight <= 2.0:
    cost_ground += 20.00 + (1.50 * weight)
  elif weight <= 6.0:
    cost_ground += 20.00 + (3.00 * weight)
  elif weight <= 10.0:
    cost_ground += 20.00 + (4.00 * weight)
  elif weight > 10:
    cost_ground += 20.00 + (4.75 * weight)
  else:
    print("Error")
  return cost_ground

#premium ground
cost_prem_ground = 125.00

#drone shipping
def drone_shipping(weight):
  cost_drone = 0.00
  if weight <= 2.0:
    cost_drone += 4.50 * weight
  elif weight <= 6.0:
    cost_drone += 9.00 * weight
  elif weight <= 10.0:
    cost_drone += 12.00 * weight
  elif weight > 10.0:
    cost_drone += 14.25 * weight
  else:
    print("Error")
  return cost_drone


def cheapest_shipping(weight):
  price_ground = ground_shipping(weight)
  price_drone = drone_shipping(weight)
  print("Price ground shipping: $" + str(price_ground))
  print("Price preimum ground shipping: $" + str(cost_prem_ground))
  print("Price drone shipping: $" + str(price_drone))

  price_list = {'Ground shipping':price_ground, 'Premium ground shipping': cost_prem_ground, 'Drone shipping': price_drone}
  print("Cheapest shipping option: ", (min(price_list,  key=price_list.get), price_list[min(price_list, key=price_list.get)]))

#Cheapest method of shipping a 4.8lb package + cost

cheapest_shipping(4.8)

print("\n")
#Cheapest method of shipping a 41.5lb package
cheapest_shipping(41.5)



  