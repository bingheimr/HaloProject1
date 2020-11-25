class Elites:
    """Modeling Elite enemies."""

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


    def describe_elite_minor(self):
        """Describe an Elite Minor"""
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

    def describe_elite_major(self):
        """Describe an Elite Major"""
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

    def describe_elite_spec_ops(self):
        """Describe a Spec Ops Elite."""
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

elite_minor = Elites(
              'elite minor',
              'minor',
              'infantry',
              'blue',
              True,
              'plasma rifle',
              'plasma pistol',
              'n/a',
              2,
              200,
              200,
              100
            )

elite_major = Elites(
              'elite major',
              'major',
              'infantry',
              'red',
              True,
              'plasma rifle',
              'plasma pistol',
              'n/a',
              2,
              300,
              200,
              150
            )

elite_spec_ops = Elites(
              'elite spec ops',
              'special operations',
              'special infantry',
              'black',
              True,
              'double plasma rifle',
              'fuel rod gun',
              'n/a',
              4,
              400,
              200,
              100
            )

elite_major.describe_elite_major()
print("\n")
elite_minor.describe_elite_minor()
print("\n")
elite_spec_ops.describe_elite_spec_ops()
