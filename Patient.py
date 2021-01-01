import tkinter
import tkinter.filedialog as fd
import json
import os
from pathlib import Path
import pandas
import numpy
import undirectedGraph
from Research import Research

class Patient(object):

    def __init__(self, id, full_name, group, research, file_path):
        self.id = id
        self.full_name = full_name
        self.group = group
        self.research = research
        self.file_path = file_path
        self.und_graph = undirectedGraph.Graph()

    def __str__(self):
        return self.id + self.full_name + self.group + self.research + self.file_path

    def chooseFile(self):
        """This function opens the browser to search a file and returns the file's path.
           :param self: Patient object
           :type self: Patient
           :return: The file'w path.
           :rtype: String
           """
        root = tkinter.Tk()
        root.withdraw()  # use to hide tkinter window

        fname = fd.askopenfilename(filetypes=(("All files", "*.type"), ("All files", "*")))

        if  (fname == ""):
            print("no file")
        elif not (fname.endswith(('xlsx', 'xls'))):
            print("wrong file extension")

        return fname

    def save_in_JSON(self):
        """This function creates a JSON file with all the Researchs - IF the file doesn't exists it will create one with the research object,
            ELSE it will append the research object to the existing file.
                   :param self: research object.
                   :type self: Research
                   :return: NONE
                   """
        s = {"id": self.id, "full_name": self.full_name, "group": self.group,"research_name": self.research, "file_path": self.file_path}
        if not (os.path.exists('Patients.json')):
            with open('Patients.json', 'w') as outfile:
                data = {}
                data['Patients'] = []
                data['Patients'].append(s)
                json.dump(data, outfile, indent=4)
        else:
            print("exists")
            with open('Patients.json', 'r+') as json_file:
                data = json.load(json_file)
                temp = data['Patients']
                print(temp)
                # python object to be appended
                y = {"id": self.id,
                     "full_name": self.full_name,
                     "group": self.group,
                     "research_name": self.research,
                     "file_path": self.file_path}

                # appending data to emp_details
                temp.append(y)
                print(temp)
                json_file.seek(0)
                json.dump(data, json_file, indent=4)

    def get_data_from_JSON(self, key):
        """This function receives a key and return a list with all the keys from Patients.json
            (it can be used for retreiving the groups, conditions and research's name).
                   :param key: The key we want to get a list from.
                   :type key: String
                   :return: key_array
                   :rtype: List
                   """
        fileName = Path(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Patients.json')
        if not(fileName.exists()):
            print("File doesn't exists")
            return False

        else:
            with open(r'\\URI\Users\uriel\PycharmProjects\FinalProject\Gui\Patients.json') as json_file:
                key_array = []
                data = json.load(json_file)
                for group in data['Patients']:
                    key_array.append(group[key])
                return key_array

    def get_treshold_Dsection_from_JSON(self,research_name,treORdsec):
        research = Research('','','','','','','')
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
                        result = res[treORdsec]
                return result

    def uploadResults(self, file_path):
        """This function receives the file_path (excel) and returns a pandas object with the relevant data.
            - With the attribute "usecols" we will load only the right columns, every third column.
            - Our excel files are without "header".
                           :param file_path: The file's path.
                           :type file_path: String
                           :return: excelFile
                           :rtype: Pandas (library) object.
                           """
        ex = self.get_conditions_from_file(file_path)

        excelFile = pandas.read_excel(file_path, header=None, usecols = lambda x: x%3==0 in range(69))
        return excelFile

    def get_conditions_from_file(self,file):
        # filefirst = (file.split("/")[-1]).split("_")[0]  # Example: Get 'sub10' from 'C:/FinalProj/newdata/healthy/sub10_dc_clean.xlsx'
        end_of_file = file.split('.')[-1]
        file_path = file.split("_")[0] # Example: Get 'C:/FinalProj/newdata/healthy/sub10' from 'C:/FinalProj/newdata/healthy/sub10_dc_clean.xlsx'
        print(file_path+'.'+end_of_file)
        file_path = file_path+'.'+end_of_file
        excelFile = pandas.read_excel(file_path, header=None, usecols='BS')
        without_nan = excelFile[70][124:].dropna()
        print(without_nan.to_dict())



    def data_section(self, file_path, section_number=3):
        """This function receives the file's path, data section number and returns a Pandas object.
            "numpy.einsum" - Evaluates the Einstein summation convention on the operands.
            Using the Einstein summation convention, many common multi-dimensional, linear algebraic array operations can be represented in a simple fashion. In implicit mode einsum computes these values.
            In explicit mode, einsum provides further flexibility to compute other array operations that might not be considered classical Einstein summation operations, by disabling, or forcing summation over specified subscript labels.
                           :param file_path: File's path.
                           :type section_number: String
                           :param section_number: Data section.
                           :type section_number: Int
                           :return: Pandas object
                           :rtype: Pandas (library) object.
                           """
        file_data = self.uploadResults(file_path)
        print("inside data section: ")
        print(file_data)
        # Number of rows
        print(file_data.shape[0])
        print(type(file_data))
        numpy_file_data = file_data.to_numpy()
        print(numpy_file_data)

        # fill needed rows with the same values as the last row - copy the last row many times as needed
        print(file_data.iloc[-1])
        print(type(file_data.iloc[-1]))
        print(file_data.iloc[[-1]])
        print(type(file_data.iloc[[-1]]))

        print(type(section_number))

        remainder = int(section_number) - (file_data.shape[0] % int(section_number))
        new_file = file_data.append([file_data.iloc[-1]] * remainder, ignore_index=True)
        print(section_number)
        print(remainder)
        print(new_file)
        new_file_data = new_file.to_numpy()
        return pandas.DataFrame(numpy.einsum('ijk->ik', new_file_data.reshape(-1, int(section_number), new_file_data.shape[1])) / int(section_number))

    def correlation_matrix(self, matrix):
        """This function receives a matrix and returns the correlation matrix.
                            :param matrix: A matrix which every column is a different feature.
                            :type matrix: Pandas object.
                            :return: Pandas object - Correlation matrix.
                            :rtype: Pandas (library) object.
                            """
        return matrix.corr()

    def binary_matrix(self, matrix, threshold):
        """This function receives a correlation matrix and a treshold, calculates the binary matrix depending on the given treshold,
            saves the binary matrix into a CSV file with the name of the patient and returns the binary matrix.
                            :param matrix: A matrix which every column is a different feature.
                            :type matrix: Pandas object.
                            :param threshold: The treshold desired for the binary matrix.
                            :type threshold: Float
                            :return: Pandas object - Binary matrix.
                            :rtype: Pandas (library) object.
                            """
        temp_binary_matrix = pandas.DataFrame()
        print(type(temp_binary_matrix))
        print(matrix[0])
        print(matrix[0].apply(lambda x: 1 if x>float(threshold) else 0))
        for col in range(len(matrix)):
            newCol = matrix.T.loc[col].apply(lambda x: 1 if x>float(threshold) else 0)
            print(newCol)
            print(type(newCol))
            temp_binary_matrix[col] = newCol

        # ---------------- create edges and nodes for the graph ------------ #
        temp_binary_matrix.to_csv(self.full_name + ".csv", index=False)
        self.und_graph.create_nodes(self.und_graph.create_edges(self.full_name))
        return temp_binary_matrix


if __name__ == '__main__':
    r1 = Patient('id', 'Uri', 'group', "res", "file_path")
    # print(r1.get_data_from_JSON(''))
    # r1.binary_matrix(r1.correlation_matrix(r1.data_section(r1.chooseFile(),5)),0.8)
    # print(type(r1.get_treshold_Dsection_from_JSON('Research2','treshold')))
    r1.get_conditions_from_file('C:/FinalProj/newdata/healthy/sub10_dc_clean.xlsx')