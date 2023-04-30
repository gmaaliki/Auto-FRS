class Schedule:
    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            for line in file:
                self.attribute_array = line.split()
                self.name = self.attribute_array[0]
                self.subject_code = self.attribute_array[1]
                self.semester = self.attribute_array[2]
                self.day = self.attribute_array[3]
                self.start_hour = self.attribute_array[4]
                self.end_hour = self.attribute_array[5]
                self.class_name = self.attribute_array[6]
                self.lecturer = self.attribute_array[7]

class Backtracking:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.results = []
    
    def find_combinations(self):
        self.backtrack([], self.nums, self.target)
        return self.results
    
    def backtrack(self, path, nums, target):
        if target == 0:
            self.results.append(path)
            return
        if target < 0:
            return
        for i in range(len(nums)):
            new_path = path + [nums[i]]
            new_target = target - nums[i]
            self.backtrack(new_path, nums[i:], new_target)

def main():

    obj = Schedule()

if __name__ == "__main__":
    main()
