class HeartAttackPredictor:
    def __init__(self):
        self.rules = [
            {'age': 60, 'height': 190, 'weight': 90, 'blood_pressure': 140, 'cholesterol_levels': 240, 'result': 'Low'},
            {'age': 50, 'height': 180, 'weight': 80, 'blood_pressure': 130, 'cholesterol_levels': 220, 'result': 'Medium'},
            {'age': 40, 'height': 170, 'weight': 70, 'blood_pressure': 120, 'cholesterol_levels': 200, 'result': 'High'},
            
        ]

    def predict(self, person):
        for rule in self.rules:
            if (person.age >= rule['age'] and
                person.height >= rule['height'] and
                person.weight >= rule['weight'] and
                person.blood_pressure >= rule['blood_pressure'] and
                person.cholesterol_levels >= rule['cholesterol_levels']):
                return rule['result']
        return 'unknown'