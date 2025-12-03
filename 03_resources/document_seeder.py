import os
# THIS IS A ROUGH DRAFT CREATED TO MAKE DATA TO TEST WITH. IT SERVED ITS PURPOSE FOR TESTING SESSION 1 
# (03/12/2025, RUN BY PHILIP RIDGERS) BUT IT'S UNLIKELY TO BE OF USE TO OTHERS IN ITS CURRENT FORM.

from faker import Faker

class MakeFakeData():
    def __init__(self, seed, directory, drop_allow, files_to_create, file_destination):
        self.fake = Faker('en_UK')
        self.seed = seed
        self.directory = directory
        self.drop_allow = drop_allow
        self.files_to_create = files_to_create
        self.file_destination = file_destination
        self.first_number = 1
        self.second_number = 906
        self.counter = 1
        self.set_seed(self.seed)
        self.create_seed_directory(self.directory)
        self.create_drop_allow(self.directory)
        self.create_multiple_files(self.directory, self.file_destination, files_to_create)
        # self.delete_seed_directory("try_this_out", "dropfile")
    def set_seed(self, seed):
        Faker.seed(seed)

    def make_name(self):
        self.name = self.fake.name()
        return self.name
    
    def make_address(self):
        self.address = self.fake.address()
        return self.address

    def create_seed_directory(self, directory_name):
        os.mkdir(directory_name)
        os.mkdir(f"{directory_name}/originals")
        os.mkdir(f"{directory_name}/updates")
        return directory_name
    
    def create_drop_allow(self, directory_name):
        with open(f"{directory_name}/{self.drop_allow}", "w"):
            pass

    def delete_seed_directory(self, directory_name, drop_allow):
        os.rmdir(f"{directory_name}/originals")
        os.rmdir(f"{directory_name}/updates")
        os.remove(f"{directory_name}/{drop_allow}")
        os.rmdir(directory_name)
    
    def create_seed_file(self, directory_name, file_destination):
        self.file_name = self.make_name()
        self.file_details = self.file_name + "\n" + self.make_address()
        self.file_name = self.file_name.split(" ")[-1]
        with open(f"{directory_name}/{file_destination}/{self.file_name}", "w") as content:
            content.write(self.file_details)
    
    def create_multiple_files(self, directory_name, file_destination, loop_num):
        for new_file in range(loop_num):
            self.create_seed_file(directory_name, file_destination)
            # if self.file_name.find("-") != -1:
            # if new_file == self.first_number:
            with open(f"{directory_name}/{self.drop_allow}", "a") as text:
                text.write(self.file_name  + "\n")

makefake = MakeFakeData(1, "example_eighteen", "allowlist", 1, "originals")