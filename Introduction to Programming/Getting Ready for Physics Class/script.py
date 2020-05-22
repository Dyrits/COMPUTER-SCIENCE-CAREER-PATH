train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
c = 3 * 10 ** 8


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

print(f_to_c(100))


def c_to_f(c_temp):
  f_temp = 32 + 9 / 5 * c_temp
  return f_temp

print(c_to_f(0))


def get_force(mass, acceleration):
  return mass * acceleration


train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")


def get_energy(mass, c):
  return mass * c * c


bomb_energy = get_energy(bomb_mass, c)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")


def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance


train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} of work over {train_distance} meters.")

