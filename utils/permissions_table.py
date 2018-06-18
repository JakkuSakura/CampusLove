from typing import Dict, Tuple, List


class PermissionsTable:

    def __init__(self):
        self.profile_status = [
            ('Love_openness', '恋爱/公开'),
            ('Love_hiding', '恋爱/隐藏'),
            ('Single_seeking', '单身/寻求'),
            ('Single_waiting', '单身/观望'),
        ]
        self.total_perms_names = []
        self.permissions_table = {}

    def getDefaultPerms(self) -> Dict[str, bool]:
        d = {}
        for e in self.total_perms_names:
            d[e] = False
        return d

    def set(self, status: Tuple[str, str], perms: Dict[str, bool]):
        self.permissions_table[status] = perms

    def getPermsDict(self, status):
        return self.permissions_table[status]


PERMISSIONS_TABLE = PermissionsTable()


def passive(action: str):
    return "passive_" + action


def positive(action: str):
    return "positive_" + action


def create_permissions(actions: List[str]):
    """
    :param actions: a str list based on which you want to generate both positive and passive permission tables
    :return: a tuple of final permission tables
    """

    PERMISSIONS_TABLE.perms = []

    for x in actions:
        PERMISSIONS_TABLE.total_perms_names.append(passive(x))
        PERMISSIONS_TABLE.total_perms_names.append(positive(x))

    tuples = tuple([(x, x) for x in PERMISSIONS_TABLE.total_perms_names])
    return tuples


if __name__ == "__main__":
    print("testing profile_permissions")
    print(create_permissions(['view', 'mail']))
    print(PERMISSIONS_TABLE.getDefaultPerms())

