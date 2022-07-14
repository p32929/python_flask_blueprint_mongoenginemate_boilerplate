import os
from string import Template


class Generate:
    def get_module_name(self):
        # self.module_name = str.lower("User")
        self.module_name = str.lower(input("Enter module name: "))

    def _create_module_folder(self):
        if not os.path.exists(self._rel_dir):
            os.makedirs(self._rel_dir)
            return True

        return False

    def _create_module_files(self):
        file_names = [
            f"{self.module_name}_controller.py",
            f"{self.module_name}_dtos.py",
            # f"{self.module_name}_schema.py",
            f"{self.module_name}_service.py",
            f"{self.module_name}_test.py",
        ]

        for filename in file_names:
            target_filename = filename.split(
                "_")[-1].replace(".py", ".txt")
            target_filename = f"_{target_filename}"
            template_path = f"{self._script_dir}/templates/{target_filename}"
            app_file = open(template_path)
            raw_template = app_file.read()
            template = Template(raw_template)
            to_be_written = template.safe_substitute(
                name=self.module_name, uname=self.module_name.capitalize())

            with open(os.path.join(self._rel_dir, filename), 'w+') as temp_file:
                temp_file.write(to_be_written)

        # Update connector.py
        app_py = f"{self._script_dir}/src/connector.py"
        app_file = open(app_py, 'a+')
        app_file.write(
            f"from src.modules.{self.module_name}.{self.module_name}_controller import {self.module_name}_controller\n")
        app_file.write(
            f"app.register_blueprint({self.module_name}_controller, url_prefix='/{self.module_name}s')\n")
        app_file.close()

        # Schema
        filename = f"{self.module_name}_schema.py",
        target_filename = filename.split(
            "_")[-1].replace(".py", ".txt")
        target_filename = f"_{target_filename}"
        template_path = f"{self._script_dir}/templates/{target_filename}"
        app_file = open(template_path)
        raw_template = app_file.read()
        template = Template(raw_template)
        to_be_written = template.safe_substitute(
            name=self.module_name, uname=self.module_name.capitalize())

        with open(os.path.join(self._schema_dir, filename), 'w+') as temp_file:
            temp_file.write(to_be_written)

    def generate_files(self):
        print(f"Generating files for {self.module_name} module")
        self._script_dir = os.path.dirname(__file__)
        self._rel_dir = f"{self._script_dir}/src/modules/{self.module_name}/"
        self._schema_dir = f"{self._script_dir}/src/schemas/"
        folder_created = self._create_module_folder()
        if folder_created:
            self._create_module_files()
            print("Module generated successfully")
        else:
            print("Please delete the module folder first")


gen = Generate()
gen.get_module_name()
gen.generate_files()
