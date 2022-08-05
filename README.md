""" The Doe family
     jenny
    /     \
[CHILD]   [CHILD]
|         |
jimmy      john-[SPOUSE]-jane-[SIBLING]-james   
|                                      |
[CHILD]                               [CHILD]   
|                                      |
jezza-----------[SPOUSE]-------------- jason   

"""

jenny = Member(fullname="Jenny Doe")
jimmy = Member(fullname="Jimmy Doe")
john = Member(fullname="John Doe")
jane = Member(fullname="Jane Doe")
james = Member(fullname="James Doe")
jezza = Member(fullname="Jezza Doe")
jason = Member(fullname="Jason Doe")

jimmy.relationship_with(member=jenny, relation=Member.CHILD)  
jezza.relationship_with(member=jimmy, relation=Member.CHILD)  
john.relationship_with(member=jenny, relation=Member.CHILD)  
jane.relationship_with(member=john, relation=Member.SPOUSE)
james.relationship_with(member=jane, relation=Member.SIBLING)
jason.relationship_with(member=james, relation=Member.CHILD)
jezza.relationship_with(member=jason, relation=Member.SPOUSE)

james.get_closest_relationship_degree(jenny) # 3
john.get_closest_relationship_degree(james) # 2
jenny.get_closest_relationship_degree(jane) # 2
jason.get_closest_relationship_degree(jason) # 1
