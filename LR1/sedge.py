import my_enums
from plant import Plant
import my_enums
from typing import List, NoReturn
import random


class Sedge(Plant):

    _life_median = my_enums.LifeMedian.SEDGE_LM.value
    _max_hp = my_enums.MaxHP.SEDGE_MHP.value
    _start_hp = my_enums.StartHP.SEDGE_START_HP.value
    _hp_reduction = my_enums.PlantHPReduction.SEDGE_HPR.value
    _offspring_dispersion = my_enums.PlantOffspringDispersion.SEDGE_OD.value
    _offspring_nutritional_value = my_enums.NutritionalValue.SEDGE_OFFSPRING_NV.value
    _start_shrub_nutritional_value = my_enums.NutritionalValue.START_SEDGE_SNV.value
    _shrub_reduction = my_enums.PlantShrubReduction.SEDGE_SR.value
    _reproduction_age_interval = my_enums.ReproductionAgeInterval.SEDGE_RAI.value
    _id_counter = 0

    @staticmethod
    def set_id_counter(new_id_counter) -> NoReturn:
        if new_id_counter < Sedge._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Sedge._id_counter})")
        Sedge._id_counter = new_id_counter

    @staticmethod
    def get_id_counter() -> int:
        return Sedge._id_counter

    def __init__(self, unpack_dict_flag=False, info_d=None):
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Sedge._id_counter += 1
            return

        self._age = 0
        self._hp = self._start_hp
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(my_enums.PersonalPowerCoefficientParameters.SEDGE_PPCP)
        self._id = my_enums.IdPrefix.SEDGE_PREF.value + str(self._id_counter)
        Sedge._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        start_power = my_enums.StartPower.SEDGE_SP.value
        k_func_coefficient = my_enums.PowerFunctionCoefficient.SEDGE_PFC.value
        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        else:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))

    def produce_eatable_offspring(self) -> NoReturn:
        min_amount, max_amount = my_enums.PlantEatableOffspringPossibleAmount.SEDGE_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = my_enums.ChanceToProduceKids.SEDGE_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce == 1:
            min_amount, max_amount = my_enums.PossibleKidsAmount.SEDGE_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Sedge() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value) -> int:
        if nutritional_value > self._nutritional_value:
            self._nutritional_value = 0
            self.get_hearted(int(0.5 * (nutritional_value - self._nutritional_value)))
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(int(nutritional_value * my_enums.UnprotectedDamageMultiplier.SEDGE_UDM.value))
        return nutritional_value

    def stats(self) -> str:
        return """ Kingdom: Plant
 Kind: Sedge
    """ + super().stats()