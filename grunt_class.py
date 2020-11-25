class Grunts:
    """Modeling a Grunt enemy."""

    def __init__(self, name, tier, type, armor_color, shield, weapon, weapon2,
                 weapon3, grenade_count, shield_strength, health_points, points):
        """Establish the attributes of a Grunt."""
        self.name = name.title()
        self.tier = tier.title()
        self.type = type.title()
        self.armor_color = armor_color.title()
        self.shield = shield
        self.weapon = weapon.title()
        self.weapon2 = weapon2.title()
        self.weapon3 = weapon3.title()
        self.grenade_count = grenade_count
        self.shield_strength = shield_strength
        self.health_points = health_points
        self.points = points

    def describe_grunt_specops(self):
        """Describe a Spec Ops Grunt"""
        print(f"The following is a breakdown of the enemy known as: {self.name.title()}")
        print(
            f"Name: {self.name} "
            f"\nTier: {self.tier} "
            f"\nType: {self.type} "
            f"\nArmor Color: {self.armor_color} "
            f"\nShield: {self.shield} "
            f"\nWeapons: {self.weapon}\n\t\t {self.weapon2}\n\t\t {self.weapon3} "
            f"\nGrenade Count: {self.grenade_count} "
            f"\nShield Strength: {self.shield_strength} "
            f"\nHealth: {self.health_points} "
            f"\nPoints: {self.points}"
        )

    def describe_grunt_major(self):
        """Describe a Grunt Major"""
        print(f"The following is a breakdown of the enemy known as: {self.name.title()}")
        print(
            f"Name: {self.name} "
            f"\nTier: {self.tier} "
            f"\nType: {self.type} "
            f"\nArmor Color: {self.armor_color} "
            f"\nShield: {self.shield} "
            f"\nWeapons: {self.weapon}\n\t\t {self.weapon2}\n\t\t {self.weapon3} "
            f"\nGrenade Count: {self.grenade_count} "
            f"\nShield Strength: {self.shield_strength} "
            f"\nHealth: {self.health_points} "
            f"\nPoints: {self.points}"
        )

    def describe_grunt_minor(self):
        """Describe a Grunt Minor"""
        print(f"The following is a breakdown of the enemy known as: {self.name.title()}")
        print(
            f"Name: {self.name} "
            f"\nTier: {self.tier} "
            f"\nType: {self.type} "
            f"\nArmor Color: {self.armor_color} "
            f"\nShield: {self.shield} "
            f"\nWeapons: {self.weapon}\n\t\t {self.weapon2}\n\t\t {self.weapon3} "
            f"\nGrenade Count: {self.grenade_count} "
            f"\nShield Strength: {self.shield_strength} "
            f"\nHealth: {self.health_points} "
            f"\nPoints: {self.points}"
        )


grunt_minor = Grunts(
              'grunt minor',
              'minor',
              'light infantry',
              'orange',
              None,
              'needler',
              'plasma pistol',
              'n/a',
              1,
              None,
              100,
              15
            )

grunt_major = Grunts(
              'grunt major',
              'major',
              'light infantry',
              'red',
              None,
              'plasma pistol',
              'needler',
              'n/a',
              2,
              None,
              150,
              25
            )

grunt_specops = Grunts(
              'grunt spec ops',
              'special operations',
              'special infantry',
              'black',
              None,
              'fuel rod gun',
              'plasma pistol',
              'needler',
              4,
              None,
              150,
              25
            )

grunt_major.describe_grunt_major()
print("\n")
grunt_minor.describe_grunt_minor()
print("\n")
grunt_specops.describe_grunt_specops()