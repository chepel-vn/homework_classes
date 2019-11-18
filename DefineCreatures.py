class Creature:
  fed = False
  name = ''
  weight = 0
  sex = False


  def __init__(self, name, sex = False):
    self.name = name
    self.sex = sex
    self.fed = False
    self.weight = 0

  def feed(self):
    self.fed = True

  def speak(self):
    return "Я существо , я пока не знаю как я подаю голос"

  def speak_status(self):
    status_string = "\"" + self.name + "\""
    if self.sex:
      if self.fed:
        status_string += " накормлен"
      else:
        status_string += " голоден"
    else:
      if self.fed:
        status_string += " накормлена"
      else:
        status_string += " голодна"

    return  status_string

class CreatureGiveMilk(Creature):
  milk_yield_one = 0

  def milk(self):
    return self.milk_yield_one

class Cow(CreatureGiveMilk):
  def __init__(self, name, sex=False):
    super(Cow, self).__init__(name, sex)
    self.milk_yield_one = 80

  def speak(self):
    return "Му-у"

class Sheep(Creature):
  # Count of wool per one haircut
  wool = 5

  def speak(self):
    return "Меее-ее"

  def haircut(self):
    return self.wool

class Goat(CreatureGiveMilk):
  def __init__(self, name, sex=False):
    super(Goat, self).__init__(name, sex)
    self.milk_yield_one = 300

  def speak(self):
    return "Беее-ее"

class Birds(Creature):
  # Count of eggs for one time
  count_eggs_one = 0

  def flap_wings(self):
    print('Машу крыльями')

  def lay_eggs(self):
    return self.count_eggs_one

class Goose(Birds):
  def __init__(self, name, sex=False):
    super(Goose, self).__init__(name, sex)
    self.count_eggs_one = 6

  def speak(self):
    return "Га-га-га"

class Chicken(Birds):
  def __init__(self, name, sex=False):
    super(Chicken, self).__init__(name, sex)
    self.count_eggs_one = 15

  def speak(self):
    if self.sex:
      return "Кукарекуууууу"
    else:
      return "Ко-ко-ко"

class Duck(Birds):
  def __init__(self, name, sex=False):
    super(Duck, self).__init__(name, sex)
    self.count_eggs_one = 10

  def speak(self):
    return "Кря-кря"

def main():
  all_creatures = list()
  goose1 = Goose('Серый', True)
  goose1.weight = 3.5
  all_creatures.append(goose1)

  goose2 = Goose('Белый', True)
  goose2.weight = 2.6
  all_creatures.append(goose2)

  cow = Cow('Манька')
  cow.weight = 700
  all_creatures.append(cow)

  sheep1 = Sheep('Барашек', True)
  sheep1.weight = 90
  all_creatures.append(sheep1)

  sheep2 = Sheep('Кудрявый', True)
  sheep2.weight = 120
  all_creatures.append(sheep2)

  chick1 = Chicken('Ко-Ко')
  chick1.weight = 0.8
  all_creatures.append(chick1)

  chick2 = Chicken('Кукареку', True)
  chick2.weight = 0.6
  all_creatures.append(chick2)

  goat1 = Goat('Рога')
  goat1.weight = 60
  all_creatures.append(goat1)

  goat2 = Goat('Копыта')
  goat2.weight = 70
  all_creatures.append(goat2)

  duck = Duck('Кряква')
  duck.weight = 1.2
  all_creatures.append(duck)

  # All creatures are speaking
  for creature in all_creatures:
    add_str = ""
    if not creature.sex:
      add_str = "а"
    print("\"{0}\" прокричал{1} {2}".format(creature.name, add_str, creature.speak()))
    # print("Вес \"{0}\" составляет {1} кг".format(creature.name, creature.weight))
  print("")

  summa_weights = 0
  creature_max_weight = all_creatures[0]
  for creature in all_creatures:
    if type(creature) in (Duck, Goose, Chicken):
      if not creature.sex:
        print("\"{0}\" снесла {1} яиц".format(creature.name, creature.lay_eggs()))
        creature.feed()
    elif type(creature) is Sheep:
      print("C \"{0}\" состригли {1} шерсти".format(creature.name, creature.haircut()))
    elif type(creature) in (Goat, Cow):
      print("C \"{0}\" надой составил {1} молока".format(creature.name, creature.milk()))
      creature.feed()

    summa_weights += creature.weight;

    if creature_max_weight.weight < creature.weight:
      creature_max_weight = creature


    print(creature.speak_status())


  print("\nОбщий вес животных составляет {0} кг".format(summa_weights))
  print("Максимальный вес в {0} кг у животного \"{1}\"".format(creature_max_weight.weight, creature_max_weight.name))


main()