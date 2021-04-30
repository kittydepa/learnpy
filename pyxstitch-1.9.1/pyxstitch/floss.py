#!/usr/bin/python3
"""
DMC floss mapping.

Sourced from csv:
    https://github.com/adrianj/CrossStitchCreator
"""
import math
import pyxstitch.hex as hu


class FlossException(Exception):
    """Floss exception."""


class FlossType(object):
    """Floss type."""

    def __init__(self, dmc):
        """Init the instance."""
        self.floss_number = dmc[0]
        self.name = dmc[1]
        self.rgb = hu.to_rgb_string(dmc[2])


class Floss(object):
    """Floss definitions."""

    def __init__(self):
        """Init the instance."""
        self._colors = {}
        self._cache = {}
        self._load()
        self._map = {}

    def _key_rgb(self, red, green, blue):
        """Create a cache key."""
        return "{}.{}.{}".format(red, green, blue)

    def _create_floss(self, dmc):
        """Create floss, handle any mappings."""
        floss_type = FlossType(dmc)
        if floss_type.rgb in self._map:
            floss_type = FlossType(self._map[floss_type.rgb])
        return floss_type

    def lookup(self, rgb):
        """Lookup a code."""
        rgb_str = self._key_rgb(rgb[0], rgb[1], rgb[2])
        if rgb_str in self._cache:
            return self._create_floss(self._cache[rgb_str])
        # try harder...
        close = None
        closest = -1
        for tries in self._colors.keys():
            t = self._colors[tries][2]
            check = hu.rgb_close(rgb[0], rgb[1], rgb[2], t[0], t[1], t[2])
            if closest == -1 or check < closest:
                closest = check
                close = self._colors[tries]
        self._cache[rgb_str] = close
        return self._create_floss(close)

    def map(self, from_color, to_color):
        """Map one floss rgb to another."""
        if to_color in self._colors or to_color is None:
            if to_color is None:
                self._colors.pop(from_color, None)
            else:
                self._map[from_color] = self._colors[to_color]
            self._cache = {}
            return True
        raise FlossException("Unknown color(s): {} -> {}".format(from_color,
                                                                 to_color))

    def _add(self, number, desc, red, green, blue, row):
        """Add a color."""
        rgb = (red, green, blue)
        self._colors[hu.to_rgb_string(rgb)] = (number, desc, rgb)

    def _load(self):
        """Load all colors."""
        self._add('150', 'Dusty Rose Ult Vy Dk', 171, 2, 73, 'row 03-06')
        self._add('151', 'Dusty Rose Vry Lt', 240, 206, 212, 'row 03-01')
        self._add('152', 'Shell Pink Med Light', 226, 160, 153, 'row 04-03')
        self._add('153', 'Violet Very Light', 230, 204, 217, 'row 05-07')
        self._add('154', 'Grape Very Dark', 87, 36, 51, 'row 04-22')
        self._add('155', 'Blue Violet Med Dark', 152, 145, 182, 'row 05-16')
        self._add('156', 'Blue Violet Med Lt', 163, 174, 209, 'row 05-14')
        self._add('157', 'Cornflower Blue Vy Lt', 187, 195, 217, 'row 05-19')
        self._add('158', 'Cornflower Blu M V D', 76, 82, 110, 'row 05-24')
        self._add('159', 'Blue Gray Light', 199, 202, 215, 'row 07-01')
        self._add('160', 'Blue Gray Medium', 153, 159, 183, 'row 07-02')
        self._add('161', 'Blue Gray', 120, 128, 164, 'row 07-03')
        self._add('162', 'Blue Ultra Very Light', 219, 236, 245, 'row 06-11')
        self._add('163', 'Celadon Green Md', 77, 131, 97, 'row 09-19')
        self._add('164', 'Forest Green Lt', 200, 216, 184, 'row 10-15')
        self._add('165', 'Moss Green Vy Lt', 239, 244, 164, 'row 12-04')
        self._add('166', 'Moss Green Md Lt', 192, 200, 64, 'row 12-06')
        self._add('167', 'Yellow Beige V Dk', 167, 124, 73, 'row 13-08')
        self._add('168', 'Pewter Very Light', 209, 209, 209, 'row 19-11')
        self._add('169', 'Pewter Light', 132, 132, 132, 'row 19-12')
        self._add('208', 'Lavender Very Dark', 131, 91, 139, 'row 05-04')
        self._add('209', 'Lavender Dark', 163, 123, 167, 'row 05-03')
        self._add('210', 'Lavender Medium', 195, 159, 195, 'row 05-02')
        self._add('211', 'Lavender Light', 227, 203, 227, 'row 05-01')
        self._add('221', 'Shell Pink Vy Dk', 136, 62, 67, 'row 04-07')
        self._add('223', 'Shell Pink Light', 204, 132, 124, 'row 04-04')
        self._add('224', 'Shell Pink Very Light', 235, 183, 175, 'row 04-02')
        self._add('225', 'Shell Pink Ult Vy Lt', 255, 223, 213, 'row 04-01')
        self._add('300', 'Mahogany Vy Dk', 111, 47, 0, 'row 15-18')
        self._add('301', 'Mahogany Med', 179, 95, 43, 'row 15-16')
        self._add('3011', 'Khaki Green Dk', 137, 138, 88, 'row 12-16')
        self._add('3012', 'Khaki Green Md', 166, 167, 93, 'row 12-15')
        self._add('3013', 'Khaki Green Lt', 185, 185, 130, 'row 12-14')
        self._add('3021', 'Brown Gray Vy Dk', 79, 75, 65, 'row 18-10')
        self._add('3022', 'Brown Gray Med', 142, 144, 120, 'row 18-13')
        self._add('3023', 'Brown Gray Light', 177, 170, 151, 'row 18-12')
        self._add('3024', 'Brown Gray Vy Lt', 235, 234, 231, 'row 18-11')
        self._add('3031', 'Mocha Brown Vy Dk', 75, 60, 42, 'row 17-23')
        self._add('3032', 'Mocha Brown Med', 179, 159, 139, 'row 18-17')
        self._add('3033', 'Mocha Brown Vy Lt', 227, 216, 204, 'row 18-15')
        self._add('304', 'Red Medium', 183, 31, 51, 'row 01-19')
        self._add('3041', 'Antique Violet Medium', 149, 111, 124, 'row 04-17')
        self._add('3042', 'Antique Violet Light', 183, 157, 167, 'row 04-16')
        self._add('3045', 'Yellow Beige Dk', 188, 150, 106, 'row 13-07')
        self._add('3046', 'Yellow Beige Md', 216, 188, 154, 'row 13-06')
        self._add('3047', 'Yellow Beige Lt', 231, 214, 193, 'row 13-05')
        self._add('3051', 'Green Gray Dk', 95, 102, 72, 'row 11-22')
        self._add('3052', 'Green Gray Md', 136, 146, 104, 'row 11-21')
        self._add('3053', 'Green Gray', 156, 164, 130, 'row 11-20')
        self._add('3064', 'Desert Sand', 196, 142, 112, 'row 16-21')
        self._add('307', 'Lemon', 253, 237, 84, 'row 14-02')
        self._add('3072', 'Beaver Gray Vy Lt', 230, 232, 232, 'row 19-01')
        self._add('3078', 'Golden Yellow Vy Lt', 253, 249, 205, 'row 14-05')
        self._add('309', 'Rose Dark', 86, 74, 74, 'row 02-08')
        self._add('310', 'Black', 0, 0, 0, 'row 19-16')
        self._add('311', 'Wedgewood Ult VyDk', 28, 80, 102, 'row 08-08')
        self._add('312', 'Baby Blue Very Dark', 53, 102, 139, 'row 07-11')
        self._add('315', 'Antique Mauve Md Dk', 129, 73, 82, 'row 04-12')
        self._add('316', 'Antique Mauve Med', 183, 115, 127, 'row 04-10')
        self._add('317', 'Pewter Gray', 108, 108, 108, 'row 19-13')
        self._add('318', 'Steel Gray Lt', 171, 171, 171, 'row 19-09')
        self._add('319', 'Pistachio Grn Vy Dk', 32, 95, 46, 'row 10-13')
        self._add('320', 'Pistachio Green Med', 105, 136, 90, 'row 10-11')
        self._add('321', 'Red', 199, 43, 59, 'row 01-18')
        self._add('322', 'Baby Blue Dark', 90, 143, 184, 'row 07-10')
        self._add('326', 'Rose Very Dark', 179, 59, 75, 'row 02-22')
        self._add('327', 'Violet Dark', 99, 54, 102, 'row 05-06')
        self._add('3325', 'Baby Blue Light', 184, 210, 230, 'row 07-07')
        self._add('3326', 'Rose Light', 251, 173, 180, 'row 02-18')
        self._add('3328', 'Salmon Dark', 227, 109, 109, 'row 01-05')
        self._add('333', 'Blue Violet Very Dark', 92, 84, 120, 'row 05-18')
        self._add('334', 'Baby Blue Medium', 115, 159, 193, 'row 07-09')
        self._add('3340', 'Apricot Med', 255, 131, 111, 'row 14-24')
        self._add('3341', 'Apricot', 252, 171, 152, 'row 14-23')
        self._add('3345', 'Hunter Green Dk', 27, 89, 21, 'row 10-24')
        self._add('3346', 'Hunter Green', 64, 106, 58, 'row 10-23')
        self._add('3347', 'Yellow Green Med', 113, 147, 92, 'row 10-22')
        self._add('3348', 'Yellow Green Lt', 204, 217, 177, 'row 10-21')
        self._add('335', 'Rose', 238, 84, 110, 'row 02-21')
        self._add('3350', 'Dusty Rose Ultra Dark', 188, 67, 101, 'row 03-05')
        self._add('3354', 'Dusty Rose Light', 228, 166, 172, 'row 03-02')
        self._add('336', 'Navy Blue', 37, 59, 115, 'row 07-13')
        self._add('3362', 'Pine Green Dk', 94, 107, 71, 'row 12-03')
        self._add('3363', 'Pine Green Md', 114, 130, 86, 'row 12-02')
        self._add('3364', 'Pine Green', 131, 151, 95, 'row 12-01')
        self._add('3371', 'Black Brown', 30, 17, 8, 'row 17-18')
        self._add('340', 'Blue Violet Medium', 173, 167, 199, 'row 05-15')
        self._add('341', 'Blue Violet Light', 183, 191, 221, 'row 05-13')
        self._add('347', 'Salmon Very Dark', 191, 45, 45, 'row 01-06')
        self._add('349', 'Coral Dark', 210, 16, 53, 'row 01-11')
        self._add('350', 'Coral Medium', 224, 72, 72, 'row 01-10')
        self._add('351', 'Coral', 233, 106, 103, 'row 01-09')
        self._add('352', 'Coral Light', 253, 156, 151, 'row 01-08')
        self._add('353', 'Peach', 254, 215, 204, 'row 01-07')
        self._add('355', 'Terra Cotta Dark', 152, 68, 54, 'row 16-13')
        self._add('356', 'Terra Cotta Med', 197, 106, 91, 'row 16-11')
        self._add('3607', 'Plum Light', 197, 73, 137, 'row 03-23')
        self._add('3608', 'Plum Very Light', 234, 156, 196, 'row 03-22')
        self._add('3609', 'Plum Ultra Light', 244, 174, 213, 'row 03-21')
        self._add('367', 'Pistachio Green Dk', 97, 122, 82, 'row 10-12')
        self._add('368', 'Pistachio Green Lt', 166, 194, 152, 'row 10-10')
        self._add('3685', 'Mauve Very Dark', 136, 21, 49, 'row 03-11')
        self._add('3687', 'Mauve', 201, 107, 112, 'row 03-09')
        self._add('3688', 'Mauve Medium', 231, 169, 172, 'row 03-08')
        self._add('3689', 'Mauve Light', 251, 191, 194, 'row 03-07')
        self._add('369', 'Pistachio Green Vy Lt', 215, 237, 204, 'row 10-09')
        self._add('370', 'Mustard Medium', 184, 157, 100, 'row 12-19')
        self._add('3705', 'Melon Dark', 255, 121, 146, 'row 01-15')
        self._add('3706', 'Melon Medium', 255, 173, 188, 'row 01-14')
        self._add('3708', 'Melon Light', 255, 203, 213, 'row 01-13')
        self._add('371', 'Mustard', 191, 166, 113, 'row 12-18')
        self._add('3712', 'Salmon Medium', 241, 135, 135, 'row 01-04')
        self._add('3713', 'Salmon Very Light', 255, 226, 226, 'row 01-01')
        self._add('3716', 'Dusty Rose Med Vy Lt', 255, 189, 189, 'row 02-10')
        self._add('372', 'Mustard Lt', 204, 183, 132, 'row 12-17')
        self._add('3721', 'Shell Pink Dark', 161, 75, 81, 'row 04-06')
        self._add('3722', 'Shell Pink Med', 188, 108, 100, 'row 04-05')
        self._add('3726', 'Antique Mauve Dark', 155, 91, 102, 'row 04-11')
        self._add('3727', 'Antique Mauve Light', 219, 169, 178, 'row 04-09')
        self._add('3731', 'Dusty Rose Very Dark', 218, 103, 131, 'row 03-04')
        self._add('3733', 'Dusty Rose', 232, 135, 155, 'row 03-03')
        self._add('3740', 'Antique Violet Dark', 120, 87, 98, 'row 04-18')
        self._add('3743', 'Antique Violet Vy Lt', 215, 203, 211, 'row 04-15')
        self._add('3746', 'Blue Violet Dark', 119, 107, 152, 'row 05-17')
        self._add('3747', 'Blue Violet Vy Lt', 211, 215, 237, 'row 05-12')
        self._add('3750', 'Antique Blue Very Dk', 56, 76, 94, 'row 07-21')
        self._add('3752', 'Antique Blue Very Lt', 199, 209, 219, 'row 07-17')
        self._add('3753', 'Antique Blue Ult Vy Lt', 219, 226, 233, 'row 07-16')
        self._add('3755', 'Baby Blue', 147, 180, 206, 'row 07-08')
        self._add('3756', 'Baby Blue Ult Vy Lt', 238, 252, 252, 'row 07-04')
        self._add('3760', 'Wedgewood Med', 62, 133, 162, 'row 08-05')
        self._add('3761', 'Sky Blue Light', 172, 216, 226, 'row 08-02')
        self._add('3765', 'Peacock Blue Vy Dk', 52, 127, 140, 'row 08-13')
        self._add('3766', 'Peacock Blue Light', 153, 207, 217, 'row 08-10')
        self._add('3768', 'Gray Green Dark', 101, 127, 127, 'row 08-23')
        self._add('3770', 'Tawny Vy Light', 255, 238, 227, 'row 15-12')
        self._add('3771', 'Terra Cotta Ult Vy Lt', 244, 187, 169, 'row 16-08')
        self._add('3772', 'Desert Sand Vy Dk', 160, 108, 80, 'row 16-24')
        self._add('3773', 'Desert Sand Dark', 182, 117, 82, 'row 16-23')
        self._add('3774', 'Desert Sand Vy Lt', 243, 225, 215, 'row 16-19')
        self._add('3776', 'Mahogany Light', 207, 121, 57, 'row 15-15')
        self._add('3777', 'Terra Cotta Vy Dk', 134, 48, 34, 'row 16-14')
        self._add('3778', 'Terra Cotta Light', 217, 137, 120, 'row 16-10')
        self._add('3779', 'Rosewood Ult Vy Lt', 248, 202, 200, 'row 16-15')
        self._add('3781', 'Mocha Brown Dk', 107, 87, 67, 'row 18-19')
        self._add('3782', 'Mocha Brown Lt', 210, 188, 166, 'row 18-16')
        self._add('3787', 'Brown Gray Dark', 98, 93, 80, 'row 18-09')
        self._add('3790', 'Beige Gray Ult Dk', 127, 106, 85, 'row 18-18')
        self._add('3799', 'Pewter Gray Vy Dk', 66, 66, 66, 'row 19-15')
        self._add('3801', 'Melon Very Dark', 231, 73, 103, 'row 01-16')
        self._add('3802', 'Antique Mauve Vy Dk', 113, 65, 73, 'row 04-13')
        self._add('3803', 'Mauve Dark', 171, 51, 87, 'row 03-10')
        self._add('3804', 'Cyclamen Pink Dark', 224, 40, 118, 'row 03-20')
        self._add('3805', 'Cyclamen Pink', 243, 71, 139, 'row 03-19')
        self._add('3806', 'Cyclamen Pink Light', 255, 140, 174, 'row 03-18')
        self._add('3807', 'Cornflower Blue', 96, 103, 140, 'row 05-22')
        self._add('3808', 'Turquoise Ult Vy Dk', 54, 105, 112, 'row 08-19')
        self._add('3809', 'Turquoise Vy Dark', 63, 124, 133, 'row 08-18')
        self._add('3810', 'Turquoise Dark', 72, 142, 154, 'row 08-17')
        self._add('3811', 'Turquoise Very Light', 188, 227, 230, 'row 08-14')
        self._add('3812', 'Sea Green Vy Dk', 47, 140, 132, 'row 09-04')
        self._add('3813', 'Blue Green Lt', 178, 212, 189, 'row 09-23')
        self._add('3814', 'Aquamarine', 80, 139, 125, 'row 09-10')
        self._add('3815', 'Celadon Green Dk', 71, 119, 89, 'row 09-20')
        self._add('3816', 'Celadon Green', 101, 165, 125, 'row 09-18')
        self._add('3817', 'Celadon Green Lt', 153, 195, 170, 'row 09-17')
        self._add('3818', 'Emerald Grn Ult V Dk', 17, 90, 59, 'row 10-08')
        self._add('3819', 'Moss Green Lt', 224, 232, 104, 'row 12-05')
        self._add('3820', 'Straw Dark', 223, 182, 95, 'row 13-26')
        self._add('3821', 'Straw', 243, 206, 117, 'row 13-25')
        self._add('3822', 'Straw Light', 246, 220, 152, 'row 13-24')
        self._add('3823', 'Yellow Ultra Pale', 255, 253, 227, 'row 15-19')
        self._add('3824', 'Apricot Light', 254, 205, 194, 'row 14-22')
        self._add('3825', 'Pumpkin Pale', 253, 189, 150, 'row 15-06')
        self._add('3826', 'Golden Brown', 173, 114, 57, 'row 16-04')
        self._add('3827', 'Golden Brown Pale', 247, 187, 119, 'row 16-01')
        self._add('3828', 'Hazelnut Brown', 183, 139, 97, 'row 13-12')
        self._add('3829', 'Old Gold Vy Dark', 169, 130, 4, 'row 13-23')
        self._add('3830', 'Terra Cotta', 185, 85, 68, 'row 16-12')
        self._add('3831', 'Raspberry Dark', 179, 47, 72, 'row 02-15')
        self._add('3832', 'Raspberry Medium', 219, 85, 110, 'row 02-14')
        self._add('3833', 'Raspberry Light', 234, 134, 153, 'row 02-13')
        self._add('3834', 'Grape Dark', 114, 55, 93, 'row 04-21')
        self._add('3835', 'Grape Medium', 148, 96, 131, 'row 04-20')
        self._add('3836', 'Grape Light', 186, 145, 170, 'row 04-19')
        self._add('3837', 'Lavender Ultra Dark', 108, 58, 110, 'row 05-05')
        self._add('3838', 'Lavender Blue Dark', 92, 114, 148, 'row 06-03')
        self._add('3839', 'Lavender Blue Med', 123, 142, 171, 'row 06-02')
        self._add('3840', 'Lavender Blue Light', 176, 192, 218, 'row 06-01')
        self._add('3841', 'Baby Blue Pale', 205, 223, 237, 'row 07-06')
        self._add('3842', 'Wedgewood Vry Dk', 50, 102, 124, 'row 08-07')
        self._add('3843', 'Electric Blue', 20, 170, 208, 'row 06-18')
        self._add('3844', 'Turquoise Bright Dark', 18, 174, 186, 'row 06-22')
        self._add('3845', 'Turquoise Bright Med', 4, 196, 202, 'row 06-21')
        self._add('3846', 'Turquoise Bright Light', 6, 227, 230, 'row 06-20')
        self._add('3847', 'Teal Green Dark', 52, 125, 117, 'row 08-27')
        self._add('3848', 'Teal Green Med', 85, 147, 146, 'row 08-26')
        self._add('3849', 'Teal Green Light', 82, 179, 164, 'row 08-25')
        self._add('3850', 'Green Bright Dk', 55, 132, 119, 'row 09-07')
        self._add('3851', 'Green Bright Lt', 73, 179, 161, 'row 09-05')
        self._add('3852', 'Straw Very Dark', 205, 157, 55, 'row 13-27')
        self._add('3853', 'Autumn Gold Dk', 242, 151, 70, 'row 15-22')
        self._add('3854', 'Autumn Gold Med', 242, 175, 104, 'row 15-21')
        self._add('3855', 'Autumn Gold Lt', 250, 211, 150, 'row 15-20')
        self._add('3856', 'Mahogany Ult Vy Lt', 255, 211, 181, 'row 15-02')
        self._add('3857', 'Rosewood Dark', 104, 37, 26, 'row 16-18')
        self._add('3858', 'Rosewood Med', 150, 74, 63, 'row 16-17')
        self._add('3859', 'Rosewood Light', 186, 139, 124, 'row 16-16')
        self._add('3860', 'Cocoa', 125, 93, 87, 'row 17-05')
        self._add('3861', 'Cocoa Light', 166, 136, 129, 'row 17-04')
        self._add('3862', 'Mocha Beige Dark', 138, 110, 78, 'row 17-22')
        self._add('3863', 'Mocha Beige Med', 164, 131, 92, 'row 17-21')
        self._add('3864', 'Mocha Beige Light', 203, 182, 156, 'row 17-20')
        self._add('3865', 'Winter White', 249, 247, 241, 'row 18-03')
        self._add('3866', 'Mocha Brn Ult Vy Lt', 250, 246, 240, 'row 18-20')
        self._add('400', 'Mahogany Dark', 143, 67, 15, 'row 15-17')
        self._add('402', 'Mahogany Vy Lt', 247, 167, 119, 'row 15-14')
        self._add('407', 'Desert Sand Med', 187, 129, 97, 'row 16-22')
        self._add('413', 'Pewter Gray Dark', 86, 86, 86, 'row 19-14')
        self._add('414', 'Steel Gray Dk', 140, 140, 140, 'row 19-10')
        self._add('415', 'Pearl Gray', 211, 211, 214, 'row 19-08')
        self._add('420', 'Hazelnut Brown Dk', 160, 112, 66, 'row 13-13')
        self._add('422', 'Hazelnut Brown Lt', 198, 159, 123, 'row 13-11')
        self._add('433', 'Brown Med', 122, 69, 31, 'row 17-14')
        self._add('434', 'Brown Light', 152, 94, 51, 'row 17-13')
        self._add('435', 'Brown Very Light', 184, 119, 72, 'row 17-12')
        self._add('436', 'Tan', 203, 144, 81, 'row 17-11')
        self._add('437', 'Tan Light', 228, 187, 142, 'row 17-10')
        self._add('444', 'Lemon Dark', 255, 214, 0, 'row 14-04')
        self._add('445', 'Lemon Light', 255, 251, 139, 'row 14-01')
        self._add('451', 'Shell Gray Dark', 145, 123, 115, 'row 17-03')
        self._add('452', 'Shell Gray Med', 192, 179, 174, 'row 17-02')
        self._add('453', 'Shell Gray Light', 215, 206, 203, 'row 17-01')
        self._add('469', 'Avocado Green', 114, 132, 60, 'row 11-14')
        self._add('470', 'Avocado Grn Lt', 148, 171, 79, 'row 11-13')
        self._add('471', 'Avocado Grn V Lt', 174, 191, 121, 'row 11-12')
        self._add('472', 'Avocado Grn U Lt', 216, 228, 152, 'row 11-11')
        self._add('498', 'Red Dark', 167, 19, 43, 'row 01-20')
        self._add('500', 'Blue Green Vy Dk', 4, 77, 51, 'row 09-27')
        self._add('501', 'Blue Green Dark', 57, 111, 82, 'row 09-26')
        self._add('502', 'Blue Green', 91, 144, 113, 'row 09-25')
        self._add('503', 'Blue Green Med', 123, 172, 148, 'row 09-24')
        self._add('504', 'Blue Green Vy Lt', 196, 222, 204, 'row 09-22')
        self._add('505', 'Jade Green', 51, 131, 98, 'row 09-16')
        self._add('517', 'Wedgewood Dark', 59, 118, 143, 'row 08-06')
        self._add('518', 'Wedgewood Light', 79, 147, 167, 'row 08-04')
        self._add('519', 'Sky Blue', 126, 177, 200, 'row 08-03')
        self._add('520', 'Fern Green Dark', 102, 109, 79, 'row 11-25')
        self._add('522', 'Fern Green', 150, 158, 126, 'row 11-24')
        self._add('523', 'Fern Green Lt', 171, 177, 151, 'row 11-19')
        self._add('524', 'Fern Green Vy Lt', 196, 205, 172, 'row 11-23')
        self._add('535', 'Ash Gray Vy Lt', 99, 100, 88, 'row 18-14')
        self._add('543', 'Beige Brown Ult Vy Lt', 242, 227, 206, 'row 17-18')
        self._add('550', 'Violet Very Dark', 92, 24, 78, 'row 05-11')
        self._add('552', 'Violet  Medium', 128, 58, 107, 'row 05-10')
        self._add('553', 'Violet', 163, 99, 139, 'row 05-09')
        self._add('554', 'Violet Light', 219, 179, 203, 'row 05-08')
        self._add('561', 'Celadon Green VD', 44, 106, 69, 'row 09-21')
        self._add('562', 'Jade Medium', 83, 151, 106, 'row 09-15')
        self._add('563', 'Jade Light', 143, 192, 152, 'row 09-14')
        self._add('564', 'Jade Very Light', 167, 205, 175, 'row 09-13')
        self._add('580', 'Moss Green Dk', 136, 141, 51, 'row 12-08')
        self._add('581', 'Moss Green', 167, 174, 56, 'row 12-07')
        self._add('597', 'Turquoise', 91, 163, 179, 'row 08-16')
        self._add('598', 'Turquoise Light', 144, 195, 204, 'row 08-15')
        self._add('600', 'Cranberry Very Dark', 205, 47, 99, 'row 03-17')
        self._add('601', 'Cranberry Dark', 209, 40, 106, 'row 03-16')
        self._add('602', 'Cranberry Medium', 226, 72, 116, 'row 03-15')
        self._add('603', 'Cranberry', 255, 164, 190, 'row 03-14')
        self._add('604', 'Cranberry Light', 255, 176, 190, 'row 03-13')
        self._add('605', 'Cranberry Very Light', 255, 192, 205, 'row 03-12')
        self._add('606', 'Orange Red Bright', 250, 50, 3, 'row 14-26')
        self._add('608', 'Burnt Orange Bright', 253, 93, 53, 'row 14-25')
        self._add('610', 'Drab Brown Dk', 121, 96, 71, 'row 13-04')
        self._add('611', 'Drab Brown', 150, 118, 86, 'row 13-03')
        self._add('612', 'Drab Brown Lt', 188, 154, 120, 'row 13-02')
        self._add('613', 'Drab Brown V Lt', 220, 196, 170, 'row 13-01')
        self._add('632', 'Desert Sand Ult Vy Dk', 135, 85, 57, 'row 16-25')
        self._add('640', 'Beige Gray Vy Dk', 133, 123, 97, 'row 18-08')
        self._add('642', 'Beige Gray Dark', 164, 152, 120, 'row 18-07')
        self._add('644', 'Beige Gray Med', 221, 216, 203, 'row 18-06')
        self._add('645', 'Beaver Gray Vy Dk', 110, 101, 92, 'row 19-05')
        self._add('646', 'Beaver Gray Dk', 135, 125, 115, 'row 19-04')
        self._add('647', 'Beaver Gray Med', 176, 166, 156, 'row 19-03')
        self._add('648', 'Beaver Gray Lt', 188, 180, 172, 'row 19-02')
        self._add('666', 'Bright Red', 227, 29, 66, 'row 01-17')
        self._add('676', 'Old Gold Lt', 229, 206, 151, 'row 13-20')
        self._add('677', 'Old Gold Vy Lt', 245, 236, 203, 'row 13-10')
        self._add('680', 'Old Gold Dark', 188, 141, 14, 'row 13-22')
        self._add('699', 'Green', 5, 101, 23, 'row 11-06')
        self._add('700', 'Green Bright', 7, 115, 27, 'row 11-05')
        self._add('701', 'Green Light', 63, 143, 41, 'row 11-04')
        self._add('702', 'Kelly Green', 71, 167, 47, 'row 11-03')
        self._add('703', 'Chartreuse', 123, 181, 71, 'row 11-02')
        self._add('704', 'Chartreuse Bright', 158, 207, 52, 'row 11-01')
        self._add('712', 'Cream', 255, 251, 239, 'row 17-07')
        self._add('718', 'Plum', 156, 36, 98, 'row 03-24')
        self._add('720', 'Orange Spice Dark', 229, 92, 31, 'row 15-05')
        self._add('721', 'Orange Spice Med', 242, 120, 66, 'row 15-04')
        self._add('722', 'Orange Spice Light', 247, 151, 111, 'row 15-03')
        self._add('725', 'Topaz Med Lt', 255, 200, 64, 'row 14-08')
        self._add('726', 'Topaz Light', 253, 215, 85, 'row 14-07')
        self._add('727', 'Topaz Vy Lt', 255, 241, 175, 'row 14-06')
        self._add('728', 'Topaz', 228, 180, 104, 'row 13-15')
        self._add('729', 'Old Gold Medium', 208, 165, 62, 'row 13-21')
        self._add('730', 'Olive Green V Dk', 130, 123, 48, 'row 12-13')
        self._add('731', 'Olive Green Dk', 147, 139, 55, 'row 12-12')
        self._add('732', 'Olive Green', 148, 140, 54, 'row 12-11')
        self._add('733', 'Olive Green Md', 188, 179, 76, 'row 12-10')
        self._add('734', 'Olive Green Lt', 199, 192, 119, 'row 12-09')
        self._add('738', 'Tan Very Light', 236, 204, 158, 'row 17-09')
        self._add('739', 'Tan Ult Vy Lt', 248, 228, 200, 'row 17-08')
        self._add('740', 'Tangerine', 255, 139, 0, 'row 14-15')
        self._add('741', 'Tangerine Med', 255, 163, 43, 'row 14-14')
        self._add('742', 'Tangerine Light', 255, 191, 87, 'row 14-13')
        self._add('743', 'Yellow Med', 254, 211, 118, 'row 14-12')
        self._add('744', 'Yellow Pale', 255, 231, 147, 'row 14-11')
        self._add('745', 'Yellow Pale Light', 255, 233, 173, 'row 14-10')
        self._add('746', 'Off White', 252, 252, 238, 'row 13-09')
        self._add('747', 'Peacock Blue Vy Lt', 229, 252, 253, 'row 08-09')
        self._add('754', 'Peach Light', 247, 203, 191, 'row 16-07')
        self._add('758', 'Terra Cotta Vy Lt', 238, 170, 155, 'row 16-09')
        self._add('760', 'Salmon', 245, 173, 173, 'row 01-03')
        self._add('761', 'Salmon Light', 255, 201, 201, 'row 01-02')
        self._add('762', 'Pearl Gray Vy Lt', 236, 236, 236, 'row 19-07')
        self._add('772', 'Yellow Green Vy Lt', 228, 236, 212, 'row 10-20')
        self._add('775', 'Baby Blue Very Light', 217, 235, 241, 'row 07-05')
        self._add('776', 'Pink Medium', 252, 176, 185, 'row 02-19')
        self._add('777', 'Raspberry Very Dark', 145, 53, 70, 'row 02-16')
        self._add('778', 'Antique Mauve Vy Lt', 223, 179, 187, 'row 04-08')
        self._add('779', 'Cocoa Dark', 98, 75, 69, 'row 17-06')
        self._add('780', 'Topaz Ultra Vy Dk', 148, 99, 26, 'row 13-19')
        self._add('781', 'Topaz Very Dark', 162, 109, 32, 'row 13-18')
        self._add('782', 'Topaz Dark', 174, 119, 32, 'row 13-17')
        self._add('783', 'Topaz Medium', 206, 145, 36, 'row 13-16')
        self._add('791', 'Cornflower Blue V D', 70, 69, 99, 'row 05-25')
        self._add('792', 'Cornflower Blue Dark', 85, 91, 123, 'row 05-23')
        self._add('793', 'Cornflower Blue Med', 112, 125, 162, 'row 05-21')
        self._add('794', 'Cornflower Blue Light', 143, 156, 193, 'row 05-20')
        self._add('796', 'Royal Blue Dark', 17, 65, 109, 'row 06-09')
        self._add('797', 'Royal Blue', 19, 71, 125, 'row 06-08')
        self._add('798', 'Delft Blue Dark', 70, 106, 142, 'row 06-07')
        self._add('799', 'Delft Blue Medium', 116, 142, 182, 'row 06-06')
        self._add('800', 'Delft Blue Pale', 192, 204, 222, 'row 06-04')
        self._add('801', 'Coffee Brown Dk', 101, 57, 25, 'row 17-15')
        self._add('803', 'Baby Blue Ult Vy Dk', 44, 89, 124, 'row 07-12')
        self._add('806', 'Peacock Blue Dark', 61, 149, 165, 'row 08-12')
        self._add('807', 'Peacock Blue', 100, 171, 186, 'row 08-11')
        self._add('809', 'Delft Blue', 148, 168, 198, 'row 06-05')
        self._add('813', 'Blue Light', 161, 194, 215, 'row 06-13')
        self._add('814', 'Garnet Dark', 123, 0, 27, 'row 01-23')
        self._add('815', 'Garnet Medium', 135, 7, 31, 'row 01-22')
        self._add('816', 'Garnet', 151, 11, 35, 'row 01-21')
        self._add('817', 'Coral Red Very Dark', 187, 5, 31, 'row 01-12')
        self._add('818', 'Baby Pink', 255, 223, 217, 'row 02-05')
        self._add('819', 'Baby Pink Light', 255, 238, 235, 'row 02-17')
        self._add('820', 'Royal Blue Very Dark', 14, 54, 92, 'row 06-10')
        self._add('822', 'Beige Gray Light', 231, 226, 211, 'row 18-05')
        self._add('823', 'Navy Blue Dark', 33, 48, 99, 'row 07-14')
        self._add('824', 'Blue Very Dark', 57, 105, 135, 'row 06-16')
        self._add('825', 'Blue Dark', 71, 129, 165, 'row 06-15')
        self._add('826', 'Blue Medium', 107, 158, 191, 'row 06-14')
        self._add('827', 'Blue Very Light', 189, 221, 237, 'row 06-12')
        self._add('828', 'Sky Blue Vy Lt', 197, 232, 237, 'row 08-01')
        self._add('829', 'Golden Olive Vy Dk', 126, 107, 66, 'row 12-25')
        self._add('830', 'Golden Olive Dk', 141, 120, 75, 'row 12-24')
        self._add('831', 'Golden Olive Md', 170, 143, 86, 'row 12-23')
        self._add('832', 'Golden Olive', 189, 155, 81, 'row 12-22')
        self._add('833', 'Golden Olive Lt', 200, 171, 108, 'row 12-21')
        self._add('834', 'Golden Olive Vy Lt', 219, 190, 127, 'row 12-20')
        self._add('838', 'Beige Brown Vy Dk', 89, 73, 55, 'row 18-25')
        self._add('839', 'Beige Brown Dk', 103, 85, 65, 'row 18-24')
        self._add('840', 'Beige Brown Med', 154, 124, 92, 'row 18-23')
        self._add('841', 'Beige Brown Lt', 182, 155, 126, 'row 18-22')
        self._add('842', 'Beige Brown Vy Lt', 209, 186, 161, 'row 18-21')
        self._add('844', 'Beaver Gray Ult Dk', 72, 72, 72, 'row 19-06')
        self._add('869', 'Hazelnut Brown V Dk', 131, 94, 57, 'row 13-14')
        self._add('890', 'Pistachio Grn Ult V D', 23, 73, 35, 'row 10-14')
        self._add('891', 'Carnation Dark', 255, 87, 115, 'row 02-04')
        self._add('892', 'Carnation Medium', 255, 121, 140, 'row 02-03')
        self._add('893', 'Carnation Light', 252, 144, 162, 'row 02-02')
        self._add('894', 'Carnation Very Light', 255, 178, 187, 'row 02-01')
        self._add('895', 'Hunter Green Vy Dk', 27, 83, 0, 'row 10-25')
        self._add('898', 'Coffee Brown Vy Dk', 73, 42, 19, 'row 17-16')
        self._add('899', 'Rose Medium', 242, 118, 136, 'row 02-20')
        self._add('900', 'Burnt Orange Dark', 209, 88, 7, 'row 14-20')
        self._add('902', 'Garnet Very Dark', 130, 38, 55, 'row 04-14')
        self._add('904', 'Parrot Green V Dk', 85, 120, 34, 'row 11-10')
        self._add('905', 'Parrot Green Dk', 98, 138, 40, 'row 11-09')
        self._add('906', 'Parrot Green Md', 127, 179, 53, 'row 11-08')
        self._add('907', 'Parrot Green Lt', 199, 230, 102, 'row 11-07')
        self._add('909', 'Emerald Green Vy Dk', 21, 111, 73, 'row 10-07')
        self._add('910', 'Emerald Green Dark', 24, 126, 86, 'row 10-06')
        self._add('911', 'Emerald Green Med', 24, 144, 101, 'row 10-05')
        self._add('912', 'Emerald Green Lt', 27, 157, 107, 'row 10-04')
        self._add('913', 'Nile Green Med', 109, 171, 119, 'row 10-03')
        self._add('915', 'Plum Dark', 130, 0, 67, 'row 03-26')
        self._add('917', 'Plum Medium', 155, 19, 89, 'row 03-25')
        self._add('918', 'Red Copper Dark', 130, 52, 10, 'row 15-11')
        self._add('919', 'Red Copper', 166, 69, 16, 'row 15-10')
        self._add('920', 'Copper Med', 172, 84, 20, 'row 15-09')
        self._add('921', 'Copper', 198, 98, 24, 'row 15-08')
        self._add('922', 'Copper Light', 226, 115, 35, 'row 15-07')
        self._add('924', 'Gray Green Vy Dark', 86, 106, 106, 'row 08-24')
        self._add('926', 'Gray Green Med', 152, 174, 174, 'row 08-22')
        self._add('927', 'Gray Green Light', 189, 203, 203, 'row 08-21')
        self._add('928', 'Gray Green Vy Lt', 221, 227, 227, 'row 08-20')
        self._add('930', 'Antique Blue Dark', 69, 92, 113, 'row 07-20')
        self._add('931', 'Antique Blue Medium', 106, 133, 158, 'row 07-19')
        self._add('932', 'Antique Blue Light', 162, 181, 198, 'row 07-18')
        self._add('934', 'Avocado Grn Black', 49, 57, 25, 'row 11-18')
        self._add('935', 'Avocado Green Dk', 66, 77, 33, 'row 11-17')
        self._add('936', 'Avocado Grn V Dk', 76, 88, 38, 'row 11-16')
        self._add('937', 'Avocado Green Md', 98, 113, 51, 'row 11-15')
        self._add('938', 'Coffee Brown Ult Dk', 54, 31, 14, 'row 17-17')
        self._add('939', 'Navy Blue Very Dark', 27, 40, 83, 'row 07-15')
        self._add('943', 'Green Bright Md', 61, 147, 132, 'row 09-06')
        self._add('945', 'Tawny', 251, 213, 187, 'row 15-13')
        self._add('946', 'Burnt Orange Med', 235, 99, 7, 'row 14-19')
        self._add('947', 'Burnt Orange', 255, 123, 77, 'row 14-18')
        self._add('948', 'Peach Very Light', 254, 231, 218, 'row 16-06')
        self._add('950', 'Desert Sand Light', 238, 211, 196, 'row 16-20')
        self._add('951', 'Tawny Light', 255, 226, 207, 'row 15-01')
        self._add('954', 'Nile Green', 136, 186, 145, 'row 10-02')
        self._add('955', 'Nile Green Light', 162, 214, 173, 'row 10-01')
        self._add('956', 'Geranium', 255, 145, 145, 'row 02-07')
        self._add('957', 'Geranium Pale', 253, 181, 181, 'row 02-06')
        self._add('958', 'Sea Green Dark', 62, 182, 161, 'row 09-03')
        self._add('959', 'Sea Green Med', 89, 199, 180, 'row 09-02')
        self._add('961', 'Dusty Rose Dark', 207, 115, 115, 'row 02-12')
        self._add('962', 'Dusty Rose Medium', 230, 138, 138, 'row 02-11')
        self._add('963', 'Dusty Rose Ult Vy Lt', 255, 215, 215, 'row 02-09')
        self._add('964', 'Sea Green Light', 169, 226, 216, 'row 09-01')
        self._add('966', 'Jade Ultra Vy Lt', 185, 215, 192, 'row 09-12')
        self._add('967', 'Apricot Very Light', 255, 222, 213, 'row 14-21')
        self._add('970', 'Pumpkin Light', 247, 139, 19, 'row 14-16')
        self._add('971', 'Pumpkin', 246, 127, 0, 'row 14-17')
        self._add('972', 'Canary Deep', 255, 181, 21, 'row 14-09')
        self._add('973', 'Canary Bright', 255, 227, 0, 'row 14-03')
        self._add('975', 'Golden Brown Dk', 145, 79, 18, 'row 16-05')
        self._add('976', 'Golden Brown Med', 194, 129, 66, 'row 16-03')
        self._add('977', 'Golden Brown Light', 220, 156, 86, 'row 16-02')
        self._add('986', 'Forest Green Vy Dk', 64, 82, 48, 'row 10-19')
        self._add('987', 'Forest Green Dk', 88, 113, 65, 'row 10-18')
        self._add('988', 'Forest Green Med', 115, 139, 91, 'row 10-17')
        self._add('989', 'Forest Green ', 141, 166, 117, 'row 10-16')
        self._add('991', 'Aquamarine Dk', 71, 123, 110, 'row 09-11')
        self._add('992', 'Aquamarine Lt', 111, 174, 159, 'row 09-09')
        self._add('993', 'Aquamarine Vy Lt', 144, 192, 180, 'row 09-08')
        self._add('995', 'Electric Blue Dark', 38, 150, 182, 'row 06-19')
        self._add('996', 'Electric Blue Medium', 48, 194, 236, 'row 06-17')
        self._add('B5200', 'Snow White', 255, 255, 255, 'row 18-01')
        self._add('Ecru', 'Ecru', 240, 234, 218, 'row 18-04')
        self._add('White', 'White', 252, 251, 248, 'row 18-02')