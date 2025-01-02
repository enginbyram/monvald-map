import mapnik

m = mapnik.Map(400,320)
m.background = mapnik.Color('ghostwhite')
mapnik.render_to_file(m, '010-background.png', 'png')