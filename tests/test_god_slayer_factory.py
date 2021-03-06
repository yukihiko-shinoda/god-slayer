"""Tests for god_slayer_factory."""
from godslayer.god_slayer_factory import GodSlayerFactory
from tests.testlibraries.god_slayer_checker import GodSlayerChecker
from tests.testlibraries.instance_resource import InstanceResource


class TestClassGodSlayerFactory:
    """Tests for God Slayer Factory."""

    @staticmethod
    def test_record_reader(path_gold_point_card_plus):
        """should"""
        expected = [
            ["2018/7/3", "東京電力  電気料金等", "ご本人", "1回払い", "", "18/8", "11402", "11402", "", "", "", "", ""],
            ["2018/7/4", "ＡＭＡＺＯＮ．ＣＯ．ＪＰ", "ご本人", "1回払い", "", "18/8", "3456", "3456", "", "", "", "", ""],
        ]
        god_slayer = GodSlayerFactory(encoding="shift_jis_2004").create(path_gold_point_card_plus)
        GodSlayerChecker.assert_god_slayer(god_slayer, 0, expected)

    @staticmethod
    def test_header_skipper(path_gold_point_card_plus_201912):
        """should"""
        expected = [
            ["2020/7/3", "東京電力  電気料金等", "11402", "1", "1", "11402", ""],
            ["2020/7/3", "AMAZON WEB SERVICES (AWS.AMAZON.CO)", "66", "1", "1", "66", "0.60　USD　110.712　07 03"],
            ["2020/7/4", "ＡＭＡＺＯＮ．ＣＯ．ＪＰ", "3456", "1", "1", "3456", ""],
        ]
        god_slayer = GodSlayerFactory(
            header=InstanceResource.REGEX_HEADER_GOLD_POINT_CARD_PLUS,
            footer=InstanceResource.REGEX_FOOTER_GOLD_POINT_CARD_PLUS,
            encoding="shift_jis_2004",
        ).create(path_gold_point_card_plus_201912)
        GodSlayerChecker.assert_god_slayer(god_slayer, 0, expected)

    @staticmethod
    def test_header_skipper_multiple_line_header(path_sf_card_viewer):
        """should"""
        expected = [["2019/01/27", "", "", "", "", "", "", "195", "2896", "ﾊﾞｽ/路面等"]]
        god_slayer = GodSlayerFactory(header=InstanceResource.HEADER_SF_CARD_VIEWER, encoding="shift_jis_2004").create(
            path_sf_card_viewer
        )
        GodSlayerChecker.assert_god_slayer(god_slayer, 1, expected)

    @staticmethod
    def test_partition_skip_record_reader(path_view_card):
        """should"""
        expected = [
            ["2020/03/21", "板橋駅　オートチャージ", "3,000", "", "3,000", "１回払", "", "3,000", "", "   ", ""],
            ["2020/03/31", "カード年会費", "524", "", "524", "１回払", "", "524", "", "   ", ""],
        ]
        god_slayer = GodSlayerFactory(
            header=InstanceResource.HEADER_VIEW_CARD,
            partition=[r"^\*{4}-\*{4}-\*{4}-[0-9]{4}\s.*$"],
            encoding="shift_jis_2004",
        ).create(path_view_card)
        GodSlayerChecker.assert_god_slayer(god_slayer, 6, expected)

    @staticmethod
    def test_partition_skip_record_before_footer_reader(path_itabashiku_population):
        """should"""
        expected = [
            ["0", "4062", "2069", "1993"],
            ["1", "4279", "2171", "2108"],
            ["2", "4285", "2152", "2133"],
            ["3", "4434", "2268", "2166"],
            ["4", "4243", "2207", "2036"],
            ["5", "4369", "2283", "2086"],
            ["6", "4345", "2213", "2132"],
            ["7", "4117", "2163", "1954"],
            ["8", "4155", "2146", "2009"],
            ["9", "4031", "2151", "1880"],
            ["10", "3933", "1988", "1945"],
            ["11", "4137", "2161", "1976"],
            ["12", "3842", "2018", "1824"],
            ["13", "3898", "1925", "1973"],
            ["14", "3820", "1914", "1906"],
            ["15", "3869", "1986", "1883"],
            ["16", "3902", "1996", "1906"],
            ["17", "4139", "2133", "2006"],
            ["18", "4474", "2242", "2232"],
            ["19", "5382", "2632", "2750"],
            ["20", "5674", "2854", "2820"],
            ["21", "6331", "3090", "3241"],
            ["22", "7218", "3385", "3833"],
            ["23", "8700", "4042", "4658"],
            ["24", "8773", "4132", "4641"],
            ["25", "9247", "4411", "4836"],
            ["26", "8757", "4205", "4552"],
            ["27", "9015", "4302", "4713"],
            ["28", "8814", "4289", "4525"],
            ["29", "8446", "4125", "4321"],
            ["30", "8173", "4050", "4123"],
            ["31", "8334", "4157", "4177"],
            ["32", "8145", "4179", "3966"],
            ["33", "7986", "3956", "4030"],
            ["34", "8126", "4170", "3956"],
            ["35", "8342", "4293", "4049"],
            ["36", "8472", "4320", "4152"],
            ["37", "8375", "4288", "4087"],
            ["38", "8213", "4253", "3960"],
            ["39", "8392", "4343", "4049"],
            ["40", "8402", "4344", "4058"],
            ["41", "8555", "4461", "4094"],
            ["42", "8545", "4400", "4145"],
            ["43", "8839", "4605", "4234"],
            ["44", "8908", "4620", "4288"],
            ["45", "9319", "4751", "4568"],
            ["46", "9611", "4927", "4684"],
            ["47", "9448", "4842", "4606"],
            ["48", "9291", "4857", "4434"],
            ["49", "8962", "4640", "4322"],
            ["50", "8714", "4400", "4314"],
            ["51", "8620", "4485", "4135"],
            ["52", "8455", "4466", "3989"],
            ["53", "6323", "3295", "3028"],
            ["54", "7974", "4093", "3881"],
            ["55", "7523", "3942", "3581"],
            ["56", "6935", "3606", "3329"],
            ["57", "6750", "3433", "3317"],
            ["58", "6449", "3358", "3091"],
            ["59", "6197", "3254", "2943"],
            ["60", "5945", "3065", "2880"],
            ["61", "6113", "3162", "2951"],
            ["62", "5380", "2755", "2625"],
            ["63", "5527", "2771", "2756"],
            ["64", "5626", "2825", "2801"],
            ["65", "5717", "2885", "2832"],
            ["66", "5913", "2994", "2919"],
            ["67", "6100", "3099", "3001"],
            ["68", "6266", "3121", "3145"],
            ["69", "6845", "3443", "3402"],
            ["70", "7587", "3805", "3782"],
            ["71", "7696", "3725", "3971"],
            ["72", "7861", "3761", "4100"],
            ["73", "5344", "2533", "2811"],
            ["74", "4419", "1971", "2448"],
            ["75", "5497", "2546", "2951"],
            ["76", "5814", "2611", "3203"],
            ["77", "5589", "2446", "3143"],
            ["78", "5471", "2371", "3100"],
            ["79", "4757", "2059", "2698"],
            ["80", "4120", "1673", "2447"],
            ["81", "3882", "1586", "2296"],
            ["82", "4202", "1584", "2618"],
            ["83", "3957", "1471", "2486"],
            ["84", "3882", "1390", "2492"],
            ["85", "3163", "1137", "2026"],
            ["86", "3031", "1035", "1996"],
            ["87", "2681", "916", "1765"],
            ["88", "2220", "680", "1540"],
            ["89", "1980", "603", "1377"],
            ["90", "1653", "508", "1145"],
            ["91", "1442", "374", "1068"],
            ["92", "1141", "291", "850"],
            ["93", "919", "240", "679"],
            ["94", "782", "179", "603"],
            ["95", "521", "119", "402"],
            ["96", "375", "59", "316"],
            ["97", "308", "51", "257"],
            ["98", "187", "32", "155"],
            ["99", "131", "23", "108"],
            ["100", "91", "7", "84"],
            ["101", "57", "5", "52"],
            ["102", "43", "7", "36"],
        ]
        god_slayer = GodSlayerFactory(
            header=InstanceResource.HEADER_ITABASHIKU_POPULATION,
            partition=[r"^(総数)|(\d*〜\d*歳?)$", r"^\d*$", r"^\d*$", r"^\d*$"],
            footer=InstanceResource.FOOTER_ITABASHIKU_POPULATION,
            encoding="shift_jis_2004",
        ).create(path_itabashiku_population)
        GodSlayerChecker.assert_god_slayer_partition(god_slayer, expected)
