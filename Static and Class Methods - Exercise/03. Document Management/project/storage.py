from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __edit_element(element_id, collection, *args):
        for element in collection:
            if element.id == element_id:
                element.edit(*args)

    def edit_category(self, category_id, new_name):
        self.__edit_element(category_id, self.categories, new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        self.__edit_element(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        self.__edit_element(document_id, self.documents, new_file_name)

    @staticmethod
    def __delete_element(element_id, collection):
        for element in collection:
            if element.id == element_id:
                collection.remove(element)

    def delete_category(self, category_id):
        self.__delete_element(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_element(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_element(document_id, self.documents)

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        result = ""
        for document in self.documents:
            result += document.__repr__() + "\n"
        return result
