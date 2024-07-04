"""Temporary Class to bundle module description information."""
class Module:
    def __init__(self, title_en=None, title_de=None, assessment_methods_en=None, assessment_methods_de=None, 
                 recommended_prerequisites_en=None, recommended_prerequisites_de=None, content_en=None, content_de=None, 
                 intended_learning_outcomes_en=None, intended_learning_outcomes_de=None, teaching_and_learning_methods_en=None, 
                 teaching_and_learning_methods_de=None, media_en=None, media_de=None, reading_list_en=None, reading_list_de=None, 
                 description_bullet_points_en=None, description_bullet_points_de=None, language='en'):
        self.language = language
        self.title_en = title_en
        self.title_de = title_de
        self.assessment_methods_en = assessment_methods_en
        self.assessment_methods_de = assessment_methods_de
        self.recommended_prerequisites_en = recommended_prerequisites_en
        self.recommended_prerequisites_de = recommended_prerequisites_de
        self.content_en = content_en
        self.content_de = content_de
        self.intended_learning_outcomes_en = intended_learning_outcomes_en
        self.intended_learning_outcomes_de = intended_learning_outcomes_de
        self.teaching_and_learning_methods_en = teaching_and_learning_methods_en
        self.teaching_and_learning_methods_de = teaching_and_learning_methods_de
        self.media_en = media_en
        self.media_de = media_de
        self.reading_list_en = reading_list_en
        self.reading_list_de = reading_list_de
        self.description_bullet_points_en = description_bullet_points_en
        self.description_bullet_points_de = description_bullet_points_de

    def switch_language(self, language):
        if language in ['en', 'de']:
            self.language = language
        else:
            raise ValueError("Unsupported language")

    def print_pretty(self):
        if self.language == 'en':
            print(f"""
Module({self.title_en})
    Prerequisites (recommended):    {self.recommended_prerequisites_en},
    Content:                        {self.content_en},
    Intended Learning Outcomes:     {self.intended_learning_outcomes_en},
    Teaching and Learning Methods:  {self.teaching_and_learning_methods_en},
    Media:                          {self.media_en},
    Reading List:                   {self.reading_list_en},
    Bullet Points:                  {self.description_bullet_points_en}
""")
        elif self.language == 'de':
            print(f"""
Module({self.title_de})
    Prerequisites (recommended):    {self.recommended_prerequisites_de},
    Content:                        {self.content_de},
    Intended Learning Outcomes:     {self.intended_learning_outcomes_de},
    Teaching and Learning Methods:  {self.teaching_and_learning_methods_de},
    Media:                          {self.media_de},
    Reading List:                   {self.reading_list_de},
    Bullet Points:                  {self.description_bullet_points_de}
""")