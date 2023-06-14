import unittest
from utils.Plastic_Card import PlasticCard
from utils.Bank_Account import BankAccount
from utils.Bank import Bank
import regex as re


class AtmTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bank: Bank = Bank()
        self.card_account: BankAccount = BankAccount("abba", 1000.33)
        self.plastic_card: PlasticCard = PlasticCard(card_id="4000500060007000", bank_account=self.card_account,
                                                     expiration_date="09/25", is_blocked=False)

    def test_balance(self):
        self.assertEqual(self.card_account.balance, 1000.33)

    def test_card_account_id(self):
        self.assertEqual(self.card_account.account_id, "abba")

    def test_balance_add(self):
        self.card_account.add_balance(100.22)
        self.assertEqual(self.card_account.balance, 1100.55)

    def test_balance_sub(self):
        self.card_account.subtract_money(100.22)
        self.assertEqual(self.card_account.balance, 900.11)

    def test_card_id(self):
        self.assertEqual(self.plastic_card.card_id, "4000500060007000")

    def test_pin(self):
        self.assertEqual(self.bank.TryPin(self.plastic_card.card_id, "5678"), True)

    def test_incorrect_pin(self):
        self.assertEqual(self.bank.TryPin(self.plastic_card.card_id, "5990"), False)

    def test_block(self):
        self.plastic_card.is_blocked = True
        self.assertEqual(self.plastic_card.is_blocked, True)
        self.plastic_card.is_blocked = False
        self.assertEqual(self.plastic_card.is_blocked, False)

    def test_phone_regular_exp(self):
        self.assertEqual(re.fullmatch(r"\+375(29|33|25|44|17|29)\d{7}", "+3754545612344"), None)


if __name__ == '__main__':
    unittest.main()