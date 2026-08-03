from dataclasses import dataclass

@dataclass
class ClubMember:
    name:str
    guests:list=[]