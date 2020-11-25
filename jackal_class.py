class Jackals:
    """Modeling Jackal enemies."""

    def __init__(self, name, rank, type, armor_color, shield, grenade_count,
                 shield_strength, health_points, points, *weapon):
        """Establish the attributes of a Jackal."""
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


    def describe_jackal_minor(self):
        """Describe an Jackal Minor"""
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
        for item in self.weapon:
            print(f"\nWeapon(s): {item.title()}".strip())


    def describe_jackal_major(self):
        """Describe an Jackal Major"""
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
        for item in self.weapon:
            print(f"\nWeapon(s): {item.title()}".strip())


jackal_major = Jackals(
                'jackal major',
                'major',
                'light infantry',
                'yellow',
                True,
                0,
                None,
                150,
                45,
                'plasma pistol',
        )

jackal_minor = Jackals(
                'jackal minor',
                'minor',
                'light infantry',
                'blue',
                True,
                0,
                None,
                100,
                30,
                'plasma pistol',
        )


jackal_minor.describe_jackal_minor()
print("\n")
jackal_major.describe_jackal_major()

