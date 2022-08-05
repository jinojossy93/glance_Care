

class Member:
    fullname: str = ""
    SPOUSE = 0
    CHILD = 1
    SIBLING = 2


    def __init__(self, fullname) -> None:
        self.fullname = fullname
    
    def __hash__(self) -> int:
        return hash(self.fullname)

    def __str__(self) -> str:
        return self.fullname


class Tree:
    def __init__(self) -> None:
        self.relations = dict()

    def find_member_m(self, relations, m):
        return self.recursive_msearch(relations, m)
    
    def recursive_msearch(self, relations, m):
        m_key = str(m)
        for mem in relations:
            if mem != "sibling_spouse":
                ss_keys = [m_key for m_key in relations[mem]["sibling_spouse"]]
                if mem == m_key:
                    return relations[mem]
                elif m_key in relations[mem].keys():
                    return relations[mem][m_key]
                elif m_key in ss_keys:
                    return relations[mem]["sibling_spouse"][ss_keys.index(m_key)]
                for k, rel in relations[mem].items():
                    if k == "sibling_spouse":
                        for index, rel in enumerate(relations[mem][k]):
                            if rel and "sibling_spouse" not in rel:
                                return self.recursive_msearch(relations[mem][k][index], m)
                    else:
                        return self.recursive_msearch(relations[mem][k], m)
            elif relations[mem]:
                for index, sibling_spouse in enumerate(relations[mem]):
                    for rel_key, _ in sibling_spouse.items():
                        if rel_key == m_key:
                            return relations[mem][index][rel_key]
            

    def relation_with(self, m2, m1, relation=Member.CHILD):
        m1_ref = self.find_member_m(self.relations, m1)
        m2_ref = self.find_member_m(self.relations, m2)
        if not m2_ref and m1_ref:
            if relation == Member.SIBLING or relation == Member.SPOUSE:
                if str(m1) in self.relations:
                    m1_ref["sibling_spouse"].append({
                        str(m2): {
                            "sibling_spouse": []
                        }
                    })
                else:
                    m1_ref["sibling_spouse"].append({
                        str(m2): {
                                "sibling_spouse": []
                            }
                        })
            else:
                m1_ref[str(m2)] = {
                        "sibling_spouse": []
                    }
        else:
            if relation == Member.SIBLING or relation == Member.SPOUSE:
                self.relations[str(m1)] = {
                            "sibling_spouse": [{
                                str(m2): {
                                    "sibling_spouse": []
                                }
                            }]
                        }
            else:
                self.relations[str(m1)] = {
                            "sibling_spouse": [],
                            str(m2): {
                                "sibling_spouse": []
                            }
                        }



if __name__ == "__main__":
    tree = Tree()
    jenny = Member(fullname="Jenny Doe")
    jimmy = Member(fullname="Jimmy Doe")
    john = Member(fullname="John Doe")
    jane = Member(fullname="Jane Doe")
    james = Member(fullname="James Doe")
    jezza = Member(fullname="Jezza Doe")
    jason = Member(fullname="Jason Doe")

    tree.relation_with(jimmy, jenny, relation=Member.CHILD)  
    tree.relation_with(jezza, jimmy, relation=Member.CHILD)  
    tree.relation_with(john, jenny, relation=Member.CHILD)  
    tree.relation_with(jane, john, relation=Member.SPOUSE)
    tree.relation_with(james, jane, relation=Member.SIBLING)
    tree.relation_with(jason, james, relation=Member.CHILD)
    tree.relation_with(jezza, jason, relation=Member.SPOUSE)
    print(tree)