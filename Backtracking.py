class Subject:
    def __init__(self, attribute_array):
        self.name = attribute_array[0]
        self.subject_code = attribute_array[1]
        self.semester = attribute_array[2]
        self.sks = int (attribute_array[3])
        self.day = attribute_array[4]
        self.start_hour = attribute_array[5]
        self.end_hour = attribute_array[6]
        self.class_name = attribute_array[7]
        self.lecturer = attribute_array[8]

class Backtracking:
    def __init__(self, input_file, user_semester):
        self.subject_arr = []

        # User inputs
        self.user_semester = user_semester

        for line in input_file:
            self.attribute_array = line.split()
            if '-' in self.attribute_array:
                continue
            self.subject = Subject(self.attribute_array)
            self.subject_arr.append(self.subject)
    
    def find_combinations(self):
        self.intervals = []
        self.path = []
        self.results = []
        self.sks_total = 0

        self.backtrack()
        self.printResults()
    
    def backtrack(self):
        if self.sks_total > 18 and self.sks_total < 24:
            if self.path:
                self.results.append(self.path)
            return

        print("langkah bt")
        for a in self.subject_arr:
            # Mencocokkan semester
            if int(a.semester) != int(self.user_semester):
                continue

            self.flag = 0

            # Memeriksa apakah mata kuliah sudah diambil atau tidak
            for subj in self.path:
                if a.name == subj.name:
                    self.flag = 1
                    break

            # Memeriksa apakah waktu sudah terpakai atau tidak
            for times in self.intervals:
                # print(int(a.start_hour) , " = " , int(times[0]))
                # print(int(a.end_hour) , " = " , int(times[1]))
                # if(int(a.start_hour)<int(times[1])):
                #     print("fizz")

                # if(int(a.end_hour)>int(times[0])):
                #     print("buzz")

                # print("------")
                if (int(a.start_hour) < int(times[1])) and (int(a.end_hour) > int(times[0])):
                    self.flag = 1
                    break

            if self.flag == 1:
                continue

            self.path.append(a)
            self.intervals.append((a.start_hour, a.end_hour))
            self.sks_total += a.sks

            self.backtrack()

    def printResults(self):
        for a in self.results:
            for subj in a:
                print(subj.name + subj.subject_code)
        print("------------------------")

def main():
    input_file = open('jadwal22-23.txt', 'r')
    # user_semester = input("Enter Semester: ")
    user_semester = 4
    bt = Backtracking(input_file, user_semester)
    bt.find_combinations()

if __name__ == "__main__":
    main()
