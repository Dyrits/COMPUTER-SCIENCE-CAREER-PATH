def cost_ground_shipping(weight):
  prices = {10: 4.75, 6: 4, 2: 3, 0: 1.5}
  flat_charge = 20
  for key, value in prices.items():
    if weight > key:
      cost = weight * value + flat_charge
      break
  return cost


def cost_drone_shipping(weight):
  prices = {10: 14.25, 6: 12, 2: 9, 0: 4.5}
  flat_charge = 0
  for key, value in prices.items():
    if weight > key:
      cost = weight * value + flat_charge
      break
  return cost


premium_ground_shipping = 125


def cheapest(weight):
  shipping_options = {"ground": cost_ground_shipping(
      weight), "premium ground": premium_ground_shipping, "drone": cost_drone_shipping(weight)}
  cheapest = min(shipping_options.values())
  for key, value in shipping_options.items():
    if value == cheapest:
      return f"The cheapest way to ship the {weight} pound package is using the {key} shipping method. It will cost ${value}."
      break
