
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
        """This function receives a key and return a list with all the keys from Researchs.json
                    (it can be used for retreiving the names, groups, conditions, description, data_section, treshold
                     and researcher in charge's name).
                           :param key: The key we want to get a list from.
                           :type key: String
                           :return: key_array
                           :rtype: List
                           """
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
        """This function updates the correspond JSON file and the research chosen.
                                   :param research_name: Research's name
                                   :type research_name: String
                                   :param res_array: The research's details.
                                   :type res_array: List
                                   :return: NONE
                                   """
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

    def get_group_data(self, research_name, group):
        """This function calculates all the graph attributes of a specific group and research.
                                           :param research_name: Research's name
                                           :type research_name: String
                                           :param group: Group's name.
                                           :type group: String
                                           :return: density, shortest_path_length, min_degree, max_degree, degree, local_efficiency
                                           :rtype: float
                                           """
        from undirectedGraph import Graph
        import numpy
        with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Patients.json') as json_file:
            patients_counter = 0
            shortest_path_length = 0
            density = 0
            modularity = 0
            min_degree = 0
            max_degree = 0
            min_efficiency = 0
            max_efficiency = 0
            degree = 0
            local_efficiency = 0
            data = json.load(json_file)
            for res in data['Patients']:
                if (res['research_name'] == research_name) and (res['group'] == group):
                    patients_counter = patients_counter + 1
                    for cond in ['B','C','D']:
                        g = Graph()
                        g.create_nodes(g.create_edges(res['full_name'] + '-' + cond))

                        shortest_path_length = shortest_path_length + g.shortest_paths
                        density = density + g.density
                        # modularity
                        min_degree = min_degree + g.min_degree()
                        max_degree = max_degree + g.max_degree()

                        # degree = numpy.array(degree)
                        print(numpy.array(g.degrees))
                        degree = degree + numpy.array(g.degrees)
                        local_efficiency = local_efficiency + numpy.array(g.locals_efficiency)
            print((density/patients_counter),(shortest_path_length/patients_counter),(min_degree/patients_counter), (max_degree/patients_counter), (degree/patients_counter), (local_efficiency/patients_counter))
            return (density/patients_counter),(shortest_path_length/patients_counter),(min_degree/patients_counter),(max_degree/patients_counter),(degree/patients_counter),(local_efficiency/patients_counter)

    def get_condition_data(self, research_name, group, condition):
        """This function calculates all the graph attributes of a specific conddition, group and research.
                                                   :param research_name: Research's name
                                                   :type research_name: String
                                                   :param group: Group's name.
                                                   :type group: String
                                                   :param condition: Condition's name.
                                                   :type condition: String
                                                   :return: density, shortest_path_length, min_degree, max_degree, degree, local_efficiency
                                                   :rtype: float
                                                   """
        from undirectedGraph import Graph
        import numpy
        with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Patients.json') as json_file:
            patients_counter = 0
            shortest_path_length = 0
            density = 0
            modularity = 0
            min_degree = 0
            max_degree = 0
            min_efficiency = 0
            max_efficiency = 0
            degree = 0
            local_efficiency = 0
            data = json.load(json_file)
            for res in data['Patients']:
                if (res['research_name'] == research_name) and (res['group'] == group):
                    patients_counter = patients_counter + 1
                    g = Graph()
                    g.create_nodes(g.create_edges(res['full_name'] + '-' + condition))
                    print(res['full_name'] + '-' + condition + '-->' + res['group'])

                    shortest_path_length = shortest_path_length + g.shortest_paths
                    density = density + g.density
                    # modularity
                    min_degree = min_degree + g.min_degree()
                    max_degree = max_degree + g.max_degree()

                    # degree = numpy.array(degree)
                    print(numpy.array(g.degrees))
                    degree = degree + numpy.array(g.degrees)
                    local_efficiency = local_efficiency + numpy.array(g.locals_efficiency)
            print((density/patients_counter),(shortest_path_length/patients_counter),(min_degree/patients_counter), (max_degree/patients_counter), (degree/patients_counter), (local_efficiency/patients_counter))
            return (density/patients_counter),(shortest_path_length/patients_counter),(min_degree/patients_counter),(max_degree/patients_counter),(degree/patients_counter),(local_efficiency/patients_counter)


if __name__ == '__main__':
    r2 = Research("researchName", "groups","conditions", "description", "data_section", "treshold", "researcherInCharge")
    # print(r2.get_data_from_JSON('name'))
    # print(set(r2.get_data_from_JSON('groups')))
    # print(r2.get_researchs_from_JSON('Research3'))
    # r2.is_in_key('Research3','groups','Group1')
    # density, shortest_path, min_degree, max_degree, degrees, local_efficiency = r2.get_group_data('Research4','G1')
    # print(density, shortest_path, min_degree, max_degree, degrees, local_efficiency)


