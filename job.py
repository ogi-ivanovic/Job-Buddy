allSkills = ["Python", "C++", "Java", "SQL", "Javascript", "HTML", "CSS", "Ruby", "C#", "C", "Linux", "Bash", ".NET"]


class Job:
    def __init__(self, title, company, description, link):
        self.__title = title
        self.__company = company
        self.__description = description
        self.__link = link
        self.__matchingSkills = 0
        self.__skills = []
        for word in description.split():
            for skill in allSkills:
                if skill in word:
                    self.__skills.append(skill)
                    break

    def getTitle(self):
        return self.__title

    def getCompany(self):
        return self.__company

    def getDescription(self):
        return self.__description

    def getLink(self):
        return self.__link

    def getNumSkills(self):
        return len(self.__skills)

    def getNumMatchingSkills(self):
        return self.__matchingSkills

    def addMatchingSkill(self):
        self.__matchingSkills += 1

    def isSkill(self, skill):
        if skill in self.__skills:
            return True
        return False

    def getDisplay1(self):
        display = self.__title + " at " + self.__company + "\n"
        display += self.__link
        return display

    def getDisplay2(self):
        display = self.__title
        if len(display) > 40:
            return ""
        numSpacesNeeded = 45 - len(display)
        for i in range(numSpacesNeeded):
            display += " "
        display += self.__company
        if len(display) > 90:
            return ""
        numSpacesNeeded = 95 - len(display)
        for i in range(numSpacesNeeded):
            display += " "
        display += str(self.__matchingSkills)
        display += "\n"
        return display

