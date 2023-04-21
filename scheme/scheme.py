from palettes.core_palette import CorePalette
import json


class Scheme:
    def __init__(self, props):
        self.props = props

    @staticmethod
    def default():
        return {
            "light": {
                "primary": [103, 80, 164],
                "primaryContainer": [234, 221, 255],
                "onPrimary": [255, 255, 255],
                "onPrimaryContainer": [33, 0, 94],
                "inversePrimary": [208, 188, 255],
                "secondary": [98, 91, 113],
                "secondaryContainer": [232, 222, 248],
                "onSecondary": [255, 255, 255],
                "onSecondaryContainer": [30, 25, 43],
                "tertiary": [125, 82, 96],
                "tertiaryContainer": [255, 216, 228],
                "onTertiary": [255, 255, 255],
                "onTertiaryContainer": [55, 11, 30],
                "surface": [254, 247, 255],
                "surfaceDim": [222, 216, 225],
                "surfaceBright": [254, 247, 255],
                "surfaceContainerLowest": [255, 255, 255],
                "surfaceContainerLow": [247, 242, 250],
                "surfaceContainer": [243, 237, 247],
                "surfaceContainerHigh": [236, 230, 240],
                "surfaceContainerHighest": [230, 224, 233],
                "surfaceVariant": [231, 224, 236],
                "onSurface": [28, 27, 31],
                "onSurfaceVariant": [73, 69, 78],
                "inverseSurface": [49, 48, 51],
                "inverseOnSurface": [244, 239, 244],
                "background": [254, 247, 255],
                "onBackground": [28, 27, 31],
                "error": [179, 38, 30],
                "errorContainer": [249, 222, 220],
                "onError": [255, 255, 255],
                "onErrorContainer": [65, 14, 11],
                "outline": [121, 116, 126],
                "outlineVariant": [196, 199, 197],
                "shadow": [0, 0, 0],
                "surfaceTint": [103, 80, 164],
                "scrim": [0, 0, 0],
            },
            "dark": {
                "primary": [208, 188, 255],
                "primaryContainer": [79, 55, 139],
                "onPrimary": [55, 30, 115],
                "onPrimaryContainer": [234, 221, 255],
                "inversePrimary": [103, 80, 164],
                "secondary": [204, 194, 220],
                "secondaryContainer": [74, 68, 88],
                "onSecondary": [51, 45, 65],
                "onSecondaryContainer": [232, 222, 248],
                "tertiary": [239, 184, 200],
                "tertiaryContainer": [99, 59, 72],
                "onTertiary": [73, 37, 50],
                "onTertiaryContainer": [255, 216, 228],
                "surface": [20, 18, 24],
                "surfaceDim": [20, 18, 24],
                "surfaceBright": [59, 56, 62],
                "surfaceContainerLowest": [15, 13, 19],
                "surfaceContainerLow": [29, 27, 32],
                "surfaceContainer": [33, 31, 38],
                "surfaceContainerHigh": [43, 41, 48],
                "surfaceContainerHighest": [54, 52, 59],
                "surfaceVariant": [73, 69, 79],
                "onSurface": [230, 225, 229],
                "onSurfaceVariant": [202, 196, 208],
                "inverseSurface": [230, 225, 229],
                "inverseOnSurface": [49, 48, 51],
                "background": [20, 18, 24],
                "onBackground": [230, 225, 229],
                "error": [242, 184, 181],
                "errorContainer": [140, 29, 24],
                "onError": [96, 20, 16],
                "onErrorContainer": [249, 222, 220],
                "outline": [147, 143, 153],
                "outlineVariant": [68, 71, 70],
                "shadow": [0, 0, 0],
                "surfaceTint": [208, 188, 255],
                "scrim": [0, 0, 0],
            },
        }

    @staticmethod
    def light(argb):
        core = CorePalette.of(argb)
        return Scheme(
            {
                "primary": core.a1.tone(40),
                "primaryContainer": core.a1.tone(90),
                "onPrimary": core.a1.tone(100),
                "onPrimaryContainer": core.a1.tone(10),
                "inversePrimary": core.a1.tone(80),
                "secondary": core.a2.tone(40),
                "secondaryContainer": core.a2.tone(90),
                "onSecondary": core.a2.tone(100),
                "onSecondaryContainer": core.a2.tone(10),
                "tertiary": core.a3.tone(40),
                "tertiaryContainer": core.a3.tone(90),
                "onTertiary": core.a3.tone(100),
                "onTertiaryContainer": core.a3.tone(10),
                "surface": core.n1.tone(98),
                "surfaceDim": core.n1.tone(87),
                "surfaceBright": core.n1.tone(98),
                "surfaceContainerLowest": core.n1.tone(100),
                "surfaceContainerLow": core.n1.tone(96),
                "surfaceContainer": core.n1.tone(94),
                "surfaceContainerHigh": core.n1.tone(92),
                "surfaceContainerHighest": core.n1.tone(90),
                "surfaceVariant": core.n2.tone(90),
                "onSurface": core.n1.tone(10),
                "onSurfaceVariant": core.n2.tone(30),
                "inverseSurface": core.n1.tone(20),
                "inverseOnSurface": core.n1.tone(95),
                "background": core.n1.tone(98),
                "onBackground": core.n1.tone(10),
                "error": core.error.tone(40),
                "errorContainer": core.error.tone(90),
                "onError": core.error.tone(100),
                "onErrorContainer": core.error.tone(10),
                "outline": core.n2.tone(50),
                "outlineVariant": core.n2.tone(80),
                "shadow": core.n1.tone(0),
                "surfaceTint": core.a1.tone(50),  # This tone was not given
                "scrim": core.n1.tone(0),
            }
        )

    @staticmethod
    def dark(argb):
        core = CorePalette.of(argb)
        return Scheme(
            {
                "primary": core.a1.tone(80),
                "primaryContainer": core.a1.tone(30),
                "onPrimary": core.a1.tone(20),
                "onPrimaryContainer": core.a1.tone(90),
                "inversePrimary": core.a1.tone(40),
                "secondary": core.a2.tone(80),
                "secondaryContainer": core.a2.tone(30),
                "onSecondary": core.a2.tone(20),
                "onSecondaryContainer": core.a2.tone(90),
                "tertiary": core.a3.tone(80),
                "tertiaryContainer": core.a3.tone(30),
                "onTertiary": core.a3.tone(20),
                "onTertiaryContainer": core.a3.tone(90),
                "surface": core.n1.tone(6),
                "surfaceDim": core.n1.tone(6),
                "surfaceBright": core.n1.tone(24),
                "surfaceContainerLowest": core.n1.tone(4),
                "surfaceContainerLow": core.n1.tone(10),
                "surfaceContainer": core.n1.tone(12),
                "surfaceContainerHigh": core.n1.tone(17),
                "surfaceContainerHighest": core.n1.tone(22),
                "surfaceVariant": core.n2.tone(30),
                "onSurface": core.n1.tone(90),
                "onSurfaceVariant": core.n2.tone(80),
                "inverseSurface": core.n1.tone(90),
                "inverseOnSurface": core.n1.tone(20),
                "background": core.n1.tone(6),
                "onBackground": core.n1.tone(90),
                "error": core.error.tone(80),
                "errorContainer": core.error.tone(30),
                "onError": core.error.tone(20),
                "onErrorContainer": core.error.tone(90),
                "outline": core.n2.tone(60),
                "outlineVariant": core.n2.tone(30),
                "shadow": core.n1.tone(0),
                "surfaceTint": core.a1.tone(30),  # This tone was not given
                "scrim": core.n1.tone(0),
            }
        )

    def toJSON(self):
        return json.dumps(self.props)
