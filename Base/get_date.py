import yaml
import os
class Get_date:
    @classmethod
    def get_date(self,file_name):
        with open('./Date'+os.sep+file_name, 'r', encoding='utf-8')as f:
            date = yaml.safe_load(f)
        return date.values()




