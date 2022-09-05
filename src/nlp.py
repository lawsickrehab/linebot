# %%
from select import select
from articut import API
import re
from question import Question


# %%
class NLP:

    def __init__(self) -> None:
        self.api = API()
        self.funcConvert = {
            "isPositive": self.__isPositive,
            "negativeMatch": self.__negativeMatch
        }

    def parse(self, userInput: str, problems: list) -> dict:
        ret = dict()
        self.api.parse(userInput)
        for problemID in problems:
            problem = Question(problemID)
            for regxPair in problem.key:
                regxResult = re.findall(
                    regxPair[0], self.api.getResultWithTags(True))
                result = self.funcConvert[regxPair[1]](userInput, regxResult)

                ret[problemID] = result
                if result != -1:
                    break

        return ret

    def __isPositive(self, input: str, regxResult: list) -> int:
        negRegx = r'([沒否不])'
        if len(regxResult) > 0:
            result = re.findall(negRegx, regxResult)
            return len(result) % 2 == 0
        return -1

    def __negativeMatch(self, input: str, regxResult: list) -> int:
        return 1 if len(regxResult) > 0 else 0

