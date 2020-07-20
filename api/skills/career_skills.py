from ..util.mongo.mongo_handler import MongoHandler

from .skill_tuple import Skill


class CareerSkillsRoller(MongoHandler):
    def __init__(self, dbName):
        super().__init__(dbName, "career_skills")

    def getRolls(self):
        return self.collection.distinct("role_name")

    def getCareerSkills(self, role, points=40):
        skills = list()
        for doc in db.collection.find({"role_name": role}):
            skills += Skill.docToSkills(doc)

        # Distribute skill points
        Skill.distributePoints(skills)

        return skills
