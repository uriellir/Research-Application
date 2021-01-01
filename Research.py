
import json
import os
from pathlib import Path

class Research:
    def __init__(self, researchName, groups, conditions, description, data_section, treshold, researcherInCharge):
        self.name = researchName
        self.groups = self.init_comboBox(groups)
        self.conditions = self.init_comboBox(conditions)
        self.description = description
        self.data_section = data_section
        self.treshold = treshold
        self.researchers = researcherInCharge

    def __str__(self):
        return self.name + ', '.join(self.groups) + ', '.join(self.conditions) + self.description + self.data_section + self.treshold + self.researchers

    def init_comboBox (self, item):
        """This function receives a string separated by ',' - separates the words between commas, clean spaces,
            capitalize each value and return a list with the values .
           :param item: values received from a textBox
           :type item: string
           :return: List containing the values of the textBox separated by ',' after relevant cleaning.
           :rtype: List
           """
        item = item.replace(" ", "")
        item = item.split(",")
        item = [value.capitalize() for value in item]
        return item

    def save_in_JSON(self):
        """This function creates a JSON file with all the Researchs - IF the file doesn't exists it will create one with the research object,
            ELSE it will append the research object to the existing file.
                   :param self: research object.
                   :type self: Research
                   :return: NONE
                   """
        s = {"name": self.name, "groups": self.groups, "conditions": self.conditions, "description": self.description,"data_section": self.data_section, "treshold":self.treshold,"researchers":self.researchers}
        if not (os.path.exists('Researchs.json')):
            with open('Researchs.json', 'w') as outfile:
                data = {}
                data['Researchs'] = []
                data['Researchs'].append(s)
                json.dump(data, outfile, indent=4)
        else:
            print("exists")
            with open('Researchs.json', 'r+') as json_file:
                data = json.load(json_file)
                temp = data['Researchs']
                print(temp)
                # python object to be appended
                y = {"name": self.name,
                     "groups": self.groups,
                     "conditions": self.conditions,
                     "description": self.description,
                     "data_section": self.data_section,
                     "treshold":self.treshold,
                     "researchers":self.researchers}

                # appending data to emp_details
                temp.append(y)
                print(temp)
                json_file.seek(0)
                json.dump(data, json_file, indent=4)

    def get_data_from_JSON(self, key):
        """This function receives a key and return a list with all the keys from Researchs.json
            (it can be used for retreiving the names, groups, conditions, description, data_section, treshold
             and researcher in charge's name).
                   :param key: The key we want to get a list from.
                   :type key: String
                   :return: key_array
                   :rtype: List
                   """
        fileName = Path(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json')
        if not(fileName.exists()):
            print("File doesn't exists")
            return False

        else:
            with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json') as json_file:
                key_array = []
                data = json.load(json_file)
                for group in data['Researchs']:
                    if isinstance(group[key], str):
                        key_array.append(group[key])
                    else:
                        key_array = key_array + group[key]
                return list(set(key_array))

    def get_researchs_from_JSON(self, request):
        with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json') as json_file:
            data = json.load(json_file)

            item = next((item for item in data['Researchs'] if item['name'] == request), None) # create a generator via a generator expression, call next to iterate that generator once, and get back the desired object.
            if item:
                return (item)

    def is_in_key(self, res_name, key, str):
        with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json') as json_file:
            data = json.load(json_file)
            data = data['Researchs']
            for res in data:
                if(res['name'] == res_name):
                    if(str in res[key]):
                        print("found - "+res['name'])
                        return True

            return False


    def update_JSON(self,research_name,res_array):
        research = Research('', '', '', '', '', '', '')
        fileName = Path(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json')
        if not (fileName.exists()):
            print("File doesn't exists")
            return False

        else:
            with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json') as json_file:
                key_array = []
                data = json.load(json_file)
                for res in data['Researchs']:
                    if res['name'] == research_name:
                        res['groups'] = res_array[0].split(',')
                        res['conditions'] = res_array[1].split(',')
                        res['description'] = res_array[2]
                        res['data_section'] = res_array[3]
                        res['treshold'] = res_array[4]
                        res['researchers'] = res_array[5]
                with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Researchs.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)


if __name__ == '__main__':

    r2 = Research("researchName", "groups","conditions", "description", "data_section", "treshold", "researcherInCharge")
    # print(r2.get_data_from_JSON('name'))
    # print(set(r2.get_data_from_JSON('groups')))
    # print(r2.get_researchs_from_JSON('Research3'))
    r2.is_in_key('Research3','groups','Group1')



