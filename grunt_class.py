class Grunts:
    """Modeling a Grunt enemy."""

    def __init__(self, name, rank, type, armor_color, shield, grenade_count,
                 shield_strength, health_points, points, *weapon):
        """Establish the attributes of a Grunt."""
        self.name = name.title()
        self.rank = rank.title()
        self.type = type.title()
        self.armor_color = armor_color.title()
        self.shield = shield
        self.grenade_count = grenade_count
        self.shield_strength = shield_strength
        self.health_points = health_points
        self.points = points
        self.weapon = weapon

    # def get_weapon(self):                         Trying to produce a variable to clean up formatting when weapons
    #     for x in self.weapon:                     print out.
    #         print(f"{x.title()}")
    #         return x
    #
    # y = get_weapon
    # y(grunt_major)

    def describe_grunt_minor(self):
        """Describe an Grunt Minor"""
        print(f"The following is a breakdown of the enemy known as: {self.name.title()}")
        print(
            f"Name: {self.name} "
            f"\nRank: {self.rank} "
            f"\nType: {self.type} "
            f"\nArmor Color: {self.armor_color} "
            f"\nShield: {self.shield} "
            f"\nGrenade Count: {self.grenade_count} "
            f"\nShield Strength: {self.shield_strength} "
            f"\nHealth: {self.health_points} "
            f"\nPoints: {self.points}")
        print("\nWeapon(s): ".strip())
        for item in self.weapon:
            print(f"{item.title()}")

    def describe_grunt_major(self):
        """Describe a Grunt Major"""
        print(f"The following is a breakdown of the enemy known as: {self.name.title()}")
        print(
            f"Name: {self.name} "
            f"\nRank: {self.rank} "
            f"\nType: {self.type} "
            f"\nArmor Color: {self.armor_color} "
            f"\nShield: {self.shield} "
            f"\nGrenade Count: {self.grenade_count} "
            f"\nShield Strength: {self.shield_strength} "
            f"\nHealth: {self.health_points} "
            f"\nPoints: {self.points}")
        print("\nWeapon(s): ".strip())
        for item in self.weapon:
            print(f"{item.title()}")

    def describe_grunt_specops(self):
        """Describe a Grunt Spec Ops"""
        print(f"The following is a breakdown of the enemy known as: {self.name.title()}")
        print(
            f"Name: {self.name} "
            f"\nRank: {self.rank} "
            f"\nType: {self.type} "
            f"\nArmor Color: {self.armor_color} "
            f"\nShield: {self.shield} "
            f"\nGrenade Count: {self.grenade_count} "
            f"\nShield Strength: {self.shield_strength} "
            f"\nHealth: {self.health_points} "
            f"\nPoints: {self.points}")
        print("\nWeapon(s): ".strip())
        for item in self.weapon:
            print(f"{item.title()}")


grunt_minor = Grunts(
              'grunt minor',
              'minor',
              'light infantry',
              'orange',
              None,
              None,
              100,
              15,
              'needler',
              'plasma pistol',
            )



grunt_major = Grunts(
              'grunt major',
              'major',
              'light infantry',
              'red',
              None,
              2,
              None,
              150,
              25,
              'plasma pistol',
              'needler',
            )

grunt_specops = Grunts(
              'grunt spec ops',
              'special operations',
              'special infantry',
              'black',
              None,
              4,
              None,
              150,
              25,
              'fuel rod gun',
              'plasma pistol',
              'needler',
            )

# grunt_major.y()

grunt_major.describe_grunt_major()
print("\n")
grunt_minor.describe_grunt_minor()
print("\n")
grunt_specops.describe_grunt_specops()
