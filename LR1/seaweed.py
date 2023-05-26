import my_enums
from plant import Plant
import my_enums
from typing import List, NoReturn
import random


class Seaweed(Plant):

    _life_median = my_enums.LifeMedian.SEAWEED_LM.value
    _max_hp = my_enums.MaxHP.SEAWEED_MHP.value
    _offspring_dispersion = my_enums.PlantOffspringDispersion.SEAWEED_OD.value
    _offspring_nutritional_value = my_enums.NutritionalValue.SEAWEED_OFFSPRING_NV.value
    _hp_reduction = my_enums.PlantHPReduction.SEAWEED_HPR.value
    _shrub_reduction = my_enums.PlantShrubReduction.SEAWEED_SR.value
    _start_shrub_nutritional_value = my_enums.NutritionalValue.START_SEAWEED_SNV.value
    _reproduction_age_interval = my_enums.ReproductionAgeInterval.SEAWEED_RAI.value
    _id_counter = 0

    @staticmethod
    def set_id_counter(new_id_counter) -> NoReturn:
        if new_id_counter < Seaweed._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >="
                             f" than old id counter({Seaweed._id_counter})")
        Seaweed._id_counter = new_id_counter

    @staticmethod
    def get_id_counter() -> int:
        return Seaweed._id_counter

    def __init__(self, unpack_dict_flag=False, info_d=None):
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Seaweed._id_counter += 1
            return

        self._age = 0
        self._hp = my_enums.StartHP.SEAWEED_START_HP.value
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(my_enums.PersonalPowerCoefficientParameters.SEAWEED_PPCP)
        self._id = my_enums.IdPrefix.SEAWEED_PREF.value + str(self._id_counter)
        Seaweed._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        if self.age <= self._life_median:
            return my_enums.StartPower.SEAWEED_SP.value
        else:
            return 3/self.age

    def produce_eatable_offspring(self) -> NoReturn:
        min_amount, max_amount = my_enums.PlantEatableOffspringPossibleAmount.SEAWEED_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = my_enums.ChanceToProduceKids.SEAWEED_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce != 0:
            min_amount, max_amount = my_enums.PossibleKidsAmount.SEAWEED_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Seaweed() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value) -> int:
        if nutritional_value > self._nutritional_value:
            self.die()
            return self._nutritional_value
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(nutritional_value * my_enums.UnprotectedDamageMultiplier.SEAWEED_UDM.value)
            return nutritional_value

    def stats(self) -> str:
        return """ Kingdom: Plant
 Kind: Seaweed
    """ + super().stats()