import ex11
from ex11 import Node, Diagnoser, Record, build_tree, optimal_tree, parse_data

# Manually build a simple tree.
#                cough
#          Yes /       \ No
#        fever           healthy
#   Yes /     \ No
# influenza   cold

flu_leaf = Node("influenza", None, None)
cold_leaf = Node("cold", None, None)
inner_vertex = Node("fever", flu_leaf, cold_leaf)
healthy_leaf = Node("healthy", None, None)
root = Node("cough", inner_vertex, healthy_leaf)

diagnoser = Diagnoser(root)

flu_leaf2 = Node("influenza", None, None)
cold_leaf2 = Node("cold", None, None)
hard_leaf2 = Node("hard influenza", None, None)
headache_node2 = Node("headache", hard_leaf2, flu_leaf2)
inner_vertex2 = Node("fever", headache_node2, cold_leaf2)
healthy_leaf2 = Node("healthy", None, None)
root2 = Node("cough", inner_vertex2, healthy_leaf2)

diagnoser2 = Diagnoser(root2)
# Manually build of diagnoser2.
#                          cough
#                    Yes /       \ No
#                  fever           healthy
#             Yes /     \ No
#            headache   cold
#       Yes /     \ No
# hard influenza influenza

flu_leaf3 = Node("influenza", None, None)
cold_leaf3 = Node("cold", None, None)
hard_leaf3 = Node("hard influenza", None, None)
headache_node3 = Node("headache", hard_leaf3, flu_leaf3)
inner_vertex3 = Node("fever", headache_node3, cold_leaf3)
healthy_leaf3 = Node("hard influenza", None, None)
root3 = Node("cough", inner_vertex3, healthy_leaf3)

diagnoser3 = Diagnoser(root3)
# Manually build of diagnoser3.
#                          cough
#                    Yes /       \ No
#                  fever       hard influenza
#             Yes /     \ No
#            headache   cold
#       Yes /     \ No
# hard influenza influenza

flu_leaf4 = Node("influenza", None, None)
cold_leaf4 = Node("cold", None, None)
hard_leaf4 = Node("hard influenza", None, None)
headache_node4 = Node("headache", hard_leaf4, flu_leaf4)
inner_vertex4 = Node("fever", headache_node4, cold_leaf4)
healthy_leaf4 = Node("influenza", None, None)
root4 = Node("cough", inner_vertex4, healthy_leaf4)

diagnoser4 = Diagnoser(root4)
# Manually build of diagnoser4.
#                          cough
#                    Yes /       \ No
#                  fever        influenza
#             Yes /     \ No
#            headache   cold
#       Yes /     \ No
# hard influenza influenza

flu_leaf5 = Node("influenza", None, None)
cold_leaf5 = Node("cold", None, None)
healthy_leaf5 = Node("influenza", None, None)
inner_vertex6 = Node("headache", cold_leaf5, healthy_leaf5)
inner_vertex5 = Node("headache", flu_leaf5, cold_leaf5)
root5 = Node("cough", inner_vertex5, inner_vertex6)

diagnoser5 = Diagnoser(root5)
# Manually build of diagnoser5.
#                          cough
#                    Yes /       \ No
#                  headache      headache
#             Yes /     \ No  Yes /     \ No
#           influenza  cold     cold    healthy

root6 = Node("cold", None, None)
diagnoser6 = Diagnoser(root6)
# Manually build of diagnoser6.
#                          cold

diagnoser7 = Diagnoser(Node("cough", Node(None), Node(None)))
# Manually build of diagnoser7.
#                          cough
#                    Yes /       \ No
#                     None       None

flu_leaf8 = Node("influenza", None, None)
none_leaf8 = Node(None, None, None)
healthy_leaf8 = Node("healthy", None, None)
inner_vertex7 = Node("headache", flu_leaf8, flu_leaf8)
inner_vertex8 = Node("headache", healthy_leaf8, none_leaf8)
root8 = Node("cough", inner_vertex8, inner_vertex7)

diagnoser8 = Diagnoser(root8)
# Manually build of diagnoser8.
#                          cough
#                    Yes /       \ No
#                     headache  headache
#             Yes /     \ No  Yes /     \ No
#           healthy  None     influenza    influenza

none_leaf9 = Node(None, None, None)
healthy_leaf9 = Node("healthy", None, None)
inner_vertex9 = Node("headache", none_leaf9, none_leaf9)
inner_vertex10 = Node("headache", healthy_leaf9, none_leaf9)
root9 = Node("cough", inner_vertex10, inner_vertex9)

diagnoser9 = Diagnoser(root9)
# Manually build of diagnoser9.
#                          cough
#                    Yes /       \ No
#                     headache  headache
#             Yes /     \ No  Yes /     \ No
#           healthy    None     None    None

flu_leaf10 = Node("influenza", None, None)
cold_leaf10 = Node("cold", None, None)
healthy_leaf10 = Node("influenza", None, None)
inner_vertex11 = Node("headache", flu_leaf10, cold_leaf10)
inner_vertex12 = Node("headache", flu_leaf10, cold_leaf10)
root10 = Node("cough", inner_vertex11, inner_vertex12)

diagnoser10 = Diagnoser(root10)
# Manually build of diagnoser10.
#                          cough
#                    Yes /       \ No
#                     headache  headache
#             Yes /     \ No  Yes /     \ No
#           influenza  cold     influenza    cold


flu_leaf11 = Node("influenza", None, None)
cold_leaf11 = Node("cold", None, None)
healthy_leaf11 = Node("influenza", None, None)
inner_vertex13 = Node("fever", flu_leaf10, cold_leaf10)
inner_vertex14 = Node("headache", flu_leaf10, cold_leaf10)
root11 = Node("cough", inner_vertex13, inner_vertex14)

diagnoser11 = Diagnoser(root11)
# Manually build of diagnoser11.
#                          cough
#                    Yes /       \ No
#                     fever  headache
#             Yes /     \ No  Yes /     \ No
#           influenza  cold     influenza    cold


leafa = Node("a", None, None)
leafb = Node("b", None, None)
none_leaf = Node(None, None, None)
vertex2_1 = Node(2, leafa, leafb)
vertex2_2 = Node(2, leafa, leafb)
vertex2_3 = Node(2, none_leaf, none_leaf)
vertex3_3 = Node(3, vertex2_3, vertex2_2)
root12 = Node(1, vertex2_1, vertex3_3)

diagnoser12 = Diagnoser(root12)
# Manually build of diagnoser12.
#                                         1
#                           Yes /                   \ No
#                    2                                3
#             Yes /     \ No                Yes /           \ No
#                a       b                   2                2
#                                     Yes /     \ No   Yes /     \ No
#                                      None      None      a      b

root13 = Node(1)
root13.positive_child = Node(2)
root13.positive_child.positive_child = Node('a')
root13.positive_child.negative_child = Node('b')
root13.negative_child = Node(3)
root13.negative_child.positive_child = Node(4)
root13.negative_child.positive_child.positive_child = Node(None)
root13.negative_child.positive_child.negative_child = Node(None)
root13.negative_child.negative_child = Node(5)
root13.negative_child.negative_child.positive_child = Node(None)
root13.negative_child.negative_child.negative_child = Node(3)
root13.negative_child.negative_child.negative_child.positive_child = Node(None)
root13.negative_child.negative_child.negative_child.negative_child = Node(4)
root13.negative_child.negative_child.negative_child.negative_child.positive_child = Node(None)
root13.negative_child.negative_child.negative_child.negative_child.negative_child = Node(2)
root13.negative_child.negative_child.negative_child.negative_child.negative_child.positive_child = Node('a')
root13.negative_child.negative_child.negative_child.negative_child.negative_child.negative_child = Node('b')
diagnoser13 = Diagnoser(root13)
# Manually build of diagnoser13.
#           1
#      /          \
#     2                 3
#    / \          /           \
#   a   b         4             5
#                / \           /  \
#             None None      None   3
#                                 /   \
#                               None   4
#                                     /  \
#                                   None  2
#                                        / \
#                                       a   b
#
leaf_flu = Node("flu")
cough_1 = Node("cough", leaf_flu, Node(None))
fever_1 = Node("fever", cough_1, Node(None))
headache_1 = Node("headache", fever_1, Node(None))
fever_2 = Node("fever", leaf_flu, Node(None))
cough_2 = Node("cough", fever_2, Node(None))
headache_2 = Node("headache", cough_2, Node(None))
root14 = Node("stomachache", headache_1, headache_2)
diagnoser14 = Diagnoser(root14)
#
#                                                 stomachache
#                                             /                  \
#                                 headache                             headache
#                                /         \                          /         \
#                           fever           None                 cough           None
#                          /    \                               /    \
#                     cough      None                      fever      None
#                    /     \                              /     \
#                   flu     None                         flu     None
#
#

influenza_leaf = Node("influenza")
None_leaf = Node(None)
cough_vertex1 = Node("cough", influenza_leaf, None_leaf)
cough_vertex2 = Node("cough", None_leaf, None_leaf)
nausea_vertex1 = Node("nausea", cough_vertex1, cough_vertex2)
cough_vertex3 = Node("cough", None_leaf, None_leaf)
cough_vertex4 = Node("cough", None_leaf, None_leaf)
nausea_vertex2 = Node("nausea", cough_vertex3, cough_vertex4)
headache_vertex1 = Node("headache", nausea_vertex1, nausea_vertex2)
cough_vertex5 = Node("cough", None_leaf, None_leaf)
cold_leaf = Node("cold")
cough_vertex6 = Node("cough", cold_leaf, None_leaf)
nausea_vertex3 = Node("nausea", cough_vertex5, cough_vertex6)
cough_vertex7 = Node("cough", None_leaf, None_leaf)
cough_vertex8 = Node("cough", None_leaf, None_leaf)
nausea_vertex4 = Node("nausea", cough_vertex7, cough_vertex8)
headache_vertex2 = Node("headache", nausea_vertex3, nausea_vertex4)
fatigue_vertex1 = Node("fatigue", headache_vertex1, headache_vertex2)
cough_vertex9 = Node("cough", None_leaf, None_leaf)
mono_leaf = Node("mono")
cough_vertex10 = Node("cough", None_leaf, mono_leaf)
nausea_vertex5 = Node("nausea", cough_vertex9, cough_vertex10)
cough_vertex11 = Node("cough", None_leaf, None_leaf)
cough_vertex12 = Node("cough", None_leaf, None_leaf)
nausea_vertex6 = Node("nausea", cough_vertex11, cough_vertex12)
headache_vertex3 = Node("headache", nausea_vertex5, nausea_vertex6)
cough_vertex13 = Node("cough", None_leaf, None_leaf)
meningitis_leaf = Node("meningitis")
cough_vertex14 = Node("cough", None_leaf, meningitis_leaf)
nausea_vertex7 = Node("nausea", cough_vertex13, cough_vertex14)
cough_vertex15 = Node("cough", None_leaf, None_leaf)
healthy_leaf = Node("healthy")
cough_vertex16 = Node("cough", None_leaf, healthy_leaf)
nausea_vertex8 = Node("nausea", cough_vertex15, cough_vertex16)
headache_vertex4 = Node("headache", nausea_vertex7, nausea_vertex8)
fatigue_vertex2 = Node("fatigue", headache_vertex3, headache_vertex4)
cough_vertex17 = Node("cough", fatigue_vertex1, fatigue_vertex2)
diagnoser15 = Diagnoser(cough_vertex17)




cough_vertex18 = Node("cough", influenza_leaf, None_leaf)
cough_vertex19 = Node("cough", None_leaf, None_leaf)
nausea_vertex9 = Node("nausea", cough_vertex18, cough_vertex19)
cough_vertex20 = Node("cough", None_leaf, None_leaf)
cough_vertex21 = Node("cough", None_leaf, None_leaf)
nausea_vertex10 = Node("nausea", cough_vertex20, cough_vertex21)
headache_vertex5 = Node("headache", nausea_vertex9, nausea_vertex10)
cough_vertex22 = Node("cough", None_leaf, None_leaf)
cough_vertex23 = Node("cough", None_leaf, None_leaf)
nausea_vertex11 = Node("nausea", cough_vertex22, cough_vertex23)
cough_vertex24 = Node("cough", None_leaf, None_leaf)
cough_vertex25 = Node("cough", cold_leaf, None_leaf)
nausea_vertex12 = Node("nausea", cough_vertex24, cough_vertex25)
headache_vertex6 = Node("headache", nausea_vertex11, nausea_vertex12)
fatigue_vertex3 = Node("fatigue", headache_vertex5, headache_vertex6)
cough_vertex26 = Node("cough", None_leaf, None_leaf)
cough_vertex27 = Node("cough", None_leaf, None_leaf)
nausea_vertex13 = Node("nausea", cough_vertex26, cough_vertex27)
cough_vertex28 = Node("cough", None_leaf, None_leaf)
cough_vertex29 = Node("cough", None_leaf, None_leaf)
nausea_vertex14 = Node("nausea", cough_vertex28, cough_vertex29)
headache_vertex7 = Node("headache", nausea_vertex13, nausea_vertex14)
cough_vertex30 = Node("cough", None_leaf, None_leaf)
cough_vertex31 = Node("cough", None_leaf, meningitis_leaf)
nausea_vertex15 = Node("nausea", cough_vertex30, cough_vertex31)
cough_vertex32 = Node("cough", None_leaf, None_leaf)
cough_vertex33 = Node("cough", None_leaf, healthy_leaf)
nausea_vertex16 = Node("nausea", cough_vertex32, cough_vertex33)
headache_vertex8 = Node("headache", nausea_vertex15, nausea_vertex16)
fatigue_vertex4 = Node("fatigue", headache_vertex7, headache_vertex8)
cough_vertex34 = Node("cough", fatigue_vertex3, fatigue_vertex4)
diagnoser16 = Diagnoser(cough_vertex34)




fever_vertex1 = Node("fever", influenza_leaf, None_leaf)
fever_vertex2 = Node("fever", influenza_leaf, None_leaf)
headache_vertex9 = Node("headache", fever_vertex1, fever_vertex2)
fever_vertex3 = Node("fever", None_leaf, None_leaf)
fever_vertex4 = Node("fever", None_leaf, None_leaf)
headache_vertex10 = Node("headache", fever_vertex3, fever_vertex4)
fatigue_vertex5 = Node("fatigue", headache_vertex9, headache_vertex10)
fever_vertex5 = Node("fever", influenza_leaf, None_leaf)
fever_vertex6 = Node("fever", influenza_leaf, None_leaf)
headache_vertex11 = Node("headache", fever_vertex5, fever_vertex6)
fever_vertex7 = Node("fever", meningitis_leaf, None_leaf)
strep_leaf = Node("strep")
fever_vertex8 = Node("fever", strep_leaf, None_leaf)
headache_vertex12 = Node("headache", fever_vertex7, fever_vertex8)
fatigue_vertex6 = Node("fatigue", headache_vertex11, headache_vertex12)
cough_vertex35 = Node("cough", fatigue_vertex5, fatigue_vertex6)
fever_vertex9 = Node("fever", None_leaf, influenza_leaf)
fever_vertex10 = Node("fever", None_leaf, None_leaf)
headache_vertex13 = Node("headache", fever_vertex9, fever_vertex10)
fever_vertex11 = Node("fever", None_leaf, cold_leaf)
fever_vertex12 = Node("fever", None_leaf, None_leaf)
headache_vertex14 = Node("headache", fever_vertex11, fever_vertex12)
fatigue_vertex7 = Node("fatigue", headache_vertex13, headache_vertex14)
fever_vertex13 = Node("fever", None_leaf, mono_leaf)
fever_vertex14 = Node("fever", None_leaf, mono_leaf)
headache_vertex15 = Node("headache", fever_vertex13, fever_vertex14)
fever_vertex15 = Node("fever", None_leaf, cold_leaf)
fever_vertex16 = Node("fever", None_leaf, healthy_leaf)
headache_vertex16 = Node("headache", fever_vertex15, fever_vertex16)
fatigue_vertex8 = Node("fatigue", headache_vertex15, headache_vertex16)
cough_vertex36 = Node("cough", fatigue_vertex7, fatigue_vertex8)
fever_vertex17 = Node("fever", cough_vertex35, cough_vertex36)
diagnoser17 = Diagnoser(fever_vertex17)




fever_vertex18 = Node("fever", influenza_leaf, None_leaf)
fever_vertex19 = Node("fever", influenza_leaf, None_leaf)
headache_vertex17 = Node("headache", fever_vertex18, fever_vertex19)
fever_vertex20 = Node("fever", None_leaf, None_leaf)
fever_vertex21 = Node("fever", None_leaf, None_leaf)
headache_vertex18 = Node("headache", fever_vertex20, fever_vertex21)
fatigue_vertex9 = Node("fatigue", headache_vertex17, headache_vertex18)
fever_vertex22 = Node("fever", influenza_leaf, None_leaf)
fever_vertex23 = Node("fever", influenza_leaf, None_leaf)
headache_vertex19 = Node("headache", fever_vertex22, fever_vertex23)
fever_vertex24 = Node("fever", meningitis_leaf, None_leaf)
fever_vertex25 = Node("fever", strep_leaf, None_leaf)
headache_vertex20 = Node("headache", fever_vertex24, fever_vertex25)
fatigue_vertex10 = Node("fatigue", headache_vertex19, headache_vertex20)
cough_vertex37 = Node("cough", fatigue_vertex9, fatigue_vertex10)
fever_vertex26 = Node("fever", None_leaf, influenza_leaf)
fever_vertex27 = Node("fever", None_leaf, None_leaf)
headache_vertex21 = Node("headache", fever_vertex26, fever_vertex27)
fever_vertex28 = Node("fever", None_leaf, cold_leaf)
fever_vertex29 = Node("fever", None_leaf, None_leaf)
headache_vertex22 = Node("headache", fever_vertex28, fever_vertex29)
fatigue_vertex11 = Node("fatigue", headache_vertex21, headache_vertex22)
fever_vertex30 = Node("fever", None_leaf, mono_leaf)
fever_vertex31 = Node("fever", None_leaf, mono_leaf)
headache_vertex23 = Node("headache", fever_vertex30, fever_vertex31)
fever_vertex32 = Node("fever", None_leaf, cold_leaf)
fever_vertex33 = Node("fever", None_leaf, healthy_leaf)
headache_vertex24 = Node("headache", fever_vertex32, fever_vertex33)
fatigue_vertex12 = Node("fatigue", headache_vertex23, headache_vertex24)
cough_vertex38 = Node("cough", fatigue_vertex11, fatigue_vertex12)
fever_vertex34 = Node("fever", cough_vertex37, cough_vertex38)
diagnoser18 = Diagnoser(fever_vertex34)




fever_vertex35 = Node("fever", influenza_leaf, None_leaf)
fever_vertex36 = Node("fever", influenza_leaf, None_leaf)
headache_vertex25 = Node("headache", fever_vertex35, fever_vertex36)
fever_vertex37 = Node("fever", influenza_leaf, None_leaf)
fever_vertex38 = Node("fever", influenza_leaf, None_leaf)
headache_vertex26 = Node("headache", fever_vertex37, fever_vertex38)
fatigue_vertex13 = Node("fatigue", headache_vertex25, headache_vertex26)
fever_vertex39 = Node("fever", mono_leaf, None_leaf)
fever_vertex40 = Node("fever", mono_leaf, None_leaf)
headache_vertex27 = Node("headache", fever_vertex39, fever_vertex40)
fever_vertex41 = Node("fever", meningitis_leaf, None_leaf)
fever_vertex42 = Node("fever", strep_leaf, None_leaf)
headache_vertex28 = Node("headache", fever_vertex41, fever_vertex42)
fatigue_vertex14 = Node("fatigue", headache_vertex27, headache_vertex28)
cough_vertex39 = Node("cough", fatigue_vertex13, fatigue_vertex14)
fever_vertex43 = Node("fever", None_leaf, influenza_leaf)
fever_vertex44 = Node("fever", None_leaf, healthy_leaf)
headache_vertex29 = Node("headache", fever_vertex43, fever_vertex44)
fever_vertex45 = Node("fever", None_leaf, cold_leaf)
fever_vertex46 = Node("fever", None_leaf, cold_leaf)
headache_vertex30 = Node("headache", fever_vertex45, fever_vertex46)
fatigue_vertex15 = Node("fatigue", headache_vertex29, headache_vertex30)
fever_vertex47 = Node("fever", None_leaf, mono_leaf)
fever_vertex48 = Node("fever", None_leaf, mono_leaf)
headache_vertex31 = Node("headache", fever_vertex47, fever_vertex48)
fever_vertex49 = Node("fever", None_leaf, meningitis_leaf)
fever_vertex50 = Node("fever", None_leaf, healthy_leaf)
headache_vertex32 = Node("headache", fever_vertex49, fever_vertex50)
fatigue_vertex16 = Node("fatigue", headache_vertex31, headache_vertex32)
cough_vertex40 = Node("cough", fatigue_vertex15, fatigue_vertex16)
fever_vertex51 = Node("fever", cough_vertex39, cough_vertex40)
diagnoser19 = Diagnoser(fever_vertex51)




fever_vertex52 = Node("fever", influenza_leaf, None_leaf)
fever_vertex53 = Node("fever", influenza_leaf, None_leaf)
headache_vertex33 = Node("headache", fever_vertex52, fever_vertex53)
fever_vertex54 = Node("fever", influenza_leaf, None_leaf)
fever_vertex55 = Node("fever", influenza_leaf, None_leaf)
headache_vertex34 = Node("headache", fever_vertex54, fever_vertex55)
fatigue_vertex17 = Node("fatigue", headache_vertex33, headache_vertex34)
fever_vertex56 = Node("fever", influenza_leaf, None_leaf)
fever_vertex57 = Node("fever", influenza_leaf, None_leaf)
headache_vertex35 = Node("headache", fever_vertex56, fever_vertex57)
fever_vertex58 = Node("fever", meningitis_leaf, None_leaf)
fever_vertex59 = Node("fever", strep_leaf, None_leaf)
headache_vertex36 = Node("headache", fever_vertex58, fever_vertex59)
fatigue_vertex18 = Node("fatigue", headache_vertex35, headache_vertex36)
cough_vertex41 = Node("cough", fatigue_vertex17, fatigue_vertex18)
fever_vertex60 = Node("fever", None_leaf, influenza_leaf)
fever_vertex61 = Node("fever", None_leaf, healthy_leaf)
headache_vertex37 = Node("headache", fever_vertex60, fever_vertex61)
fever_vertex62 = Node("fever", None_leaf, cold_leaf)
fever_vertex63 = Node("fever", None_leaf, cold_leaf)
headache_vertex38 = Node("headache", fever_vertex62, fever_vertex63)
fatigue_vertex19 = Node("fatigue", headache_vertex37, headache_vertex38)
fever_vertex64 = Node("fever", None_leaf, influenza_leaf)
fever_vertex65 = Node("fever", None_leaf, healthy_leaf)
headache_vertex39 = Node("headache", fever_vertex64, fever_vertex65)
fever_vertex66 = Node("fever", None_leaf, meningitis_leaf)
fever_vertex67 = Node("fever", None_leaf, healthy_leaf)
headache_vertex40 = Node("headache", fever_vertex66, fever_vertex67)
fatigue_vertex20 = Node("fatigue", headache_vertex39, headache_vertex40)
cough_vertex42 = Node("cough", fatigue_vertex19, fatigue_vertex20)
fever_vertex68 = Node("fever", cough_vertex41, cough_vertex42)
diagnoser20 = Diagnoser(fever_vertex68)




fever_vertex69 = Node("fever", influenza_leaf, None_leaf)
fever_vertex70 = Node("fever", influenza_leaf, None_leaf)
headache_vertex41 = Node("headache", fever_vertex69, fever_vertex70)
fever_vertex71 = Node("fever", influenza_leaf, None_leaf)
fever_vertex72 = Node("fever", influenza_leaf, None_leaf)
headache_vertex42 = Node("headache", fever_vertex71, fever_vertex72)
fatigue_vertex21 = Node("fatigue", headache_vertex41, headache_vertex42)
fever_vertex73 = Node("fever", influenza_leaf, None_leaf)
fever_vertex74 = Node("fever", influenza_leaf, None_leaf)
headache_vertex43 = Node("headache", fever_vertex73, fever_vertex74)
fever_vertex75 = Node("fever", meningitis_leaf, None_leaf)
fever_vertex76 = Node("fever", strep_leaf, None_leaf)
headache_vertex44 = Node("headache", fever_vertex75, fever_vertex76)
fatigue_vertex22 = Node("fatigue", headache_vertex43, headache_vertex44)
cough_vertex43 = Node("cough", fatigue_vertex21, fatigue_vertex22)
fever_vertex77 = Node("fever", None_leaf, influenza_leaf)
fever_vertex78 = Node("fever", None_leaf, healthy_leaf)
headache_vertex45 = Node("headache", fever_vertex77, fever_vertex78)
fever_vertex79 = Node("fever", None_leaf, cold_leaf)
fever_vertex80 = Node("fever", None_leaf, cold_leaf)
headache_vertex46 = Node("headache", fever_vertex79, fever_vertex80)
fatigue_vertex23 = Node("fatigue", headache_vertex45, headache_vertex46)
fever_vertex81 = Node("fever", None_leaf, influenza_leaf)
fever_vertex82 = Node("fever", None_leaf, healthy_leaf)
headache_vertex47 = Node("headache", fever_vertex81, fever_vertex82)
fever_vertex83 = Node("fever", None_leaf, meningitis_leaf)
fever_vertex84 = Node("fever", None_leaf, healthy_leaf)
headache_vertex48 = Node("headache", fever_vertex83, fever_vertex84)
fatigue_vertex24 = Node("fatigue", headache_vertex47, headache_vertex48)
cough_vertex44 = Node("cough", fatigue_vertex23, fatigue_vertex24)
fever_vertex85 = Node("fever", cough_vertex43, cough_vertex44)
diagnoser21 = Diagnoser(fever_vertex85)




fever_vertex86 = Node("fever", influenza_leaf, None_leaf)
fever_vertex87 = Node("fever", mono_leaf, None_leaf)
nausea_vertex17 = Node("nausea", fever_vertex86, fever_vertex87)
fever_vertex88 = Node("fever", influenza_leaf, None_leaf)
fever_vertex89 = Node("fever", mono_leaf, None_leaf)
nausea_vertex18 = Node("nausea", fever_vertex88, fever_vertex89)
headache_vertex49 = Node("headache", nausea_vertex17, nausea_vertex18)
fever_vertex90 = Node("fever", influenza_leaf, None_leaf)
fever_vertex91 = Node("fever", meningitis_leaf, None_leaf)
nausea_vertex19 = Node("nausea", fever_vertex90, fever_vertex91)
fever_vertex92 = Node("fever", strep_leaf, None_leaf)
fever_vertex93 = Node("fever", strep_leaf, None_leaf)
nausea_vertex20 = Node("nausea", fever_vertex92, fever_vertex93)
headache_vertex50 = Node("headache", nausea_vertex19, nausea_vertex20)
fatigue_vertex25 = Node("fatigue", headache_vertex49, headache_vertex50)
fever_vertex94 = Node("fever", None_leaf, influenza_leaf)
fever_vertex95 = Node("fever", None_leaf, mono_leaf)
nausea_vertex21 = Node("nausea", fever_vertex94, fever_vertex95)
fever_vertex96 = Node("fever", None_leaf, influenza_leaf)
fever_vertex97 = Node("fever", None_leaf, mono_leaf)
nausea_vertex22 = Node("nausea", fever_vertex96, fever_vertex97)
headache_vertex51 = Node("headache", nausea_vertex21, nausea_vertex22)
fever_vertex98 = Node("fever", None_leaf, influenza_leaf)
fever_vertex99 = Node("fever", None_leaf, cold_leaf)
nausea_vertex23 = Node("nausea", fever_vertex98, fever_vertex99)
fever_vertex100 = Node("fever", None_leaf, strep_leaf)
fever_vertex101 = Node("fever", None_leaf, healthy_leaf)
nausea_vertex24 = Node("nausea", fever_vertex100, fever_vertex101)
headache_vertex52 = Node("headache", nausea_vertex23, nausea_vertex24)
fatigue_vertex26 = Node("fatigue", headache_vertex51, headache_vertex52)
fever_vertex102 = Node("fever", fatigue_vertex25, fatigue_vertex26)
diagnoser22 = Diagnoser(fever_vertex102)




cough_vertex45 = Node("cough", influenza_leaf, None_leaf)
cough_vertex46 = Node("cough", None_leaf, None_leaf)
nausea_vertex25 = Node("nausea", cough_vertex45, cough_vertex46)
cough_vertex47 = Node("cough", None_leaf, None_leaf)
cough_vertex48 = Node("cough", None_leaf, None_leaf)
nausea_vertex26 = Node("nausea", cough_vertex47, cough_vertex48)
headache_vertex53 = Node("headache", nausea_vertex25, nausea_vertex26)
cough_vertex49 = Node("cough", None_leaf, None_leaf)
cough_vertex50 = Node("cough", cold_leaf, None_leaf)
nausea_vertex27 = Node("nausea", cough_vertex49, cough_vertex50)
cough_vertex51 = Node("cough", None_leaf, None_leaf)
cough_vertex52 = Node("cough", None_leaf, None_leaf)
nausea_vertex28 = Node("nausea", cough_vertex51, cough_vertex52)
headache_vertex54 = Node("headache", nausea_vertex27, nausea_vertex28)
fatigue_vertex27 = Node("fatigue", headache_vertex53, headache_vertex54)
cough_vertex53 = Node("cough", None_leaf, None_leaf)
cough_vertex54 = Node("cough", None_leaf, None_leaf)
nausea_vertex29 = Node("nausea", cough_vertex53, cough_vertex54)
cough_vertex55 = Node("cough", None_leaf, None_leaf)
cough_vertex56 = Node("cough", None_leaf, None_leaf)
nausea_vertex30 = Node("nausea", cough_vertex55, cough_vertex56)
headache_vertex55 = Node("headache", nausea_vertex29, nausea_vertex30)
cough_vertex57 = Node("cough", None_leaf, None_leaf)
cough_vertex58 = Node("cough", None_leaf, meningitis_leaf)
nausea_vertex31 = Node("nausea", cough_vertex57, cough_vertex58)
cough_vertex59 = Node("cough", None_leaf, None_leaf)
cough_vertex60 = Node("cough", None_leaf, healthy_leaf)
nausea_vertex32 = Node("nausea", cough_vertex59, cough_vertex60)
headache_vertex56 = Node("headache", nausea_vertex31, nausea_vertex32)
fatigue_vertex28 = Node("fatigue", headache_vertex55, headache_vertex56)
cough_vertex61 = Node("cough", fatigue_vertex27, fatigue_vertex28)
diagnoser23 = Diagnoser(cough_vertex61)




headache_vertex57 = Node("headache", influenza_leaf, None_leaf)
headache_vertex58 = Node("headache", cold_leaf, None_leaf)
fever_vertex103 = Node("fever", headache_vertex57, headache_vertex58)
headache_vertex59 = Node("headache", None_leaf, None_leaf)
headache_vertex60 = Node("headache", None_leaf, None_leaf)
fever_vertex104 = Node("fever", headache_vertex59, headache_vertex60)
headache_vertex61 = Node("headache", fever_vertex103, fever_vertex104)
diagnoser24 = Diagnoser(headache_vertex61)




fever_vertex105 = Node("fever", influenza_leaf, None_leaf)
fever_vertex106 = Node("fever", meningitis_leaf, None_leaf)
cough_vertex62 = Node("cough", fever_vertex105, fever_vertex106)
fever_vertex107 = Node("fever", None_leaf, cold_leaf)
fever_vertex108 = Node("fever", None_leaf, healthy_leaf)
cough_vertex63 = Node("cough", fever_vertex107, fever_vertex108)
fever_vertex109 = Node("fever", cough_vertex62, cough_vertex63)
diagnoser25 = Diagnoser(fever_vertex109)


def print_in_order(diagno: Diagnoser):
    printable = ['']

    def print_in_order_helper(cur_node: Node):
        if cur_node is None:
            return
        if cur_node.positive_child:
            print_in_order_helper(cur_node.positive_child)
        printable[0] += str(cur_node.data) + ' '
        if cur_node.negative_child:
            print_in_order_helper(cur_node.negative_child)

    print_in_order_helper(diagno.root)
    return printable[0][:-1]


def test_diagnose1():
    assert "cold" == diagnoser.diagnose(["cough"])


def test_diagnose2():
    assert "influenza" == diagnoser2.diagnose(["cough", "fever"])


def test_success_rate_error():
    records = []
    try:
        diagnoser.calculate_success_rate(records)
    except ValueError as e:
        assert str(e) != ''


def test_success_rate1():
    records = [Record("influenza", ["cough", "fever"]), Record("healthy", []),
               Record('hard influenza', ["cougth", "fever", "headache"])]
    assert 0.6666666666666666 == diagnoser.calculate_success_rate(records)


def test_success_rate2():
    records2 = [Record("influenza", ["cough", "fever"]), Record("healthy", []),
                Record('hard influenza', ["cough", "fever", "headache"])]
    assert 1.0 == diagnoser2.calculate_success_rate(records2)


def test_success_rate3():
    records3 = [Record("influenza", ["cough", "fever"]),
                Record("indigestion", ["stomachache"])]
    assert 0.5 == diagnoser2.calculate_success_rate(records3)


def test_success_rate4():
    records4 = [Record("influenza", ["cough"]),
                Record("indigestion", ["stomachache"])]
    assert 0 == diagnoser7.calculate_success_rate(records4)


def test_all_illnesses1():
    result = diagnoser3.all_illnesses()
    assert "hard influenza" == result[0]


def test_all_illnesses2():
    assert diagnoser7.all_illnesses() == []


def test_all_illnesses3():
    assert diagnoser8.all_illnesses() == ["influenza", "healthy"]
    assert diagnoser9.all_illnesses() == ["healthy"]
    assert diagnoser10.all_illnesses() == ["influenza", "cold"] or \
           diagnoser10.all_illnesses() == ["cold", "influenza"]


def test_all_illnesses_and_build_tree():
    symptoms = []
    records = parse_data("test_all_illnesses.txt")
    for record in records:
        for symptom in record.symptoms:
            if symptom not in symptoms:
                symptoms.append(symptom)
    assert build_tree(records, symptoms).all_illnesses() == ["influenza", "cold", "strep", "mono", "healthy"], f"""the output from the function all_illnesses should not be:\n{build_tree(records, symptoms).all_illnesses()}\nbut: ["influenza", "cold", "strep", "mono", "healthy"]\nthe diagnoser was built by the function built_tree with the records taken from test_all_illnesses.txt"""


def test_paths_to_illness1():
    paths1 = diagnoser4.paths_to_illness('influenza')
    assert [[True, True, False], [False]] == paths1 or [[False], [True, True, False]] == paths1


def test_paths_to_illness2():
    paths2 = diagnoser4.paths_to_illness('cold')
    assert [[True, False]] == paths2


def test_paths_to_illness3():
    paths3 = diagnoser4.paths_to_illness('something_that_doesnt_exist')
    assert [] == paths3


def test_paths_to_illness4():
    paths4 = diagnoser6.paths_to_illness("cold")
    assert [[]] == paths4


def test_paths_to_illness5():
    paths5 = diagnoser2.paths_to_illness('healthy')
    assert [[False]] == paths5


def test_paths_to_illness6():
    paths6 = diagnoser5.paths_to_illness('cold')
    assert [[True, False], [False, True]] == paths6 or [[False, True], [True, False]] == paths6


def test_paths_to_illness7():
    paths7 = diagnoser7.paths_to_illness(None)
    assert [[True], [False]] == paths7 or [[False], [True]] == paths7
    assert sorted(diagnoser9.paths_to_illness(None)) == sorted(
        [[True, False], [False, True], [False, False]])


def test_paths_to_illnesses_and_build_tree():
    paths = [[], [[False, False, False, False, False, False, False, False, False, False,False, False, False, False]],
             [[True, True, False, False, False, False, False, False, False, False, False, False, False, False],
                 [True, False, False, False, False, False, False, False, False, False, False, False, False, False]],
             [[False, False, True, True, True, False, False, False, False, False, False, False, False, False],
                 [False, False, True, True, False, False, False, False, False, False, False, False, False, False],
                 [False, False, True, False, False, False, False, False, False,False, False, False, False, False]],
             [[False, False, False, False, False, True, True, True, True, False, False, False, False, False],
                 [False, False, False, False, False, True, True, True, False, False, False, False, False, False],
                 [False, False, False, False, False, True, True, False, False, False, False, False, False, False],
                 [False, False, False, False, False, True, False, False, False, False, False, False, False, False]],
             [[False, False, False, False, False, False, False, False,False, True, True, True, True, True],
                 [False, False, False, False, False, False, False, False, False, True, True, True, True, False],
                 [False, False, False, False, False, False, False, False, False, True, True, True, False, False],
                 [False, False, False, False, False, False, False, False, False, True, True, False, False, False],
                 [False, False, False, False, False, False, False, False, False, True, False, False, False, False]]]
    symptoms = []
    illnesses = []
    records = parse_data("test_all_illnesses.txt")
    for record in records:
        for symptom in record.symptoms:
            if symptom not in symptoms:
                symptoms.append(symptom)
        if record.illness not in illnesses:
            illnesses.append(record.illness)
    diagno = build_tree(records, symptoms)
    for i in range(len(paths)):
        assert sorted(diagno.paths_to_illness(illnesses[i])) == sorted(paths[i]), f"\nthe paths to the illness {illnesses[i]} \nis not: {diagno.paths_to_illness(illnesses[i])} \nbut: {paths[i]}\nthe diagnoser was built by the function built_tree with the records taken from test_all_illnesses.txt"


def test_build_tree():
    symptoms = ['a', 'b', 'd', 'g', 'k', 'a']
    records = parse_data("test_all_illnesses.txt")
    diagno = build_tree(records, symptoms)
    tree = "None a None k None a None g None a None k None a None d None a None k None a None g None a None k mono a None b None a None k None a None g None a None k None a None d None a None k None a None g None a None k mono a None a None a None k None a None g None a None k None a None d None a None k None a None g None a None k None a None b None a None k None a None g None a None k None a strep d None a None k None a cold g None a influenza k None a healthy"
    assert print_in_order(diagno) == tree, f"\nyour built_tree function did not built the expected tree, the records has taken from the file 'test_all_illnesses.txt' and  the symptoms ['a', 'b', 'd', 'g', 'k', 'a'] \nyour tree is:{print_in_order(diagno)} \nthe tree according to our data:{tree}"


def test_build_tree1():
    records = parse_data("tiny_data2.txt")
    tree1 = build_tree(records, ["headache", "fever"]).root

    assert "meningitis" == tree1.positive_child.positive_child.data
    assert "influenza" == tree1.positive_child.negative_child.data
    assert "cold" == tree1.negative_child.positive_child.data
    assert "healthy" == tree1.negative_child.negative_child.data


def test_build_tree2():
    records = parse_data("small_data1.txt")
    tree2 = build_tree(records, ["headache", "fever"]).root

    assert "influenza" == tree2.positive_child.positive_child.data
    assert "cold" == tree2.positive_child.negative_child.data
    assert "strep" == tree2.negative_child.positive_child.data
    assert "healthy" == tree2.negative_child.negative_child.data


def test_build_tree3():
    records = parse_data("medium_data1.txt")
    tree3 = build_tree(records, ["fever", "cough"]).root

    assert "influenza" == tree3.positive_child.positive_child.data
    assert "meningitis" == tree3.positive_child.negative_child.data
    assert "cold" == tree3.negative_child.positive_child.data
    assert "healthy" == tree3.negative_child.negative_child.data


def test_build_tree4():
    records = parse_data("medium_data2.txt")
    tree4 = build_tree(records, ["fever", "cough"]).root

    assert "influenza" == tree4.positive_child.positive_child.data
    assert "strep" == tree4.positive_child.negative_child.data
    assert "cold" == tree4.negative_child.positive_child.data
    assert "healthy" == tree4.negative_child.negative_child.data


def test_build_tree_errors():
    records = [Record("influenza", ["cough", "fever"]),
               Record("indigestion", ["stomachache"])]
    errors = ['']
    try:
        build_tree(records + ["non_record_type"], ["fever", "cough"])
    except TypeError as error1:
        errors[0] = str(error1)
        assert str(error1) != '', "you should add an error message to the error you raising (the error case checked is a non record type in the record list)"

    try:
        build_tree(records, ["1", 1])
    except TypeError as error2:
        assert str(error2) != '', "you should add an error message to the error you raising (the error case checked is a non str type in the symptoms list)"
        assert str(error2) != str(errors[0]), "you should add a *different* error message to the error you raising (the error case checked is a non str type in the symptoms list)"


def test_build_tree_empty_records():
    records = []
    tree4 = build_tree(records, ["fever", "cough"]).root

    assert tree4.positive_child.positive_child.data is None
    assert tree4.positive_child.negative_child.data is None
    assert tree4.negative_child.positive_child.data is None
    assert tree4.negative_child.negative_child.data is None

def test_build_tree_empty_symptoms():
    records1 = [Record("influenza", ["cough", "fever"]),
                Record("influenza", ["cough"]),
                Record("indigestion", ["stomachache"])]

    records2 = [Record("influenza", ["cough", "fever"]),
                Record("indigestion", ["stomachache"]),
                Record("indigestion", ["stomachache"])]

    tree1 = build_tree(records1, []).root
    tree2 = build_tree(records2, []).root
    assert tree1.data == "influenza"
    assert tree1.positive_child is None and tree1.negative_child is None

    assert tree2.data == "indigestion"
    assert tree2.positive_child is None and tree2.negative_child is None

def test_build_tree_empty_records_and_empty_symptoms():
    records = []
    tree4 = build_tree(records, []).root

    assert tree4.data is None


def test_optimal_tree1():
    records = parse_data("test_optimal_tree1.txt")
    tree = optimal_tree(records, ["cough", "fever", "headache"], 2).root

    assert "cough" == tree.data or "fever" == tree.data
    assert "cough" == tree.positive_child.data or "fever" == tree.positive_child.data


def test_optimal_tree2():
    records = parse_data("test_optimal_tree2.txt")
    tree = optimal_tree(records, ["cough", "fever", "headache"], 1).root

    assert "fever" == tree.data or "headache" == tree.data


def test_optimal_tree3():
    records = parse_data("test_optimal_tree3.txt")
    tree = optimal_tree(records, ["fever", "cough", "headache"], 2).root

    assert "influenza" == tree.positive_child.positive_child.data
    assert "meningitis" == tree.positive_child.negative_child.data
    assert "cold" == tree.negative_child.positive_child.data
    assert "healthy" == tree.negative_child.negative_child.data


def test_optimal_tree_errors():
    records = [Record("influenza", ["cough", "fever"]),
               Record("indigestion", ["stomachache"])]
    errors = ['', '', '', '']
    try:
        optimal_tree(records + ["non_record_type"], ["fever", "cough"], 1)
    except TypeError as error1:
        errors[0] = str(error1)
        assert str(error1) != '', "you should add an error message to the error you raising (the error case checked is a non record type in the record list)"

    try:
        optimal_tree(records, ["1", 1], 1)
    except TypeError as error2:
        assert str(error2) != '', "you should add an error message to the error you raising (the error case checked is a non str type in the symptoms list)"
        for e in errors:
            assert str(error2) != e, "you should add a *different* error message to the error you raising (the error case checked is a non str type in the symptoms list)"
        errors[1] = str(error2)

    try:
        optimal_tree(records, ["1"], -1)
    except ValueError as error3:
        assert str(error3) != '', "you should add an error message to the error you raising (the error case checked is a number below 0 for the depth varible)"
        for e in errors:
            assert str(error3) != e, "you should add a *different* error message to the error you raising (the error case checked is a number below 0 for the depth varible)"

    try:
        optimal_tree(records, ["1"], 2)
    except ValueError as error4:
        assert str(error4) != '', "you should add an error message to the error you raising (the error case checked is a number above the length of the symptoms for the depth varible)"
        for e in errors:
            assert str(error4) != e, "you should add a *different* error message to the error you raising (the error case checked is a number above the length of the symptoms for the depth varible)"
        errors[2] = str(error4)

    try:
        optimal_tree(records, ["1", "1"], 1)
    except ValueError as error5:
        assert str(error5) != '', "you should add an error message to the error you raising (the error case checked is a a symptom that appear twice)"
        for e in errors:
            assert str(error5) != e, "you should add a *different* error message to the error you raising (the error case checked is a a symptom that appear twice)"
        errors[3] = str(error5)


def test_optimal_tree_empty_symptoms():
    records1 = [Record("influenza", ["cough", "fever"]),
                Record("influenza", ["cough"]),
                Record("indigestion", ["stomachache"])]

    records2 = [Record("influenza", ["cough", "fever"]),
                Record("indigestion", ["stomachache"]),
                Record("indigestion", ["stomachache"])]

    tree1 = optimal_tree(records1, [], 0).root
    tree2 = optimal_tree(records2, [], 0).root
    tree3 = optimal_tree(records1, ["a", "b"], 0).root
    tree4 = optimal_tree(records2, ["a", "b"], 0).root
    assert tree1.data == "influenza"
    assert tree1.positive_child is None and tree1.negative_child is None

    assert tree2.data == "indigestion"
    assert tree2.positive_child is None and tree2.negative_child is None

    assert tree3.data == "influenza"
    assert tree3.positive_child is None and tree1.negative_child is None

    assert tree4.data == "indigestion"
    assert tree4.positive_child is None and tree2.negative_child is None


def test_minimize_false():
    diagnoser7.minimize()
    assert print_in_order(diagnoser7) == "None"
    diagnoser8.minimize()
    assert print_in_order(diagnoser8) == "healthy headache None cough influenza"
    diagnoser9.minimize()
    assert print_in_order(diagnoser9) == "healthy headache None cough None"
    diagnoser10.minimize()
    assert print_in_order(diagnoser10) == "influenza headache cold"
    diagnoser11.minimize()
    assert print_in_order(diagnoser11) == "influenza fever cold cough influenza headache cold"
    diagnoser12.minimize()
    assert print_in_order(diagnoser12) == "a 2 b 1 None 3 a 2 b"
    diagnoser13.minimize()
    assert print_in_order(diagnoser13) == "a 2 b 1 None 3 None 5 None 3 None 4 a 2 b"
    diagnoser14.minimize()
    assert print_in_order(diagnoser14) == "flu cough None fever None headache None stomachache flu fever None cough None headache None"
    diagnoser15.minimize()
    assert print_in_order(diagnoser15) == "influenza cough None nausea None headache None fatigue None nausea cold cough None headache None cough None nausea None cough mono headache None fatigue None nausea None cough meningitis headache None nausea None cough healthy"
    diagnoser16.minimize()
    assert print_in_order(diagnoser16) == "influenza cough None nausea None headache None fatigue None headache None nausea cold cough None cough None fatigue None nausea None cough meningitis headache None nausea None cough healthy"
    diagnoser17.minimize()
    assert print_in_order(diagnoser17) == "influenza fever None fatigue None cough influenza fever None fatigue meningitis fever None headache strep fever None fever None fever influenza headache None fatigue None fever cold headache None cough None fever mono fatigue None fever cold headache None fever healthy"
    diagnoser18.minimize()
    assert print_in_order(diagnoser18) == "influenza fever None fatigue None cough influenza fever None fatigue meningitis fever None headache strep fever None fever None fever influenza headache None fatigue None fever cold headache None cough None fever mono fatigue None fever cold headache None fever healthy"
    diagnoser19.minimize()
    assert print_in_order(diagnoser19) == "influenza fever None cough mono fever None fatigue meningitis fever None headache strep fever None fever None fever influenza headache None fever healthy fatigue None fever cold cough None fever mono fatigue None fever meningitis headache None fever healthy"
    diagnoser20.minimize()
    assert print_in_order(diagnoser20) == "influenza fever None cough influenza fever None fatigue meningitis fever None headache strep fever None fever None fever influenza headache None fever healthy fatigue None fever cold cough None fever influenza headache None fever healthy fatigue None fever meningitis headache None fever healthy"
    diagnoser21.minimize()
    assert print_in_order(diagnoser21) == "influenza fever None cough influenza fever None fatigue meningitis fever None headache strep fever None fever None fever influenza headache None fever healthy fatigue None fever cold cough None fever influenza headache None fever healthy fatigue None fever meningitis headache None fever healthy"
    diagnoser22.minimize()
    assert print_in_order(diagnoser22) == "influenza fever None nausea mono fever None fatigue influenza fever None nausea meningitis fever None headache strep fever None fever None fever influenza nausea None fever mono fatigue None fever influenza nausea None fever cold headache None fever strep nausea None fever healthy"
    diagnoser23.minimize()
    assert print_in_order(diagnoser23) == "influenza cough None nausea None headache None fatigue None nausea cold cough None headache None cough None fatigue None nausea None cough meningitis headache None nausea None cough healthy"
    diagnoser24.minimize()
    assert print_in_order(diagnoser24) == "influenza headache None fever cold headache None headache None"
    diagnoser25.minimize()
    assert print_in_order(diagnoser25) == "influenza fever None cough meningitis fever None fever None fever cold cough None fever healthy"

def test_minimize_true():
    diagnoser7.minimize(True)
    assert print_in_order(diagnoser7) == "None"
    diagnoser8.minimize(True)
    assert print_in_order(diagnoser8) == "healthy cough influenza"
    diagnoser9.minimize(True)
    assert print_in_order(diagnoser9) == "healthy"
    diagnoser10.minimize(True)
    assert print_in_order(diagnoser10) == "influenza headache cold"
    diagnoser11.minimize(True)
    assert print_in_order(diagnoser11) == "influenza fever cold cough influenza headache cold"
    diagnoser12.minimize(True)
    assert print_in_order(diagnoser12) == "a 2 b"
    diagnoser13.minimize(True)
    assert print_in_order(diagnoser13) == "a 2 b"
    diagnoser14.minimize(True)
    assert print_in_order(diagnoser14) == "flu"
    diagnoser15.minimize()
    diagnoser15.minimize(True)
    p = print_in_order(diagnoser15)
    assert p == "influenza fatigue cold cough mono fatigue meningitis headache healthy"
    diagnoser16.minimize(True)
    assert print_in_order(diagnoser16) == "influenza fatigue cold cough meningitis headache healthy"
    diagnoser17.minimize(True)
    assert print_in_order(diagnoser17) == "influenza cough influenza fatigue meningitis headache strep fever influenza fatigue cold cough mono fatigue cold headache healthy"
    diagnoser18.minimize(True)
    assert print_in_order(diagnoser18) == "influenza cough influenza fatigue meningitis headache strep fever influenza fatigue cold cough mono fatigue cold headache healthy"
    diagnoser19.minimize(True)
    assert print_in_order(diagnoser19) == "influenza cough mono fatigue meningitis headache strep fever influenza headache healthy fatigue cold cough mono fatigue meningitis headache healthy"
    diagnoser20.minimize(True)
    assert print_in_order(diagnoser20) == "influenza cough influenza fatigue meningitis headache strep fever influenza headache healthy fatigue cold cough influenza headache healthy fatigue meningitis headache healthy"
    diagnoser21.minimize(True)
    assert print_in_order(diagnoser21) == "influenza cough influenza fatigue meningitis headache strep fever influenza headache healthy fatigue cold cough influenza headache healthy fatigue meningitis headache healthy"
    diagnoser22.minimize(True)
    assert print_in_order(diagnoser22) == "influenza nausea mono fatigue influenza nausea meningitis headache strep fever influenza nausea mono fatigue influenza nausea cold headache strep nausea healthy"
    diagnoser23.minimize(True)
    assert print_in_order(diagnoser23) == "influenza fatigue cold cough meningitis headache healthy"
    diagnoser24.minimize(True)
    assert print_in_order(diagnoser24) == "influenza fever cold"
    diagnoser25.minimize(True)
    assert print_in_order(diagnoser25) == "influenza cough meningitis fever cold cough healthy"

def test_7():
    def check(n: Node):
        def helper(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.data != b.data:
                return False
            if helper(a.positive_child, b.positive_child):
                return helper(a.negative_child, b.negative_child)
            return False

        if n.positive_child is None:
            return False
        return helper(n.positive_child, n.negative_child)

    def check_for_nones(cur_root: Node):
        if cur_root is None:
            return False
        if cur_root.data is None:
            return True
        if cur_root.positive_child:
            is_there_none_in_pos = check_for_nones(cur_root.positive_child)
            is_there_none_in_neg = check_for_nones(cur_root.negative_child)
            return is_there_none_in_pos or is_there_none_in_neg
        return False

    files = ["tiny_data.txt", "tiny_data2.txt", "small_data.txt",
             "small_data1.txt", "medium_data.txt", "medium_data1.txt",
             "medium_data2.txt", "big_data.txt", "test_optimal_tree1.txt",
             "test_optimal_tree2.txt", "test_optimal_tree3.txt"]

    rates_built_tree = [1.0, 1.0, 0.9333333333333333, 0.9333333333333333, 0.9083333333333333, 0.9459459459459459, 0.9501133786848073, 0.9156666666666666, 1.0, 1.0, 1.0]
    rates_optimal = [[0.16666666666666666, 0.25, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.22358722358722358, 0.26077097505668934, 0.16666666666666666, 0.25, 0.5, 0.25], [0.3333333333333333, 0.5, 0.3333333333333333, 0.3333333333333333, 0.325, 0.40540540540540543, 0.4467120181405896, 0.32516666666666666, 0.5, 1.0, 0.5], [0.6666666666666666, 1.0, 0.6, 0.6, 0.5766666666666667, 0.6781326781326781, 0.7029478458049887, 0.5598333333333333, 1.0, 1.0, 1.0]]
    list_of_rates = [rates_optimal[0], rates_optimal[1], rates_optimal[2],
                     rates_built_tree]
    for i in range(len(list_of_rates)):
        rates = list_of_rates[i]
        for ind, file in enumerate(files):
            symps = []
            r = parse_data(file)
            for record in r:
                for s in record.symptoms:
                    if s not in symps:
                        symps.append(s)
            if i < len(list_of_rates) - 1:
                diagnoser = optimal_tree(r, list(symps), i)
            else:
                symps += [symps[0]]
                diagnoser = build_tree(r, list(symps))
            rate_before_minimizing = diagnoser.calculate_success_rate(r)
            diagnoser.minimize(False)
            assert check(
                diagnoser.root) == False, f"\nyour minimize(False) function dos not remove all duplications!\nfile name: {file},\nthe tree was built using the optimal_tree function with a depth of {i}" if i < 3 else f"\nyour minimize(False) function dos not remove all duplications!\nfile name: {file},\nthe tree was built using the built_tree function"
            rate_after_removing_duplications = diagnoser.calculate_success_rate(r)
            diagnoser.minimize(True)
            assert check_for_nones(diagnoser.root) == False, f"\nyour minimize(True) dos not remove all nones!\nfile name: {file},\nthe tree was built using the optimal_tree function with a depth of {i}" if i < 3 else f"\nyour minimize(True) dos not remove all nones!\nfile name: {file},\nthe tree was built using the built_tree function"
            rate_after_removing_empties = diagnoser.calculate_success_rate(r)
            assert rate_before_minimizing == rate_after_removing_duplications, f"\nyour minimize(False) function changes the rate of success of the diagnoser, it should not do that!\nbefore: {rate_before_minimizing}, after: {rate_after_removing_duplications}\nfile name: {file},\nthe tree was built using the optimal_tree function with a depth of {i}" if i < 3 else f"\nyour minimize(False) function changes the rate of success of the diagnoser, it should not do that!\nbefore: {rate_before_minimizing}\nafter: {rate_after_removing_duplications}\nfile name: {file}\nthe tree was built using the built_tree function"
            assert rate_after_removing_duplications == rate_after_removing_empties, f"\nyour minimize(True) function changes the rate of success of the diagnoser, it should not do that!\nbefore: {rate_after_removing_duplications}, after: {rate_after_removing_empties}\nfile name: {file},\nthe tree was built using the optimal_tree function with a depth of {i}" if i < 3 else f"\nyour minimize(True) function changes the rate of success of the diagnoser, it should not do that!\nbefore: {rate_after_removing_duplications}\nafter: {rate_after_removing_empties}\nfile name: {file},\nthe tree was built using the built_tree function"
            assert rate_after_removing_empties == rates[ind], f"\nthe rate you calculated dos not mach the rate we have in our data\nyour rate: {rate_after_removing_empties}, our rate: {rates[ind]}\nfile name: {file},\nthe tree was built using the optimal_tree function with a depth of {i}" if i < 3 else f"\nthe rate you calculated dos not mach the rate we have in our data\nyour rate: {rate_before_minimizing}, our rate: {rate_after_removing_duplications}\nfile name: {file},\nthe tree was built using the built_tree function"

