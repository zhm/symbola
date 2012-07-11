import fontforge

font = fontforge.font()

font.fontname   = "Symbola"
font.fullname   = "Symbola"
font.familyname = "Symbola"

for i in range(1, 268):
  glyph = font.createChar(i + 8447)

  glyph.importOutlines("svg/%s.svg" %i)

  ymin = glyph.boundingBox()[1]
  glyph.transform([1, 0, 0, 1, 0, -ymin])
  glyph.autoHint()

  glyph.left_side_bearing = glyph.right_side_bearing = 10

font.generate("fonts/Symbola.pfb", flags=["tfm", "afm"])
font.generate("fonts/Symbola.otf")
font.generate("fonts/Symbola.ttf")
