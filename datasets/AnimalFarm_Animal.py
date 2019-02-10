{'name': 'AnimalFarm_Animal',
 'columns': [('farmtype', Lookup.ANIMAL_FARM_HOUSE, {'label': 'Animal building'}),
             ('CubId', Lookup.PROP, {'label': 'Baby animal'}),
             ('Name', Lookup.TRANSLATION, {'label': 'Adult animal'}),
             ('TotalPoint', None, {'label': 'Total point*'}),
             ('StandardPoint', None, {'label': 'Standard point*'}),
             ('ProductionCycle', None, {'label': 'Production cycle*'}),
             ('touchcoef', None, {'label': 'Effect of petting animal*'}),
             ('FoodRalation', Lookup.PROP, {'split': ';',
                                            'quantity_post': ',',
                                            'label': 'Favorite food*'}),
             ('FoodCanEat', None, {'label': 'Food eaten per day'}),
             ('ShitNum', None, {'label': 'Feces made per day'}),
             ('SpeedRegion', None, {'label': 'Movement speed of animal*'}),
             ('Price', None, {'label': 'Market price'}),
             ('Product', Lookup.ITEM_DROP_FIXED, {'label': 'Daily animal drops'}),
             ('Product_Extra', Lookup.ITEM_DROP_FIXED, {'label': 'Extra animal drops'})]}