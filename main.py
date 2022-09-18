class Relations:
    SPOUSE = 0
    CHILD = 1
    SIBLING = 2


class Member:
    fullname: str = ""
    sibling: list[str] = []
    spouse: list[str] = []
    child: list[str] = []
    
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
            

    def relation_with(self, m1, m2, relation=Relations.CHILD):
        m1_ref = self.relations.get(str(m1))
        if not m1_ref:
            self.relations[str(m1)] = m1
            m1_ref = self.relations.get(str(m1))
        m2_ref = self.relations.get(str(m2))
        if not m2_ref:
            self.relations[str(m2)] = m2
            m2_ref = self.relations.get(str(m2))
        if relation == Relations.CHILD:
            if not m2_ref.child:
                m2_ref.child = [str(m1_ref)]
            else:
                m2_ref.child.append(str(m1_ref))
        elif relation == Relations.SPOUSE:
            if m2_ref.spouse:
                m2_ref.spouse.append(str(m1_ref))
            else:
                m2_ref.spouse = [str(m1_ref)]
        else:
            if m2_ref.sibling:
                m2_ref.sibling.append(str(m1_ref))
            else:
                m2_ref.sibling = [str(m1_ref)]
    def get_closest_relationship_degree(self, m1, m2):
        result = []
        # if its the same member just print 1 and return
        if m1 == m2:
            print(1)
            return
        count = 0
        m1_ref = self.relations.get(str(m1))
        # check the relationship from first member to second
        # if the first member is a node in lower level the relation path may not successful
        count, match = self.check_m(m1_ref, m2, count)
        if match:
            result.append(count)
        else:
            count = 0
            count, match = self.check_m(m2, m1, count)
            if match:
                result.append(count)

        # taking the minimum value from the possible multiple length from relationship traversal
        print(min(result) if result else 0)

    def check_m(self, m1, m2, count):
        match = False
        for mc in m1.child:
            c, match = self.check_m(self.relations.get(mc), m2, count)
            count += 1
            if match:
                return count+c, match
            count -= c
        if m1.sibling:
            count, match = self.count_m_list(m1.sibling, m2, count)
            if match:
                return count, match
        if m1.spouse:
            count, match = self.count_m_list(m1.spouse, m2, count)
            if match:
                return count, match
        return count, match

    def count_m_list(self, l, m, c):
        for mkey in l:
            c += 1
            if mkey == str(m):
                return c, True
            count, match = self.check_m(self.relations.get(mkey), m, c)
            if match:
                return count, match
        return c, False

