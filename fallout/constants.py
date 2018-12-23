# encoding: utf-8
from fallout.enums import *  # noqa


# Body part modifiers (ranged, melee, critical)
BODY_PARTS_MODIFIERS = {
    PART_TORSO: (0, 0, 0),
    PART_LEGS: (-10, -5, 10),
    PART_ARMS: (-20, -10, 20),
    PART_HEAD: (-30, -15, 25),
    PART_EYES: (-40, -20, 30),
}

# Body part randomly hit if not targetted (body part, chance)
BODY_PARTS_RANDOM_CHANCES = (
    (PART_EYES, 1),
    (PART_HEAD, 5),
    (PART_ARMS, 10),
    (PART_LEGS, 15),
    (PART_TORSO, 100),
)

# Racial traits (bonus, min, max)
RACES_STATS = {
    RACE_HUMAN: {
        SPECIAL_STRENGTH: (0, 1, 10),
        SPECIAL_PERCEPTION: (0, 1, 10),
        SPECIAL_ENDURANCE: (0, 1, 10),
        SPECIAL_CHARISMA: (0, 1, 10),
        SPECIAL_INTELLIGENCE: (0, 1, 10),
        SPECIAL_AGILITY: (0, 1, 10),
        SPECIAL_LUCK: (0, 1, 10),
        RESISTANCE_ELECTRICITY: (30, -100, 100),
        PERK_RATE: (2, None, None),
    },
    RACE_GHOUL: {
        SPECIAL_STRENGTH: (0, 1, 8),
        SPECIAL_PERCEPTION: (0, 4, 13),
        SPECIAL_ENDURANCE: (0, 1, 10),
        SPECIAL_CHARISMA: (0, 1, 6),
        SPECIAL_INTELLIGENCE: (0, 2, 10),
        SPECIAL_AGILITY: (0, 1, 10),
        SPECIAL_LUCK: (0, 5, 12),
        RESISTANCE_RADIATION: (80, -100, 100),
        RESISTANCE_POISON: (30, -100, 100),
        PERK_RATE: (3, None, None),
    },
    RACE_SUPER_MUTANT: {
        SPECIAL_STRENGTH: (0, 5, 13),
        SPECIAL_PERCEPTION: (0, 1, 11),
        SPECIAL_ENDURANCE: (0, 4, 11),
        SPECIAL_CHARISMA: (0, 1, 7),
        SPECIAL_INTELLIGENCE: (0, 1, 8),
        SPECIAL_AGILITY: (0, 1, 8),
        SPECIAL_LUCK: (0, 1, 10),
        STATS_DAMAGE_RESISTANCE: (25, -100, 100),
        RESISTANCE_RADIATION: (50, -100, 100),
        RESISTANCE_POISON: (20, -100, 100),
        RESISTANCE_FIRE: (25, -100, 100),
        HIT_POINTS_PER_LEVEL: (2, None, None),
        PERK_RATE: (3, None, None),
    },
    RACE_DEATHCLAW: {
        SPECIAL_STRENGTH: (0, 6, 14),
        SPECIAL_PERCEPTION: (0, 4, 12),
        SPECIAL_ENDURANCE: (0, 1, 13),
        SPECIAL_CHARISMA: (0, 1, 3),
        SPECIAL_INTELLIGENCE: (0, 1, 4),
        SPECIAL_AGILITY: (0, 6, 16),
        SPECIAL_LUCK: (0, 1, 10),
        STATS_DAMAGE_RESISTANCE: (40, -100, 100),
        STATS_MELEE_DAMAGE: (5, None, None),
        STATS_DAMAGE_THRESHOLD: (4, None, None),
        HIT_POINTS_PER_LEVEL: (2, None, None),
        PERK_RATE: (3, None, None),
    },
    RACE_ROBOT: {
        SPECIAL_STRENGTH: (0, 7, 12),
        SPECIAL_PERCEPTION: (0, 7, 12),
        SPECIAL_ENDURANCE: (0, 7, 12),
        SPECIAL_CHARISMA: (0, 1, 1),
        SPECIAL_INTELLIGENCE: (0, 1, 12),
        SPECIAL_AGILITY: (0, 1, 12),
        SPECIAL_LUCK: (0, 5, 5),
        STATS_DAMAGE_RESISTANCE: (40, -100, 100),
        STATS_HEALING_RATE: (0, 0, 0),
        RESISTANCE_RADIATION: (100, -100, 100),
        RESISTANCE_POISON: (100, -100, 100),
        RESISTANCE_FIRE: (40, -100, 100),
        RESISTANCE_ELECTRICITY: (-50, -100, 100),
        RESISTANCE_GAZ_CONTACT: (100, -100, 100),
        RESISTANCE_GAZ_INHALED: (100, -100, 100),
        HIT_POINTS_PER_LEVEL: (0, 0, 0),
        PERK_RATE: (10, None, None),
    },
    RACE_ANIMAL: {
        SPECIAL_STRENGTH: (0, 1, 7),
        SPECIAL_PERCEPTION: (0, 4, 14),
        SPECIAL_ENDURANCE: (0, 1, 6),
        SPECIAL_CHARISMA: (0, 1, 5),
        SPECIAL_INTELLIGENCE: (0, 1, 3),
        SPECIAL_AGILITY: (0, 1, 15),
        SPECIAL_LUCK: (0, 1, 10),
        PERK_RATE: (10, None, None),
    }
}

# Radiation effects
RADS_EFFECTS = {
    (0, 199): {},
    (200, 399): {
        SPECIAL_STRENGTH: (-1, None, None),
    },
    (400, 599): {
        STATS_HEALING_RATE: (-3, 0, None),
        SPECIAL_STRENGTH: (-1, 1, None),
        SPECIAL_AGILITY: (-1, 1, None),
    },
    (600, 799): {
        STATS_HEALING_RATE: (-5, 0, None),
        STATS_MAX_HEALTH: (-5, 0, None),
        SPECIAL_STRENGTH: (-2, 1, None),
        SPECIAL_ENDURANCE: (-1, 1, None),
        SPECIAL_AGILITY: (-2, 1, None),
    },
    (800, 999): {
        STATS_HEALING_RATE: (-10, 0, None),
        STATS_MAX_HEALTH: (-15, 0, None),
        SPECIAL_STRENGTH: (-4, 1, None),
        SPECIAL_PERCEPTION: (-3, 1, None),
        SPECIAL_ENDURANCE: (-3, 1, None),
        SPECIAL_CHARISMA: (-3, 1, None),
        SPECIAL_INTELLIGENCE: (-1, 1, None),
        SPECIAL_AGILITY: (-5, 1, None),
    },
    (1000, None): {
        STATS_HEALING_RATE: (-10, None, None),
        STATS_MAX_HEALTH: (-20, None, None),
        SPECIAL_STRENGTH: (-6, 1, None),
        SPECIAL_PERCEPTION: (-5, 1, None),
        SPECIAL_ENDURANCE: (-5, 1, None),
        SPECIAL_CHARISMA: (-5, 1, None),
        SPECIAL_INTELLIGENCE: (-3, 1, None),
        SPECIAL_AGILITY: (-6, 1, None),
    },
}

# Dehydration effets
THIRST_EFFECTS = {
    (0, 199): {},
    (200, 399): {
        SPECIAL_ENDURANCE: (-1, 1, None),
    },
    (400, 599): {
        SPECIAL_PERCEPTION: (-1, 1, None),
        SPECIAL_ENDURANCE: (-2, 1, None),
    },
    (600, 799): {
        SPECIAL_PERCEPTION: (-2, 1, None),
        SPECIAL_ENDURANCE: (-2, 1, None),
        SPECIAL_INTELLIGENCE: (-1, 1, None),
    },
    (800, 999): {
        SPECIAL_PERCEPTION: (-2, 1, None),
        SPECIAL_ENDURANCE: (-3, 1, None),
        SPECIAL_INTELLIGENCE: (-1, 1, None),
        SPECIAL_AGILITY: (-2, 1, None),
    },
    (1000, None): {
        STATS_HEALTH: (-9999, None, None),
    },
}

# Hunger effects
HUNGER_EFFECTS = {
    (0, 199): {},
    (200, 399): {
        SPECIAL_STRENGTH: (-1, 1, None),
    },
    (400, 599): {
        SPECIAL_STRENGTH: (-2, 1, None),
        SPECIAL_CHARISMA: (-1, 1, None),
    },
    (600, 799): {
        SPECIAL_STRENGTH: (-3, 1, None),
        SPECIAL_PERCEPTION: (-1, 1, None),
        SPECIAL_CHARISMA: (-2, 1, None),
    },
    (800, 999): {
        SPECIAL_STRENGTH: (-3, 1, None),
        SPECIAL_PERCEPTION: (-2, 1, None),
        SPECIAL_CHARISMA: (-2, 1, None),
    },
    (1000, None): {
        STATS_HEALTH: (-9999, None, None),
    },
}

# Sleep deprivation effects
SLEEP_EFFECTS = {
    (0, 199): {},
    (200, 399): {
        SPECIAL_AGILITY: (-1, 1, None),
    },
    (400, 599): {
        SPECIAL_INTELLIGENCE: (-1, 1, None),
        SPECIAL_AGILITY: (-2, 1, None),
    },
    (600, 799): {
        SPECIAL_ENDURANCE: (-1, 1, None),
        SPECIAL_INTELLIGENCE: (-2, 1, None),
        SPECIAL_AGILITY: (-3, 1, None),
    },
    (800, 999): {
        SPECIAL_ENDURANCE: (-2, 1, None),
        SPECIAL_INTELLIGENCE: (-2, 1, None),
        SPECIAL_AGILITY: (-3, 1, None),
    },
    (1000, None): {
        STATS_HEALTH: (-9999, None, None),
    },
}

# Survival effects
SURVIVAL_EFFECTS = (
    (STATS_RADS, RADS_EFFECTS),
    (STATS_THIRST, THIRST_EFFECTS),
    (STATS_HUNGER, HUNGER_EFFECTS),
    (STATS_SLEEP, SLEEP_EFFECTS),
)

# Critical rolls
CRITICAL_FAIL_D10 = 10
CRITICAL_FAIL_D100 = 96

# Base value for experience points
BASE_XP = 1000

# Tag skill bonus
TAG_SKILL_BONUS = 20

# Healing rate multiplier when resting
HEALING_RATE_RESTING_MULT = 4.0

# Range malus when fighting
FIGHT_RANGE_MALUS = 3

# Action points cost
AP_COST_FIGHT = 5  # Fight unarmed
AP_COST_EQUIP = 4  # Equip item
AP_COST_USE = 3  # Use item
AP_COST_DROP = 2  # Drop item
AP_COST_TAKE = 2  # Take item
AP_COST_REPAIR = 5  # Repair item

# Experience gains
XP_GAIN_ROLL_FAIL = 3  # XP gain for roll failure
XP_GAIN_ROLL_SUCCESS = 2  # XP gain for roll success
XP_GAIN_ROLL = (XP_GAIN_ROLL_FAIL, XP_GAIN_ROLL_SUCCESS)
XP_GAIN_FIGHT_MISS = 3  # XP gain for fight failure (multiplier)
XP_GAIN_FIGHT_HIT = 2  # XP gain for fight success (multiplier)
XP_GAIN_FIGHT = (XP_GAIN_FIGHT_MISS, XP_GAIN_FIGHT_HIT)

# Turn time
TURN_TIME = 30

# Computed statistics from S.P.E.C.I.A.L.
COMPUTED_STATS = (
    ('hit_points_per_level', lambda s, c: 3 + (s.endurance // 2)),
    ('skill_points_per_level', lambda s, c: 5 + (2 * s.intelligence)),
    ('max_health', lambda s, c: (15 + (s.strength + (2 * s.endurance)) + ((c.level - 1) * s.hit_points_per_level))),
    ('max_action_points', lambda s, c: 5 + (s.agility // 2)),
    # Secondary statistics
    ('armor_class', lambda s, c: s.agility),
    ('carry_weight', lambda s, c: (15 + (15 * s.strength)) // 2),
    ('melee_damage', lambda s, c: max(1, s.strength - 5)),
    ('sequence', lambda s, c: 2 * s.perception),
    ('healing_rate', lambda s, c: (s.endurance // 3)),
    ('critical_chance', lambda s, c: s.luck),
    # Resistances
    ('radiation_resistance', lambda s, c: 2 * s.endurance),
    ('poison_resistance', lambda s, c: 5 * s.endurance),
    # Skills
    ('small_guns', lambda s, c: 5 + (4 * s.agility)),
    ('big_guns', lambda s, c: 2 * s.agility),
    ('energy_weapons', lambda s, c: 2 * s.agility),
    ('unarmed', lambda s, c: 30 + (2 * (s.strength + s.agility))),
    ('melee_weapons', lambda s, c: 20 + (2 * (s.strength + s.agility))),
    ('throwing', lambda s, c: 4 * s.agility),
    ('first_aid', lambda s, c: 2 * (s.perception + s.endurance)),
    ('doctor', lambda s, c: 5 + s.perception + s.intelligence),
    ('chems', lambda s, c: 10 + (2 * s.intelligence)),
    ('sneak', lambda s, c: 5 + (3 * s.agility)),
    ('lockpick', lambda s, c: 10 + s.perception + s.agility),
    ('steal', lambda s, c: 3 * s.agility),
    ('traps', lambda s, c: 10 + (2 * s.perception)),
    ('explosives', lambda s, c: 2 * s.perception),
    ('science', lambda s, c: 4 * s.intelligence),
    ('repair', lambda s, c: 3 * s.intelligence),
    ('speech', lambda s, c: 5 * s.charisma),
    ('barter', lambda s, c: 4 * s.charisma),
    ('survival', lambda s, c: 2 * (s.endurance + s.intelligence)),
    ('knowledge', lambda s, c: 5 * s.intelligence),
)

# Computed needs per hour
COMPUTED_NEEDS = {
    ('thirst', lambda s, c: max(1, (20 - s.endurance) * 2)),
    ('hunger', lambda s, c: max(1, (16 - s.endurance) * 2)),
    ('sleep', lambda s, c: max(1, (14 - s.endurance) * 2)),
}
