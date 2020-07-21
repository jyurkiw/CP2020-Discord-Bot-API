from ..util.mongo.mongo_handler import MongoHandler

from .skill import Skill


class CareerSkillsRoller(MongoHandler):
    def __init__(self, dbName):
        super().__init__(dbName, "career_skills")

    def getRoles(self):
        return self.collection.distinct("role_name")

    def getCareerSkills(self, role, points=40):
        skills = list()
        for doc in self.collection.find({"role_name": role}):
            skills += Skill.docToSkills(doc)

        # Distribute skill points
        Skill.distributePoints(skills)

        return skills
