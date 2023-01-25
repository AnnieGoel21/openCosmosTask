from osgeo import gdal

options_list = [
    '-ot byte',
    '-of WebP', 
    '-b 1 -b 2 -b 3 ',
    '-outsize 500px 500px'
]

options_string = " ".join(options_list)

gdal.Translate(
    'output_quick_view.webp',
    'Output.TIF',
    options = options_string
)
