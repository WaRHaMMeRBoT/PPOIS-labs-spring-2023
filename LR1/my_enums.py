import enum


CREATOR = "Selitsky"

BASE_ECOSYSTEM_PARAMETERS = {
    "ocean_vertical_length": 7,
    "ocean_horizontal_length": 7,
    "deadly_worm_sleep_interval": 5,
    "deadly_worm_sleep_counter": 5,
    "seaweed_amount": 20,
    "sedge_amount": 10,
    "urut_amount": 10,
    "carp_amount": 12,
    "perch_amount": 6,
    "beluga_amount": 12,
    "shark_amount": 6
}


class LifeMedian(enum.Enum):

    SEAWEED_LM = 3
    SEDGE_LM = 70
    URUT_LM = 200

    CARP_LM = 15
    PERCH_LM = 14
    BELUGA_LM = 10
    SHARK_LM = 25


class PlantOffspringDispersion(enum.Enum):

    SEAWEED_OD = 1
    SEDGE_OD = 1
    URUT_OD = 2


class PlantEatableOffspringPossibleAmount(enum.Enum):

    SEAWEED_EOPA = (10, 15)
    SEDGE_EOPA = (10, 15)
    URUT_EOPA = (25, 35)


class PlantHPReduction(enum.Enum):

    SEAWEED_HPR = 5
    SEDGE_HPR = 13
    URUT_HPR = 50


class PlantShrubReduction(enum.Enum):

    SEAWEED_SR = 5
    SEDGE_SR = 25
    URUT_SR = 50


class StartPower(enum.Enum):

    SEAWEED_SP = 1.0
    SEDGE_SP = 5.0
    URUT_SP = 10.0

    M_CARP_SP = 10.0
    FEM_CARP_SP = 8.0

    M_PERCH_SP = 15
    FEM_PERCH_SP = 10

    M_BELUGA_SP = 12
    FEM_BELUGA_SP = 10

    M_SHARK_SP = 15
    FEM_SHARK_SP = 12


class PowerFunctionCoefficient(enum.Enum):

    SEAWEED_PFC = 0.0
    SEDGE_PFC = (2. / 3.)
    URUT_PFC = 1.0

    M_CARP_PFC = 6.0
    FEM_CARP_PFC = (24. / 5.)

    M_PERCH_PFC = 12.5
    FEM_PERCH_PFC = (42.5 / 4)

    M_BELUGA_PFC = (40.5 / 3.)
    FEM_BELUGA_PFC = (35. / 3.)

    M_SHARK_PFC = (55. / 8)
    FEM_SHARK_PFC = (55.5 / 8)


class PersonalPowerCoefficientParameters(enum.Enum):

    SEAWEED_PPCP = {"min_numerator": 1, "max_numerator": 1, "denominator": 1}
    SEDGE_PPCP = {"min_numerator": 20, "max_numerator": 30, "denominator": 25}
    URUT_PPCP = {"min_numerator": 40, "max_numerator": 55, "denominator": 50}

    FEM_CARP_PPCP = {"min_numerator": 25, "max_numerator": 35, "denominator": 30}
    M_CARP_PPCP = {"min_numerator": 35, "max_numerator": 45, "denominator": 40}

    FEM_PERCH_PPCP = {"min_numerator": 40, "max_numerator": 65, "denominator": 52.5}
    M_PERCH_PPCP = {"min_numerator": 55, "max_numerator": 75, "denominator": 65}

    FEM_BELUGA_PPCP = {"min_numerator": 35, "max_numerator": 55, "denominator": 45}
    M_BELUGA_PPCP = {"min_numerator": 40, "max_numerator": 65, "denominator": 52.5}

    FEM_SHARK_PPCP = {"min_numerator": 55, "max_numerator": 80, "denominator": 67.5}
    M_SHARK_PPCP = {"min_numerator": 60, "max_numerator": 80, "denominator": 70}


class NutritionalValue(enum.Enum):

    START_SEAWEED_SNV = 30
    START_SEDGE_SNV = 50
    START_URUT_SNV = 100

    SEAWEED_OFFSPRING_NV = 5
    SEDGE_OFFSPRING_NV = 10
    URUT_OFFSPRING_NV = 5

    CARP_NV = 250
    PERCH_NV = 600
    BELUGA_NV = 200
    SHARK_NV = 600


class Damage(enum.Enum):

    CARP_D = 100
    PERCH_D = 300
    BELUGA_D = 200
    SHARK_D = 350


class UnprotectedDamageMultiplier(enum.Enum):

    SEAWEED_UDM = 0.1
    SEDGE_UDM = 0.05
    URUT_UDM = 0.075

    EVERY_ANIMAL_UDM = 0.1


class StartHP(enum.Enum):

    SEAWEED_START_HP = 5
    SEDGE_START_HP = 10
    URUT_START_HP = 10


class MaxHP(enum.Enum):

    SEAWEED_MHP = 10
    SEDGE_MHP = 400
    URUT_MHP = 1000

    CARP_MHP = 200
    PERCH_MHP = 350
    BELUGA_MHP = 200
    SHARK_MHP = 300


class RequiredNutritionalValue(enum.Enum):

    CARP_RNV = 100
    PERCH_RNV = 125
    SHARK_RNV = 150
    BELUGA_RNV = 100


class HungerPerCycle(enum.Enum):

    CARP_HPC = 75
    PERCH_HPC = 100
    BELUGA_HPC = 100
    SHARK_HPC = 150


class Genders(enum.Enum):

    FEMALE = "female"
    MALE = "male"


class ReproductionAgeInterval(enum.Enum):

    SEAWEED_RAI = (1, 4)
    SEDGE_RAI = (30, 70)
    URUT_RAI = (50, 200)

    CARP_RAI = (5, 11)
    PERCH_RAI = (4, 12)
    BELUGA_RAI = (3, 9)
    SHARK_RAI = (8, 20)


class IdPrefix(enum.Enum):

    SEAWEED_PREF = "seaweed"
    SEDGE_PREF = "sedge"
    URUT_PREF = "urut"

    CARP_PREF = "carp"
    PERCH_PREF = "perch"
    BELUGA_PREF = "beluga"
    SHARK_PREF = "shark"


class ChanceToProduceKids(enum.Enum):

    SEAWEED_CTPK = (0, 2)
    SEDGE_CTPK = (1, 10)
    URUT_CTPK = (1, 40)

    CARP_CTPK = (1, 3)
    PERCH_CTPK = (1, 2)
    BELUGA_CTPK = (1, 3)
    SHARK_CTPK = (1, 2)


class PossibleKidsAmount(enum.Enum):

    SEAWEED_PKA = (2, 4)
    SEDGE_PKA = (2, 4)
    URUT_PKA = (1, 3)

    CARP_PKA = (3, 5)
    PERCH_PKA = (2, 3)
    BELUGA_PKA = (3, 5)
    SHARK_PKA = (2, 3)


class SterilePeriods(enum.Enum):

    CARP_SP = 2
    PERCH_SP = 3
    BELUGA_SP = 2
    SHARK_SP = 4