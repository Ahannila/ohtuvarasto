import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_liian_vahan_ei_ota(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-1)

        self.assertEqual(self.varasto.saldo, 8)

    def test_virheellinen_saldo_nollataan(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_print_self(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(self.varasto.__str__(), "saldo = 8, vielä tilaa 2")

    def test_maara_isompi_kuin_saldo(self):
        self.varasto.lisaa_varastoon(3)

        self.varasto.ota_varastosta(4)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisataan_enemman_mita_mahtuu(self):
        self.varasto.lisaa_varastoon(9)

        self.varasto.lisaa_varastoon(3)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_initti_liikatilavuus(self):
        self.varasto1 = Varasto(0,-2)

        self.assertEqual(self.varasto1.saldo, 0.0)

    def test_initti_tayteen_ja_ylimaara_hukkaan(self):
        self.varasto1 = Varasto(5,6)

        self.assertEqual(self.varasto1.saldo, 5)
