import random

class Algorithm:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing algorithm: {self.name}")

class AlgorithmManager:
    def __init__(self):
        self.algorithms = []
        self.analytics = []

    def create_algorithm(self, name):
        algorithm = Algorithm(name)
        self.algorithms.append(algorithm)
        return algorithm

    def apply_to_tasks(self, algorithm, task_database):
        print(f"Applying algorithm '{algorithm.name}' to tasks in {task_database}")

    def random_impulse(self):
        return random.randint(1, 3)

    def analyze_impulses(self):
        impulse_data = []
        for algorithm in self.algorithms:
            impulse_data.append((algorithm.name, self.random_impulse()))
        return impulse_data

    def analyze_kpd(self):
        kpd_data = []
        for algorithm in self.algorithms:
            kpd_data.append((algorithm.name, random.uniform(0, 1)))
        return kpd_data

    def regulate_parameters(self):
        parameter_data = []
        for algorithm in self.algorithms:
            parameter_data.append((algorithm.name, random.randint(1, 100)))
        return parameter_data

    def analyze_all(self):
        impulses = self.analyze_impulses()
        kpd = self.analyze_kpd()
        parameters = self.regulate_parameters()
        self.analytics.extend(impulses)
        self.analytics.extend(kpd)
        self.analytics.extend(parameters)
