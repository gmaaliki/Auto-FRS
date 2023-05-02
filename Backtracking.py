class Subject:
    def __init__(self, attribute_array):
        self.name = attribute_array[0]
        self.subject_code = attribute_array[1]
        self.semester = attribute_array[2]
        self.sks = attribute_array[3]
        self.day = attribute_array[4]
        self.start_hour = attribute_array[5]
        self.end_hour = attribute_array[6]
        self.class_name = attribute_array[7]
        self.lecturer = attribute_array[8]

class Backtracking:
    def __init__(self, input_file):
        self.subject_arr = []
        self.intervals = []
        self.line_index = 0
        self.sks_total = 0

        for line in input_file:
            self.attribute_array = line.split()
            if self.attribute_array == '-':
                continue
            self.subject = Subject(self.attribute_array)
            self.subject_arr.append(self.subject)
            self.line_index += 1
    
    def find_combinations(self):
        # self.backtrack([], self.nums, self.target)
        # return self.results
        print("hello")
    
    def backtrack(self, path, nums, target):
        if target == 0:
            # self.results.append(path)
            return
        if target < 0:
            return
        for i in range(len(nums)):
            new_path = path + [nums[i]]
            new_target = target - nums[i]
            self.backtrack(new_path, nums[i:], new_target)

def main():
    input_file = open('jadwal22-23.txt', 'r')
    bt = Backtracking(input_file)
    print(bt.subject_arr[5]. name)

if __name__ == "__main__":
    main()
