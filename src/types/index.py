from typing import TypedDict, List

class Resume(TypedDict):
    name: str
    email: str
    phone: str
    education: List[str]
    experience: List[str]
    skills: List[str]

class AnalysisResult(TypedDict):
    score: float
    feedback: str