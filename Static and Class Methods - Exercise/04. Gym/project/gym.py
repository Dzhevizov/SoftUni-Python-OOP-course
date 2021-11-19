from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def __add_element(element, collection):
        if element not in collection:
            collection.append(element)

    def add_customer(self, customer: Customer):
        self.__add_element(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_element(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_element(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_element(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_element(subscription, self.subscriptions)

    @staticmethod
    def __repr_element(res, element_id, collection):
        for element in collection:
            if element.id == element_id:
                res.append(element.__repr__())

    @staticmethod
    def __get_equipment_id(exercise_id, plans):
        for exercise in plans:
            if exercise.id == exercise_id:
                return exercise.equipment_id

    def subscription_info(self, subscription_id):
        result = []
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result.append(subscription.__repr__())
                customer_id = subscription.customer_id
                trainer_id = subscription.trainer_id
                exercise_id = subscription.exercise_id
                self.__repr_element(result, customer_id, self.customers)
                self.__repr_element(result, trainer_id, self.trainers)
                equipment_id = self.__get_equipment_id(exercise_id, self.plans)
                self.__repr_element(result, equipment_id, self.equipment)
                self.__repr_element(result, exercise_id, self.plans)
        return "\n".join(result)
