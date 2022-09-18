import unittest


from .main import Tree, Member, Relations

tree = Tree()
jenny = Member(fullname="Jenny Doe")
jimmy = Member(fullname="Jimmy Doe")
john = Member(fullname="John Doe")
jane = Member(fullname="Jane Doe")
james = Member(fullname="James Doe")
jezza = Member(fullname="Jezza Doe")
jason = Member(fullname="Jason Doe")

class TestCloseRelationship(unittest.TestCase):

  def setUp(self) -> None:
    tree.relation_with(jimmy, jenny, relation=Relations.CHILD)
    tree.relation_with(jezza, jimmy, relation=Relations.CHILD)
    tree.relation_with(john, jenny, relation=Relations.CHILD)
    tree.relation_with(jane, john, relation=Relations.SPOUSE)
    tree.relation_with(james, jane, relation=Relations.SIBLING)
    tree.relation_with(jason, james, relation=Relations.CHILD)
    tree.relation_with(jezza, jason, relation=Relations.SPOUSE)
    
  def test_close_relationships(self):
    tree.get_closest_relationship_degree(james, jenny)  # 3
    tree.get_closest_relationship_degree(john, james)  # 2
    tree.get_closest_relationship_degree(jenny, jane)  # 2
    # relationship with itself is considered as 1
    tree.get_closest_relationship_degree(jason, jason)  # 1
    # for i in tree.relations:
    #   print(tree.relations[i].__dict__)
    