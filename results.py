import tkinter
import tkinter.filedialog as fd
import json
import pandas
import numpy

class results(object):
    def __init__(self, researchName):
        self.name = researchName
        self.researchers = []
        self.groups = []
        self.conditions = []
        self.description = []

    def set_researchers(self, researchers):
        self.researchers.append(researchers)

    def set_groups(self, groups):
        self.groups.append(groups)

    def set_conditions(self, conditions):
        self.conditions.append(conditions)

    def set_description(self, description):
        self.description.append(description)

    def chooseFile(self):
        root = tkinter.Tk()
        root.withdraw()  # use to hide tkinter window

        fname = fd.askopenfilename(filetypes=(("All files", "*.type"), ("All files", "*")))
        print(fname)
        print(type(fname))

        if  (fname == ""):
            print("no file")
        elif not (fname.endswith(('xlsx', 'xls'))):
            print("wrong file extension")

        return fname

    def uploadResults(self, file_path):
        # With the attribute "usecols" we will load only the right columns, every third column.
        # Our excel files are without "header".
        excelFile = pandas.read_excel(file_path, header=None, usecols = lambda x: x%3==0 in range(69))
        # print(excelFile)
        return excelFile

    def data_section(self, section_number=3.0):
        file_data = self.uploadResults(self.chooseFile())
        # "numpy.einsum" - Evaluates the Einstein summation convention on the operands.
        # Using the Einstein summation convention, many common multi-dimensional, linear algebraic array operations can be represented in a simple fashion. In implicit mode einsum computes these values.
        # In explicit mode, einsum provides further flexibility to compute other array operations that might not be considered classical Einstein summation operations, by disabling, or forcing summation over specified subscript labels.
        print("inside data section: ")
        print(file_data)
        # Number of lines
        print(file_data.shape[0])
        print(type(file_data))
        numpy_file_data = file_data.to_numpy()
        print(numpy_file_data)


        # fill needed rows with the same values as the last row - copy the last row many times as needed
        print(file_data.iloc[-1])
        print(type(file_data.iloc[-1]))
        print(file_data.iloc[[-1]])
        print(type(file_data.iloc[[-1]]))

        remainder = section_number - (file_data.shape[0] % section_number)
        new_file = file_data.append([file_data.iloc[-1]] * remainder, ignore_index=True)
        print(section_number)
        print(remainder)
        print(new_file)
        new_file_data = new_file.to_numpy()
        return pandas.DataFrame(numpy.einsum('ijk->ik', new_file_data.reshape(-1, int(section_number), new_file_data.shape[1])) / section_number)

    def correlation_matrix(self, matrix):
        return matrix.corr()

    def binary_matrix(self, matrix, threshold):
        temp_binary_matrix = pandas.DataFrame()
        print(type(temp_binary_matrix))
        print(matrix[0])
        print(matrix[0].apply(lambda x: 1 if x>threshold else 0))
        for col in range(len(matrix)):
            newCol = matrix.T.loc[col].apply(lambda x: 1 if x>threshold else 0)
            print(newCol)
            print(type(newCol))
            temp_binary_matrix[col] = newCol

        # ------- JSON -----------

        # with open("data_file.json", "w") as write_file:
        #     json.dump(temp_binary_matrix, write_file)
        # --------------------------

        temp_binary_matrix.to_csv(self.name + ".csv", index=False)
        return temp_binary_matrix

if __name__ == '__main__':
    r1 = results("name")
    r1.data_section(5)