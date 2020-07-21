from ..util.mongo.mongo_handler import MongoHandler

from .skill import Skill


class PickupSkillsRoller(MongoHandler):
    def __init__(self, dbName):
        super().__init__(dbName, "skills")

    def addPickupSkills(self, skills, points):
        skSet = set([s.name for s in skills])

        for doc in self.collection.find():
            if doc.get("name") not in skSet:
                skills += Skill.docToSkills(doc, 0)

        # Distribute skill points
        Skill.distributePoints(skills, points=points)

        return PickupSkillsRoller.trimSkillList(skills)

    @staticmethod
    def trimSkillList(skills):
        return [s for s in skills if s.score > 0]
