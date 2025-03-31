{
   'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base','product', 'account'],
    'data': [
       'security/ir.model.access.csv',
       
      #  'views/property.xml',
        'views/Estate_floor_view.xml',
       
         'views/estate_country_views.xml',
         'views/estate_property_type_views.xml',
         'views/estate_property_views.xml',
         'views/estate_region_views.xml',
         # 'views/estate_sub_city_views.xml',
          'views/parking_space_views.xml',
         'views/parking_wizard.xml',
         "views/region.xml",
         'views/city.xml',
         'wizard/wizard_view.xml',


         #   'views/menu.xml',


    ],
    'application':True,
    "installable":True
}

