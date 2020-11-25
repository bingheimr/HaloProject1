class Elites:
    """Modeling Elite enemies."""

    def __init__(self, name, rank, type, armor_color, shield, grenade_count,
                 shield_strength, health_points, points, *weapon):
        """Establish the attributes of an Elite."""
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

    def describe_elite_minor(self):
        """Describe an Elite Minor"""
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

    def describe_elite_major(self):
        """Describe an Elite Major"""
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

    def describe_elite_spec_ops(self):
        """Describe a Spec Ops Elite."""
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
            f"\nPoints: {self.points} ")
        print("\nWeapon(s): ".strip())
        for item in self.weapon:
            print(f"{item.title()}")


elite_minor = Elites(
              'elite minor',
              'minor',
              'infantry',
              'blue',
              True,
              2,
              200,
              200,
              100,
              'plasma rifle',
              'plasma pistol',
        )

elite_major = Elites(
              'elite major',
              'major',
              'infantry',
              'red',
              True,
              2,
              300,
              200,
              150,
              'plasma rifle',
              'plasma pistol',
            )

elite_spec_ops = Elites(
              'elite spec ops',
              'special operations',
              'special infantry',
              'black',
              True,
              4,
              400,
              200,
              100,
              'double plasma rifle',
              'fuel rod gun',
              'plasma pistol',
            )

elite_major.describe_elite_major()
print("\n")
elite_minor.describe_elite_minor()
print("\n")
elite_spec_ops.describe_elite_spec_ops()
